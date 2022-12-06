"""Generated client library for transcoder version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.transcoder.v1beta1 import transcoder_v1beta1_messages as messages


class TranscoderV1beta1(base_api.BaseApiClient):
  """Generated client library for service transcoder version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://transcoder.googleapis.com/'
  MTLS_BASE_URL = 'https://transcoder.mtls.googleapis.com/'

  _PACKAGE = 'transcoder'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'TranscoderV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new transcoder handle."""
    url = url or self.BASE_URL
    super(TranscoderV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_jobTemplates = self.ProjectsLocationsJobTemplatesService(self)
    self.projects_locations_jobs = self.ProjectsLocationsJobsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)
    self.v1beta1 = self.V1beta1Service(self)

  class ProjectsLocationsJobTemplatesService(base_api.BaseApiService):
    """Service class for the projects_locations_jobTemplates resource."""

    _NAME = 'projects_locations_jobTemplates'

    def __init__(self, client):
      super(TranscoderV1beta1.ProjectsLocationsJobTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a job template in the specified region.

      Args:
        request: (TranscoderProjectsLocationsJobTemplatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobTemplate) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobTemplates',
        http_method='POST',
        method_id='transcoder.projects.locations.jobTemplates.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['jobTemplateId'],
        relative_path='v1beta1/{+parent}/jobTemplates',
        request_field='jobTemplate',
        request_type_name='TranscoderProjectsLocationsJobTemplatesCreateRequest',
        response_type_name='JobTemplate',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a job template.

      Args:
        request: (TranscoderProjectsLocationsJobTemplatesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobTemplates/{jobTemplatesId}',
        http_method='DELETE',
        method_id='transcoder.projects.locations.jobTemplates.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobTemplatesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the job template data.

      Args:
        request: (TranscoderProjectsLocationsJobTemplatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobTemplate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobTemplates/{jobTemplatesId}',
        http_method='GET',
        method_id='transcoder.projects.locations.jobTemplates.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobTemplatesGetRequest',
        response_type_name='JobTemplate',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists job templates in the specified region.

      Args:
        request: (TranscoderProjectsLocationsJobTemplatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobTemplatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobTemplates',
        http_method='GET',
        method_id='transcoder.projects.locations.jobTemplates.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/jobTemplates',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobTemplatesListRequest',
        response_type_name='ListJobTemplatesResponse',
        supports_download=False,
    )

  class ProjectsLocationsJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs resource."""

    _NAME = 'projects_locations_jobs'

    def __init__(self, client):
      super(TranscoderV1beta1.ProjectsLocationsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a job in the specified region.

      Args:
        request: (TranscoderProjectsLocationsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='POST',
        method_id='transcoder.projects.locations.jobs.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}/jobs',
        request_field='job',
        request_type_name='TranscoderProjectsLocationsJobsCreateRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a job.

      Args:
        request: (TranscoderProjectsLocationsJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='DELETE',
        method_id='transcoder.projects.locations.jobs.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns the job data.

      Args:
        request: (TranscoderProjectsLocationsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method='GET',
        method_id='transcoder.projects.locations.jobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobsGetRequest',
        response_type_name='Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists jobs in the specified region.

      Args:
        request: (TranscoderProjectsLocationsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method='GET',
        method_id='transcoder.projects.locations.jobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/jobs',
        request_field='',
        request_type_name='TranscoderProjectsLocationsJobsListRequest',
        response_type_name='ListJobsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(TranscoderV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(TranscoderV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class V1beta1Service(base_api.BaseApiService):
    """Service class for the v1beta1 resource."""

    _NAME = 'v1beta1'

    def __init__(self, client):
      super(TranscoderV1beta1.V1beta1Service, self).__init__(client)
      self._upload_configs = {
          }

    def GetPublicKeys(self, request, global_params=None):
      r"""GetPublicKeys method for the v1beta1 service.

      Args:
        request: (TranscoderGetPublicKeysRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PublicKeys) The response message.
      """
      config = self.GetMethodConfig('GetPublicKeys')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetPublicKeys.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='transcoder.getPublicKeys',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta1/publicKeys',
        request_field='',
        request_type_name='TranscoderGetPublicKeysRequest',
        response_type_name='PublicKeys',
        supports_download=False,
    )
