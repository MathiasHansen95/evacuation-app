"""Generated client library for datastore version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.datastore.v1 import datastore_v1_messages as messages


class DatastoreV1(base_api.BaseApiClient):
  """Generated client library for service datastore version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://datastore.googleapis.com/'
  MTLS_BASE_URL = 'https://datastore.mtls.googleapis.com/'

  _PACKAGE = 'datastore'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/datastore']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DatastoreV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new datastore handle."""
    url = url or self.BASE_URL
    super(DatastoreV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_indexes = self.ProjectsIndexesService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsIndexesService(base_api.BaseApiService):
    """Service class for the projects_indexes resource."""

    _NAME = 'projects_indexes'

    def __init__(self, client):
      super(DatastoreV1.ProjectsIndexesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned google.longrunning.Operation, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status. During index creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with delete, then re-creating the index with create. Indexes with a single property cannot be created.

      Args:
        request: (GoogleDatastoreAdminV1Index) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.indexes.create',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/indexes',
        request_field='<request>',
        request_type_name='GoogleDatastoreAdminV1Index',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an existing index. An index can only be deleted if it is in a `READY` or `ERROR` state. On successful execution of the request, the index will be in a `DELETING` state. And on completion of the returned google.longrunning.Operation, the index will be removed. During index deletion, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, followed by calling delete again.

      Args:
        request: (DatastoreProjectsIndexesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='datastore.projects.indexes.delete',
        ordered_params=['projectId', 'indexId'],
        path_params=['indexId', 'projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/indexes/{indexId}',
        request_field='',
        request_type_name='DatastoreProjectsIndexesDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an index.

      Args:
        request: (DatastoreProjectsIndexesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDatastoreAdminV1Index) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='datastore.projects.indexes.get',
        ordered_params=['projectId', 'indexId'],
        path_params=['indexId', 'projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/indexes/{indexId}',
        request_field='',
        request_type_name='DatastoreProjectsIndexesGetRequest',
        response_type_name='GoogleDatastoreAdminV1Index',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the indexes that match the specified filters. Datastore uses an eventually consistent query to fetch the list of indexes and may occasionally return stale results.

      Args:
        request: (DatastoreProjectsIndexesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleDatastoreAdminV1ListIndexesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='datastore.projects.indexes.list',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/projects/{projectId}/indexes',
        request_field='',
        request_type_name='DatastoreProjectsIndexesListRequest',
        response_type_name='GoogleDatastoreAdminV1ListIndexesResponse',
        supports_download=False,
    )

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = 'projects_operations'

    def __init__(self, client):
      super(DatastoreV1.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (DatastoreProjectsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='datastore.projects.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='',
        request_type_name='DatastoreProjectsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatastoreProjectsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='datastore.projects.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatastoreProjectsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (DatastoreProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/operations/{operationsId}',
        http_method='GET',
        method_id='datastore.projects.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatastoreProjectsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (DatastoreProjectsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/operations',
        http_method='GET',
        method_id='datastore.projects.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='DatastoreProjectsOperationsListRequest',
        response_type_name='GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DatastoreV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def AllocateIds(self, request, global_params=None):
      r"""Allocates IDs for the given keys, which is useful for referencing an entity before it is inserted.

      Args:
        request: (DatastoreProjectsAllocateIdsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AllocateIdsResponse) The response message.
      """
      config = self.GetMethodConfig('AllocateIds')
      return self._RunMethod(
          config, request, global_params=global_params)

    AllocateIds.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.allocateIds',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:allocateIds',
        request_field='allocateIdsRequest',
        request_type_name='DatastoreProjectsAllocateIdsRequest',
        response_type_name='AllocateIdsResponse',
        supports_download=False,
    )

    def BeginTransaction(self, request, global_params=None):
      r"""Begins a new transaction.

      Args:
        request: (DatastoreProjectsBeginTransactionRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BeginTransactionResponse) The response message.
      """
      config = self.GetMethodConfig('BeginTransaction')
      return self._RunMethod(
          config, request, global_params=global_params)

    BeginTransaction.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.beginTransaction',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:beginTransaction',
        request_field='beginTransactionRequest',
        request_type_name='DatastoreProjectsBeginTransactionRequest',
        response_type_name='BeginTransactionResponse',
        supports_download=False,
    )

    def Commit(self, request, global_params=None):
      r"""Commits a transaction, optionally creating, deleting or modifying some entities.

      Args:
        request: (DatastoreProjectsCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CommitResponse) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Commit.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.commit',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:commit',
        request_field='commitRequest',
        request_type_name='DatastoreProjectsCommitRequest',
        response_type_name='CommitResponse',
        supports_download=False,
    )

    def Export(self, request, global_params=None):
      r"""Exports a copy of all or a subset of entities from Google Cloud Datastore to another storage system, such as Google Cloud Storage. Recent updates to entities may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

      Args:
        request: (DatastoreProjectsExportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Export')
      return self._RunMethod(
          config, request, global_params=global_params)

    Export.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.export',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:export',
        request_field='googleDatastoreAdminV1ExportEntitiesRequest',
        request_type_name='DatastoreProjectsExportRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Import(self, request, global_params=None):
      r"""Imports entities into Google Cloud Datastore. Existing entities with the same key are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportEntities operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Datastore.

      Args:
        request: (DatastoreProjectsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.import',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:import',
        request_field='googleDatastoreAdminV1ImportEntitiesRequest',
        request_type_name='DatastoreProjectsImportRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Lookup(self, request, global_params=None):
      r"""Looks up entities by key.

      Args:
        request: (DatastoreProjectsLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupResponse) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lookup.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.lookup',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:lookup',
        request_field='lookupRequest',
        request_type_name='DatastoreProjectsLookupRequest',
        response_type_name='LookupResponse',
        supports_download=False,
    )

    def ReserveIds(self, request, global_params=None):
      r"""Prevents the supplied keys' IDs from being auto-allocated by Cloud Datastore.

      Args:
        request: (DatastoreProjectsReserveIdsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReserveIdsResponse) The response message.
      """
      config = self.GetMethodConfig('ReserveIds')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReserveIds.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.reserveIds',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:reserveIds',
        request_field='reserveIdsRequest',
        request_type_name='DatastoreProjectsReserveIdsRequest',
        response_type_name='ReserveIdsResponse',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      r"""Rolls back a transaction.

      Args:
        request: (DatastoreProjectsRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RollbackResponse) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.rollback',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:rollback',
        request_field='rollbackRequest',
        request_type_name='DatastoreProjectsRollbackRequest',
        response_type_name='RollbackResponse',
        supports_download=False,
    )

    def RunAggregationQuery(self, request, global_params=None):
      r"""Runs an aggregation query.

      Args:
        request: (DatastoreProjectsRunAggregationQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RunAggregationQueryResponse) The response message.
      """
      config = self.GetMethodConfig('RunAggregationQuery')
      return self._RunMethod(
          config, request, global_params=global_params)

    RunAggregationQuery.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.runAggregationQuery',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:runAggregationQuery',
        request_field='runAggregationQueryRequest',
        request_type_name='DatastoreProjectsRunAggregationQueryRequest',
        response_type_name='RunAggregationQueryResponse',
        supports_download=False,
    )

    def RunQuery(self, request, global_params=None):
      r"""Queries for entities.

      Args:
        request: (DatastoreProjectsRunQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RunQueryResponse) The response message.
      """
      config = self.GetMethodConfig('RunQuery')
      return self._RunMethod(
          config, request, global_params=global_params)

    RunQuery.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='datastore.projects.runQuery',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}:runQuery',
        request_field='runQueryRequest',
        request_type_name='DatastoreProjectsRunQueryRequest',
        response_type_name='RunQueryResponse',
        supports_download=False,
    )
