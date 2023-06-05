# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.datastream import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.datastream_v1.services.datastream.async_client import (
    DatastreamAsyncClient,
)
from google.cloud.datastream_v1.services.datastream.client import DatastreamClient
from google.cloud.datastream_v1.types.datastream import (
    CreateConnectionProfileRequest,
    CreatePrivateConnectionRequest,
    CreateRouteRequest,
    CreateStreamRequest,
    DeleteConnectionProfileRequest,
    DeletePrivateConnectionRequest,
    DeleteRouteRequest,
    DeleteStreamRequest,
    DiscoverConnectionProfileRequest,
    DiscoverConnectionProfileResponse,
    FetchStaticIpsRequest,
    FetchStaticIpsResponse,
    GetConnectionProfileRequest,
    GetPrivateConnectionRequest,
    GetRouteRequest,
    GetStreamObjectRequest,
    GetStreamRequest,
    ListConnectionProfilesRequest,
    ListConnectionProfilesResponse,
    ListPrivateConnectionsRequest,
    ListPrivateConnectionsResponse,
    ListRoutesRequest,
    ListRoutesResponse,
    ListStreamObjectsRequest,
    ListStreamObjectsResponse,
    ListStreamsRequest,
    ListStreamsResponse,
    LookupStreamObjectRequest,
    OperationMetadata,
    StartBackfillJobRequest,
    StartBackfillJobResponse,
    StopBackfillJobRequest,
    StopBackfillJobResponse,
    UpdateConnectionProfileRequest,
    UpdateStreamRequest,
)
from google.cloud.datastream_v1.types.datastream_resources import (
    AvroFileFormat,
    BackfillJob,
    BigQueryDestinationConfig,
    BigQueryProfile,
    ConnectionProfile,
    DestinationConfig,
    Error,
    ForwardSshTunnelConnectivity,
    GcsDestinationConfig,
    GcsProfile,
    JsonFileFormat,
    MysqlColumn,
    MysqlDatabase,
    MysqlProfile,
    MysqlRdbms,
    MysqlSourceConfig,
    MysqlSslConfig,
    MysqlTable,
    OracleColumn,
    OracleProfile,
    OracleRdbms,
    OracleSchema,
    OracleSourceConfig,
    OracleTable,
    PostgresqlColumn,
    PostgresqlProfile,
    PostgresqlRdbms,
    PostgresqlSchema,
    PostgresqlSourceConfig,
    PostgresqlTable,
    PrivateConnection,
    PrivateConnectivity,
    Route,
    SourceConfig,
    SourceObjectIdentifier,
    StaticServiceIpConnectivity,
    Stream,
    StreamObject,
    Validation,
    ValidationMessage,
    ValidationResult,
    VpcPeeringConfig,
)

__all__ = (
    "DatastreamClient",
    "DatastreamAsyncClient",
    "CreateConnectionProfileRequest",
    "CreatePrivateConnectionRequest",
    "CreateRouteRequest",
    "CreateStreamRequest",
    "DeleteConnectionProfileRequest",
    "DeletePrivateConnectionRequest",
    "DeleteRouteRequest",
    "DeleteStreamRequest",
    "DiscoverConnectionProfileRequest",
    "DiscoverConnectionProfileResponse",
    "FetchStaticIpsRequest",
    "FetchStaticIpsResponse",
    "GetConnectionProfileRequest",
    "GetPrivateConnectionRequest",
    "GetRouteRequest",
    "GetStreamObjectRequest",
    "GetStreamRequest",
    "ListConnectionProfilesRequest",
    "ListConnectionProfilesResponse",
    "ListPrivateConnectionsRequest",
    "ListPrivateConnectionsResponse",
    "ListRoutesRequest",
    "ListRoutesResponse",
    "ListStreamObjectsRequest",
    "ListStreamObjectsResponse",
    "ListStreamsRequest",
    "ListStreamsResponse",
    "LookupStreamObjectRequest",
    "OperationMetadata",
    "StartBackfillJobRequest",
    "StartBackfillJobResponse",
    "StopBackfillJobRequest",
    "StopBackfillJobResponse",
    "UpdateConnectionProfileRequest",
    "UpdateStreamRequest",
    "AvroFileFormat",
    "BackfillJob",
    "BigQueryDestinationConfig",
    "BigQueryProfile",
    "ConnectionProfile",
    "DestinationConfig",
    "Error",
    "ForwardSshTunnelConnectivity",
    "GcsDestinationConfig",
    "GcsProfile",
    "JsonFileFormat",
    "MysqlColumn",
    "MysqlDatabase",
    "MysqlProfile",
    "MysqlRdbms",
    "MysqlSourceConfig",
    "MysqlSslConfig",
    "MysqlTable",
    "OracleColumn",
    "OracleProfile",
    "OracleRdbms",
    "OracleSchema",
    "OracleSourceConfig",
    "OracleTable",
    "PostgresqlColumn",
    "PostgresqlProfile",
    "PostgresqlRdbms",
    "PostgresqlSchema",
    "PostgresqlSourceConfig",
    "PostgresqlTable",
    "PrivateConnection",
    "PrivateConnectivity",
    "Route",
    "SourceConfig",
    "SourceObjectIdentifier",
    "StaticServiceIpConnectivity",
    "Stream",
    "StreamObject",
    "Validation",
    "ValidationMessage",
    "ValidationResult",
    "VpcPeeringConfig",
)
