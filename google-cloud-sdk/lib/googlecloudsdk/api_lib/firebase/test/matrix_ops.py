# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common test matrix operations used by Firebase Test Lab commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import collections
import datetime
import time

from apitools.base.py import exceptions as apitools_exceptions

from googlecloudsdk.api_lib.firebase.test import exceptions
from googlecloudsdk.api_lib.firebase.test import util
from googlecloudsdk.calliope import exceptions as calliope_exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import console_io
import six

_DEFAULT_STATUS_INTERVAL_SECS = 6.0
_TIMESTAMP_FORMAT = '%H:%M:%S'


class MatrixMonitor(object):
  """A monitor to follow and possibly cancel a single test matrix invocation.

  Attributes:
    matrix_id: {str} the unique ID of the matrix being monitored.
    completed_matrix_states: the set of TestMatrix.State enums representing all
      final matrix states.
  """

  def __init__(self,
               matrix_id,
               test_type,
               context,
               clock=datetime.datetime.now,
               status_interval_secs=None):
    """Construct a MatrixMonitor to monitor a single test matrix instance.

    Args:
      matrix_id: {str} the unique ID of the matrix being monitored.
      test_type: {str} the type of matrix test being run (e.g. 'robo')
      context: {str:obj} dict containing the gcloud command context, which
        includes the Testing API client & messages libs generated by Apitools.
      clock: injected function which returns a current datetime object when
        called. Used to generate time-stamps on progress messages.
      status_interval_secs: {float} how long to sleep between status checks.
    """
    self.matrix_id = matrix_id
    self._test_type = test_type
    self._client = context['testing_client']
    self._messages = context['testing_messages']
    self._clock = clock
    self._project = util.GetProject()
    self._max_status_length = 0

    if status_interval_secs is not None:
      self._status_interval_secs = status_interval_secs
    else:
      self._status_interval_secs = (
          properties.VALUES.test.matrix_status_interval.GetInt() or
          _DEFAULT_STATUS_INTERVAL_SECS)
      # Poll for matrix status half as fast if the end user is not running in
      # interactive mode (i.e. either sys.stdin or sys.stderr is not a terminal
      # i/o stream) such as when gcloud is called by a CI system like Jenkins).
      # This reduces Testing service load and API quota usage.
      if not console_io.IsInteractive(error=True):
        self._status_interval_secs *= 2

    exec_states = self._messages.TestExecution.StateValueValuesEnum
    self._state_names = {
        exec_states.VALIDATING: 'Validating',
        exec_states.PENDING: 'Pending',
        exec_states.RUNNING: 'Running',
        exec_states.FINISHED: 'Finished',
        exec_states.ERROR: 'Error',
        exec_states.UNSUPPORTED_ENVIRONMENT: 'Unsupported',
        exec_states.INCOMPATIBLE_ENVIRONMENT: 'Incompatible Environment',
        exec_states.INCOMPATIBLE_ARCHITECTURE: 'Incompatible Architecture',
        exec_states.CANCELLED: 'Cancelled',
        exec_states.INVALID: 'Invalid',
        exec_states.TEST_STATE_UNSPECIFIED: '*Unspecified*',
    }
    self._completed_execution_states = set([
        exec_states.FINISHED,
        exec_states.ERROR,
        exec_states.UNSUPPORTED_ENVIRONMENT,
        exec_states.INCOMPATIBLE_ENVIRONMENT,
        exec_states.INCOMPATIBLE_ARCHITECTURE,
        exec_states.CANCELLED,
        exec_states.INVALID,
    ])
    matrix_states = self._messages.TestMatrix.StateValueValuesEnum
    self.completed_matrix_states = set([
        matrix_states.FINISHED,
        matrix_states.ERROR,
        matrix_states.CANCELLED,
        matrix_states.INVALID,
    ])

  def HandleUnsupportedExecutions(self, matrix):
    """Report unsupported device dimensions and return supported test list.

    Args:
      matrix: a TestMatrix message.

    Returns:
      A list of TestExecution messages which have supported dimensions.
    """
    states = self._messages.TestExecution.StateValueValuesEnum
    supported_tests = []
    unsupported_dimensions = set()

    for test in matrix.testExecutions:
      if test.state == states.UNSUPPORTED_ENVIRONMENT:
        unsupported_dimensions.add(_FormatInvalidDimension(test.environment))
      else:
        supported_tests.append(test)

    if unsupported_dimensions:
      log.status.Print(
          'Some device dimensions are not compatible and will be skipped:'
          '\n  {d}'.format(d='\n  '.join(unsupported_dimensions)))
    log.status.Print(
        'Firebase Test Lab will execute your {t} test on {n} device(s). More '
        'devices may be added later if flaky test attempts are specified.'
        .format(t=self._test_type, n=len(supported_tests)))
    return supported_tests

  def _GetTestExecutionStatus(self, test_id):
    """Fetch the TestExecution state of a specific test within a matrix.

    This method is only intended to be used for a TestMatrix with exactly one
    supported TestExecution. It would be inefficient to use it iteratively on
    a larger TestMatrix.

    Args:
      test_id: ID of the TestExecution status to find.

    Returns:
      The TestExecution message matching the unique test_id.
    """
    matrix = self.GetTestMatrixStatus()
    for test in matrix.testExecutions:
      if test.id == test_id:
        return test
    # We should never get here.
    raise exceptions.TestExecutionNotFoundError(test_id, self.matrix_id)

  def MonitorTestExecutionProgress(self, test_id):
    """Monitor and report the progress of a single running test.

    This method prints more detailed test progress messages for the case where
    the matrix has exactly one supported test configuration.

    Args:
      test_id: str, the unique id of the single supported test in the matrix.

    Raises:
      TestLabInfrastructureError if the Test service reports a backend error.

    """
    states = self._messages.TestExecution.StateValueValuesEnum
    last_state = ''
    error = ''
    progress = []
    last_progress_len = 0

    while True:
      status = self._GetTestExecutionStatus(test_id)
      timestamp = self._clock().strftime(_TIMESTAMP_FORMAT)
      # Check for optional error and progress details
      details = status.testDetails
      if details:
        error = details.errorMessage or ''
        progress = details.progressMessages or []

      # Progress is cumulative, so only print what's new since the last update.
      for msg in progress[last_progress_len:]:
        log.status.Print('{0} {1}'.format(timestamp, msg.rstrip()))
      last_progress_len = len(progress)

      if status.state == states.ERROR:
        raise exceptions.TestLabInfrastructureError(error)

      if status.state == states.UNSUPPORTED_ENVIRONMENT:
        raise exceptions.AllDimensionsIncompatibleError(
            'Device dimensions are not compatible: {d}. '
            'Please use "gcloud firebase test android models list" to '
            'determine which device dimensions are compatible.'.format(
                d=_FormatInvalidDimension(status.environment)))

      # Inform user of test progress, typically PENDING -> RUNNING -> FINISHED
      if status.state != last_state:
        last_state = status.state
        log.status.Print('{0} Test is {1}'.format(
            timestamp, self._state_names[last_state]))

      if status.state in self._completed_execution_states:
        break

      self._SleepForStatusInterval()

    # Even if the single TestExecution is done, we also need to wait for the
    # matrix to reach a finalized state before monitoring is done.
    matrix = self.GetTestMatrixStatus()
    while matrix.state not in self.completed_matrix_states:
      log.debug('Matrix not yet complete, still in state: %s', matrix.state)
      self._SleepForStatusInterval()
      matrix = self.GetTestMatrixStatus()
    self._LogTestComplete(matrix.state)
    return

  def GetTestMatrixStatus(self):
    """Fetch the response from the GetTestMatrix rpc.

    Returns:
      A TestMatrix message holding the current state of the created tests.

    Raises:
      HttpException if the Test service reports a backend error.
    """
    request = self._messages.TestingProjectsTestMatricesGetRequest(
        projectId=self._project, testMatrixId=self.matrix_id)
    try:
      return self._client.projects_testMatrices.Get(request)
    except apitools_exceptions.HttpError as e:
      exc = calliope_exceptions.HttpException(e)
      exc.error_format = (
          'Http error {status_code} while monitoring test run: {message}')
      raise exc

  def MonitorTestMatrixProgress(self):
    """Monitor and report the progress of multiple running tests in a matrix."""
    while True:
      matrix = self.GetTestMatrixStatus()

      state_counts = collections.defaultdict(int)
      for test in matrix.testExecutions:
        state_counts[test.state] += 1

      self._UpdateMatrixStatus(state_counts)

      if matrix.state in self.completed_matrix_states:
        self._LogTestComplete(matrix.state)
        break
      self._SleepForStatusInterval()

  def _UpdateMatrixStatus(self, state_counts):
    """Update the matrix status line with the current test state counts.

    Example: 'Test matrix status: Finished:5 Running:3 Unsupported:2'

    Args:
      state_counts: {state:count} a dict mapping a test state to its frequency.
    """
    status = []
    timestamp = self._clock().strftime(_TIMESTAMP_FORMAT)
    for state, count in six.iteritems(state_counts):
      if count > 0:
        status.append('{s}:{c}'.format(s=self._state_names[state], c=count))
    status.sort()
    # Use \r so that the status summary will update on the same console line.
    out = '\r{0} Test matrix status: {1} '.format(timestamp, ' '.join(status))

    # Right-pad with blanks when the status line gets shorter.
    self._max_status_length = max(len(out), self._max_status_length)
    log.status.write(out.ljust(self._max_status_length))

  def _LogTestComplete(self, matrix_state):
    """Let the user know that their test matrix has completed running."""
    log.info('Test matrix completed in state: {0}'.format(matrix_state))
    log.status.Print('\n{0} testing complete.'.format(
        self._test_type.capitalize()))

  def _SleepForStatusInterval(self):
    time.sleep(self._status_interval_secs)

  def CancelTestMatrix(self):
    """Cancels an in-progress TestMatrix.

    Raises:
      HttpException if the Test service reports a back-end error.
    """
    request = self._messages.TestingProjectsTestMatricesCancelRequest(
        projectId=self._project, testMatrixId=self.matrix_id)
    try:
      self._client.projects_testMatrices.Cancel(request)
    except apitools_exceptions.HttpError as e:
      exc = calliope_exceptions.HttpException(e)
      exc.error_format = 'CancelTestMatrix: {message}'
      raise exc


def _FormatInvalidDimension(environment):
  """Return a human-readable string representing an invalid matrix dimension."""
  if getattr(environment, 'androidDevice', None) is not None:
    device = environment.androidDevice
    return ('[OS-version {vers} on {model}]'.format(
        model=device.androidModelId, vers=device.androidVersionId))
  if getattr(environment, 'iosDevice', None) is not None:
    device = environment.iosDevice
    return ('[OS-version {vers} on {model}]'.format(
        model=device.iosModelId, vers=device.iosVersionId))
  # Handle any new device environments here.
  return '[unknown-environment]'


def ReformatDuration(duration):
  """Reformat a Duration arg to work around ApiTools non-support of that type.

  Duration args are normally converted to an int in seconds (e.g. --timeout 5m
  becomes args.timeout with int value 300). Duration proto fields are converted
  to type string during discovery doc creation, so we have to convert the int
  back into a string-formatted Duration (i.e. append an 's') before
  passing it to the Testing Service.

  Args:
    duration: {int} the number of seconds in the time duration.

  Returns:
    String representation of the Duration with units of seconds.
  """
  return '{secs}s'.format(secs=duration)
