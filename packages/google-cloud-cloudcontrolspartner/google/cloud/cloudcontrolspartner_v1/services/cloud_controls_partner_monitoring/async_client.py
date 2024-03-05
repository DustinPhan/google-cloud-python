# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.cloudcontrolspartner_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_monitoring import (
    pagers,
)
from google.cloud.cloudcontrolspartner_v1.types import violations

from .client import CloudControlsPartnerMonitoringClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    CloudControlsPartnerMonitoringTransport,
)
from .transports.grpc_asyncio import CloudControlsPartnerMonitoringGrpcAsyncIOTransport


class CloudControlsPartnerMonitoringAsyncClient:
    """Service describing handlers for resources"""

    _client: CloudControlsPartnerMonitoringClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CloudControlsPartnerMonitoringClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudControlsPartnerMonitoringClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        CloudControlsPartnerMonitoringClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = CloudControlsPartnerMonitoringClient._DEFAULT_UNIVERSE

    violation_path = staticmethod(CloudControlsPartnerMonitoringClient.violation_path)
    parse_violation_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_violation_path
    )
    common_billing_account_path = staticmethod(
        CloudControlsPartnerMonitoringClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        CloudControlsPartnerMonitoringClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CloudControlsPartnerMonitoringClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        CloudControlsPartnerMonitoringClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        CloudControlsPartnerMonitoringClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        CloudControlsPartnerMonitoringClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudControlsPartnerMonitoringAsyncClient: The constructed client.
        """
        return CloudControlsPartnerMonitoringClient.from_service_account_info.__func__(CloudControlsPartnerMonitoringAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudControlsPartnerMonitoringAsyncClient: The constructed client.
        """
        return CloudControlsPartnerMonitoringClient.from_service_account_file.__func__(CloudControlsPartnerMonitoringAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return CloudControlsPartnerMonitoringClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CloudControlsPartnerMonitoringTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudControlsPartnerMonitoringTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = functools.partial(
        type(CloudControlsPartnerMonitoringClient).get_transport_class,
        type(CloudControlsPartnerMonitoringClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, CloudControlsPartnerMonitoringTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud controls partner monitoring async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.CloudControlsPartnerMonitoringTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = CloudControlsPartnerMonitoringClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_violations(
        self,
        request: Optional[Union[violations.ListViolationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListViolationsAsyncPager:
        r"""Lists Violations for a workload Callers may also choose to read
        across multiple Customers or for a single customer as per
        `AIP-159 <https://google.aip.dev/159>`__ by using '-' (the
        hyphen or dash character) as a wildcard character instead of
        {customer} & {workload}. Format:
        ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1

            async def sample_list_violations():
                # Create a client
                client = cloudcontrolspartner_v1.CloudControlsPartnerMonitoringAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1.ListViolationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_violations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1.types.ListViolationsRequest, dict]]):
                The request object. Message for requesting list of
                Violations
            parent (:class:`str`):
                Required. Parent resource Format
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.cloudcontrolspartner_v1.services.cloud_controls_partner_monitoring.pagers.ListViolationsAsyncPager:
                Response message for list customer
                violation requests
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = violations.ListViolationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_violations,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListViolationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_violation(
        self,
        request: Optional[Union[violations.GetViolationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> violations.Violation:
        r"""Gets details of a single Violation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import cloudcontrolspartner_v1

            async def sample_get_violation():
                # Create a client
                client = cloudcontrolspartner_v1.CloudControlsPartnerMonitoringAsyncClient()

                # Initialize request argument(s)
                request = cloudcontrolspartner_v1.GetViolationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_violation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.cloudcontrolspartner_v1.types.GetViolationRequest, dict]]):
                The request object. Message for getting a Violation
            name (:class:`str`):
                Required. Format:
                ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.cloudcontrolspartner_v1.types.Violation:
                Details of resource Violation
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = violations.GetViolationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_violation,
            default_retry=retries.AsyncRetry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "CloudControlsPartnerMonitoringAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("CloudControlsPartnerMonitoringAsyncClient",)
