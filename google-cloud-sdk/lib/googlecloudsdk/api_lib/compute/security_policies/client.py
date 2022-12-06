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
"""Security policy."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import exceptions as calliope_exceptions


class SecurityPolicy(object):
  """Abstracts SecurityPolicy resource."""

  def __init__(self, ref, compute_client=None):
    self.ref = ref
    self._compute_client = compute_client

  @property
  def _client(self):
    return self._compute_client.apitools_client

  @property
  def _messages(self):
    return self._compute_client.messages

  def _MakeDeleteRequestTuple(self):
    region = getattr(self.ref, 'region', None)
    if region is not None:
      return (self._client.regionSecurityPolicies, 'Delete',
              self._messages.ComputeRegionSecurityPoliciesDeleteRequest(
                  project=self.ref.project,
                  region=region,
                  securityPolicy=self.ref.Name()))
    return (self._client.securityPolicies, 'Delete',
            self._messages.ComputeSecurityPoliciesDeleteRequest(
                project=self.ref.project, securityPolicy=self.ref.Name()))

  def _MakeDescribeRequestTuple(self):
    region = getattr(self.ref, 'region', None)
    if region is not None:
      return (self._client.regionSecurityPolicies, 'Get',
              self._messages.ComputeRegionSecurityPoliciesGetRequest(
                  project=self.ref.project,
                  region=region,
                  securityPolicy=self.ref.Name()))
    return (self._client.securityPolicies, 'Get',
            self._messages.ComputeSecurityPoliciesGetRequest(
                project=self.ref.project, securityPolicy=self.ref.Name()))

  def _MakeCreateRequestTuple(self, security_policy):
    region = getattr(self.ref, 'region', None)
    if region is not None:
      return (self._client.regionSecurityPolicies, 'Insert',
              self._messages.ComputeRegionSecurityPoliciesInsertRequest(
                  project=self.ref.project,
                  region=region,
                  securityPolicy=security_policy))
    return (self._client.securityPolicies, 'Insert',
            self._messages.ComputeSecurityPoliciesInsertRequest(
                project=self.ref.project, securityPolicy=security_policy))

  def _MakePatchRequestTuple(self, security_policy):
    region = getattr(self.ref, 'region', None)
    if region is not None:
      return (self._client.regionSecurityPolicies, 'Patch',
              self._messages.ComputeRegionSecurityPoliciesPatchRequest(
                  project=self.ref.project,
                  region=region,
                  securityPolicy=self.ref.Name(),
                  securityPolicyResource=security_policy))
    return (self._client.securityPolicies, 'Patch',
            self._messages.ComputeSecurityPoliciesPatchRequest(
                project=self.ref.project,
                securityPolicy=self.ref.Name(),
                securityPolicyResource=security_policy))

  def Delete(self, only_generate_request=False):
    requests = [self._MakeDeleteRequestTuple()]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Describe(self, only_generate_request=False):
    requests = [self._MakeDescribeRequestTuple()]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Create(self, security_policy=None, only_generate_request=False):
    requests = [self._MakeCreateRequestTuple(security_policy)]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Patch(self, security_policy=None, only_generate_request=False):
    requests = [self._MakePatchRequestTuple(security_policy)]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests


class SecurityPolicyRule(object):
  """Abstracts SecurityPolicyRule resource."""

  def __init__(self, ref, compute_client=None):
    self.ref = ref
    self._compute_client = compute_client

  @property
  def _client(self):
    return self._compute_client.apitools_client

  @property
  def _messages(self):
    return self._compute_client.messages

  def _ConvertPriorityToInt(self, priority):
    try:
      int_priority = int(priority)
    except ValueError:
      raise calliope_exceptions.InvalidArgumentException(
          'priority', 'priority must be a valid non-negative integer.')
    if int_priority < 0:
      raise calliope_exceptions.InvalidArgumentException(
          'priority', 'priority must be a valid non-negative integer.')
    return int_priority

  def _ConvertAction(self, action):
    return {
        'deny-403': 'deny(403)',
        'deny-404': 'deny(404)',
        'deny-502': 'deny(502)',
        'redirect-to-recaptcha': 'redirect_to_recaptcha',
        'rate-based-ban': 'rate_based_ban'
    }.get(action, action)

  def _MakeDeleteRequestTuple(self):
    return (self._client.securityPolicies, 'RemoveRule',
            self._messages.ComputeSecurityPoliciesRemoveRuleRequest(
                project=self.ref.project,
                priority=self._ConvertPriorityToInt(self.ref.Name()),
                securityPolicy=self.ref.securityPolicy))

  def _MakeDescribeRequestTuple(self):
    return (self._client.securityPolicies, 'GetRule',
            self._messages.ComputeSecurityPoliciesGetRuleRequest(
                project=self.ref.project,
                priority=self._ConvertPriorityToInt(self.ref.Name()),
                securityPolicy=self.ref.securityPolicy))

  def _MakeCreateRequestTuple(self, src_ip_ranges, expression, action,
                              description, preview, redirect_options,
                              rate_limit_options, request_headers_to_add):
    """Generates a SecurityPolicies AddRule request.

    Args:
      src_ip_ranges: The list of IP ranges to match.
      expression: The CEVAL expression to match.
      action: The action to enforce on match.
      description: The description of the rule.
      preview: If true, the action will not be enforced.
      redirect_options: Parameters defining the redirect action, such as
        redirect type and redirect target.
      rate_limit_options: The rate limiting behavior for this rule.
      request_headers_to_add: A list of headers to add to requests that match
        this rule.

    Returns:
      A tuple containing the resource collection, verb, and request.
    """
    if src_ip_ranges:
      matcher = self._messages.SecurityPolicyRuleMatcher(
          versionedExpr=self._messages.SecurityPolicyRuleMatcher
          .VersionedExprValueValuesEnum('SRC_IPS_V1'),
          config=self._messages.SecurityPolicyRuleMatcherConfig(
              srcIpRanges=src_ip_ranges))
    elif expression:
      matcher = self._messages.SecurityPolicyRuleMatcher(
          expr=self._messages.Expr(expression=expression))

    security_policy_rule = self._messages.SecurityPolicyRule(
        priority=self._ConvertPriorityToInt(self.ref.Name()),
        description=description,
        action=self._ConvertAction(action),
        match=matcher,
        preview=preview)
    if redirect_options is not None:
      security_policy_rule.redirectOptions = redirect_options
    if request_headers_to_add is not None:
      security_policy_rule.headerAction = self._ConvertRequestHeadersToAdd(
          request_headers_to_add)

    if rate_limit_options is not None:
      security_policy_rule.rateLimitOptions = rate_limit_options

    return (self._client.securityPolicies, 'AddRule',
            self._messages.ComputeSecurityPoliciesAddRuleRequest(
                project=self.ref.project,
                securityPolicyRule=security_policy_rule,
                securityPolicy=self.ref.securityPolicy))

  def _MakePatchRequestTuple(self, src_ip_ranges, expression, action,
                             description, preview, redirect_options,
                             rate_limit_options, request_headers_to_add,
                             preconfig_waf_config):
    """Generates a SecurityPolicies PatchRule request.

    Args:
      src_ip_ranges: The list of IP ranges to match.
      expression: The CEVAL expression to match.
      action: The action to enforce on match.
      description: The description of the rule.
      preview: If true, the action will not be enforced.
      redirect_options: Parameters defining the redirect action, such as
        redirect type and redirect target.
      rate_limit_options: The rate limiting behavior for this rule.
      request_headers_to_add: A list of headers to add to requests that match
        this rule.
      preconfig_waf_config: preconfigured WAF configuration to be applied for
        this rule.

    Returns:
      A tuple containing the resource collection, verb, and request.
    """
    matcher = None
    if src_ip_ranges:
      matcher = self._messages.SecurityPolicyRuleMatcher(
          versionedExpr=self._messages.SecurityPolicyRuleMatcher
          .VersionedExprValueValuesEnum('SRC_IPS_V1'),
          config=self._messages.SecurityPolicyRuleMatcherConfig(
              srcIpRanges=src_ip_ranges))
    elif expression:
      matcher = self._messages.SecurityPolicyRuleMatcher(
          expr=self._messages.Expr(expression=expression))

    security_policy_rule = self._messages.SecurityPolicyRule(
        priority=self._ConvertPriorityToInt(self.ref.Name()),
        description=description,
        action=self._ConvertAction(action),
        match=matcher,
        preview=preview)
    if redirect_options is not None:
      security_policy_rule.redirectOptions = redirect_options
    if request_headers_to_add is not None:
      security_policy_rule.headerAction = self._ConvertRequestHeadersToAdd(
          request_headers_to_add)

    if rate_limit_options is not None:
      security_policy_rule.rateLimitOptions = rate_limit_options
    if preconfig_waf_config is not None:
      security_policy_rule.preconfiguredWafConfig = preconfig_waf_config

    return (self._client.securityPolicies, 'PatchRule',
            self._messages.ComputeSecurityPoliciesPatchRuleRequest(
                project=self.ref.project,
                priority=self._ConvertPriorityToInt(self.ref.Name()),
                securityPolicyRule=security_policy_rule,
                securityPolicy=self.ref.securityPolicy))

  def _ConvertRequestHeadersToAdd(self, request_headers_to_add):
    """Converts a request-headers-to-add string list into an HttpHeaderAction.

    Args:
      request_headers_to_add: A dict of headers to add to requests that match
        this rule. Leading whitespace in each header name and value is stripped.

    Returns:
      An HttpHeaderAction object with a populated request_headers_to_add field.
    """
    header_action = self._messages.SecurityPolicyRuleHttpHeaderAction()
    for hdr_name, hdr_val in request_headers_to_add.items():
      header_to_add = (
          self._messages.SecurityPolicyRuleHttpHeaderActionHttpHeaderOption())
      header_to_add.headerName = hdr_name.strip()
      header_to_add.headerValue = hdr_val.lstrip()
      header_action.requestHeadersToAdds.append(header_to_add)
    return header_action

  def Delete(self, only_generate_request=False):
    requests = [self._MakeDeleteRequestTuple()]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Describe(self, only_generate_request=False):
    requests = [self._MakeDescribeRequestTuple()]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Create(self,
             src_ip_ranges=None,
             expression=None,
             action=None,
             description=None,
             preview=False,
             redirect_options=None,
             rate_limit_options=None,
             request_headers_to_add=None,
             only_generate_request=False):
    """Make and optionally send a request to Create a security policy rule."""
    requests = [
        self._MakeCreateRequestTuple(src_ip_ranges, expression, action,
                                     description, preview, redirect_options,
                                     rate_limit_options, request_headers_to_add)
    ]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests

  def Patch(self,
            src_ip_ranges=None,
            expression=None,
            action=None,
            description=None,
            preview=None,
            redirect_options=None,
            rate_limit_options=None,
            request_headers_to_add=None,
            preconfig_waf_config=None,
            only_generate_request=False):
    """Make and optionally send a request to Patch a security policy rule."""
    requests = [
        self._MakePatchRequestTuple(src_ip_ranges, expression, action,
                                    description, preview, redirect_options,
                                    rate_limit_options, request_headers_to_add,
                                    preconfig_waf_config)
    ]
    if not only_generate_request:
      return self._compute_client.MakeRequests(requests)
    return requests
