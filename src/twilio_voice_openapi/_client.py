# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import archives, settings, ip_records, byoc_trunks, source_ip_mappings
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TwilioVoiceOpenAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.connection_policies import connection_policies
from .resources.dialing_permissions import dialing_permissions

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "TwilioVoiceOpenAPI",
    "AsyncTwilioVoiceOpenAPI",
    "Client",
    "AsyncClient",
]


class TwilioVoiceOpenAPI(SyncAPIClient):
    archives: archives.ArchivesResource
    byoc_trunks: byoc_trunks.ByocTrunksResource
    connection_policies: connection_policies.ConnectionPoliciesResource
    dialing_permissions: dialing_permissions.DialingPermissionsResource
    settings: settings.SettingsResource
    ip_records: ip_records.IPRecordsResource
    source_ip_mappings: source_ip_mappings.SourceIPMappingsResource
    with_raw_response: TwilioVoiceOpenAPIWithRawResponse
    with_streaming_response: TwilioVoiceOpenAPIWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous TwilioVoiceOpenAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `TWILIO_VOICE_OPENAPI_USERNAME`
        - `password` from `TWILIO_VOICE_OPENAPI_PASSWORD`
        """
        if username is None:
            username = os.environ.get("TWILIO_VOICE_OPENAPI_USERNAME")
        if username is None:
            raise TwilioVoiceOpenAPIError(
                "The username client option must be set either by passing username to the client or by setting the TWILIO_VOICE_OPENAPI_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("TWILIO_VOICE_OPENAPI_PASSWORD")
        if password is None:
            raise TwilioVoiceOpenAPIError(
                "The password client option must be set either by passing password to the client or by setting the TWILIO_VOICE_OPENAPI_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("TWILIO_VOICE_OPENAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://voice.twilio.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.archives = archives.ArchivesResource(self)
        self.byoc_trunks = byoc_trunks.ByocTrunksResource(self)
        self.connection_policies = connection_policies.ConnectionPoliciesResource(self)
        self.dialing_permissions = dialing_permissions.DialingPermissionsResource(self)
        self.settings = settings.SettingsResource(self)
        self.ip_records = ip_records.IPRecordsResource(self)
        self.source_ip_mappings = source_ip_mappings.SourceIPMappingsResource(self)
        self.with_raw_response = TwilioVoiceOpenAPIWithRawResponse(self)
        self.with_streaming_response = TwilioVoiceOpenAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTwilioVoiceOpenAPI(AsyncAPIClient):
    archives: archives.AsyncArchivesResource
    byoc_trunks: byoc_trunks.AsyncByocTrunksResource
    connection_policies: connection_policies.AsyncConnectionPoliciesResource
    dialing_permissions: dialing_permissions.AsyncDialingPermissionsResource
    settings: settings.AsyncSettingsResource
    ip_records: ip_records.AsyncIPRecordsResource
    source_ip_mappings: source_ip_mappings.AsyncSourceIPMappingsResource
    with_raw_response: AsyncTwilioVoiceOpenAPIWithRawResponse
    with_streaming_response: AsyncTwilioVoiceOpenAPIWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTwilioVoiceOpenAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `TWILIO_VOICE_OPENAPI_USERNAME`
        - `password` from `TWILIO_VOICE_OPENAPI_PASSWORD`
        """
        if username is None:
            username = os.environ.get("TWILIO_VOICE_OPENAPI_USERNAME")
        if username is None:
            raise TwilioVoiceOpenAPIError(
                "The username client option must be set either by passing username to the client or by setting the TWILIO_VOICE_OPENAPI_USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("TWILIO_VOICE_OPENAPI_PASSWORD")
        if password is None:
            raise TwilioVoiceOpenAPIError(
                "The password client option must be set either by passing password to the client or by setting the TWILIO_VOICE_OPENAPI_PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("TWILIO_VOICE_OPENAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://voice.twilio.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.archives = archives.AsyncArchivesResource(self)
        self.byoc_trunks = byoc_trunks.AsyncByocTrunksResource(self)
        self.connection_policies = connection_policies.AsyncConnectionPoliciesResource(self)
        self.dialing_permissions = dialing_permissions.AsyncDialingPermissionsResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.ip_records = ip_records.AsyncIPRecordsResource(self)
        self.source_ip_mappings = source_ip_mappings.AsyncSourceIPMappingsResource(self)
        self.with_raw_response = AsyncTwilioVoiceOpenAPIWithRawResponse(self)
        self.with_streaming_response = AsyncTwilioVoiceOpenAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TwilioVoiceOpenAPIWithRawResponse:
    def __init__(self, client: TwilioVoiceOpenAPI) -> None:
        self.archives = archives.ArchivesResourceWithRawResponse(client.archives)
        self.byoc_trunks = byoc_trunks.ByocTrunksResourceWithRawResponse(client.byoc_trunks)
        self.connection_policies = connection_policies.ConnectionPoliciesResourceWithRawResponse(
            client.connection_policies
        )
        self.dialing_permissions = dialing_permissions.DialingPermissionsResourceWithRawResponse(
            client.dialing_permissions
        )
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)
        self.ip_records = ip_records.IPRecordsResourceWithRawResponse(client.ip_records)
        self.source_ip_mappings = source_ip_mappings.SourceIPMappingsResourceWithRawResponse(client.source_ip_mappings)


class AsyncTwilioVoiceOpenAPIWithRawResponse:
    def __init__(self, client: AsyncTwilioVoiceOpenAPI) -> None:
        self.archives = archives.AsyncArchivesResourceWithRawResponse(client.archives)
        self.byoc_trunks = byoc_trunks.AsyncByocTrunksResourceWithRawResponse(client.byoc_trunks)
        self.connection_policies = connection_policies.AsyncConnectionPoliciesResourceWithRawResponse(
            client.connection_policies
        )
        self.dialing_permissions = dialing_permissions.AsyncDialingPermissionsResourceWithRawResponse(
            client.dialing_permissions
        )
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)
        self.ip_records = ip_records.AsyncIPRecordsResourceWithRawResponse(client.ip_records)
        self.source_ip_mappings = source_ip_mappings.AsyncSourceIPMappingsResourceWithRawResponse(
            client.source_ip_mappings
        )


class TwilioVoiceOpenAPIWithStreamedResponse:
    def __init__(self, client: TwilioVoiceOpenAPI) -> None:
        self.archives = archives.ArchivesResourceWithStreamingResponse(client.archives)
        self.byoc_trunks = byoc_trunks.ByocTrunksResourceWithStreamingResponse(client.byoc_trunks)
        self.connection_policies = connection_policies.ConnectionPoliciesResourceWithStreamingResponse(
            client.connection_policies
        )
        self.dialing_permissions = dialing_permissions.DialingPermissionsResourceWithStreamingResponse(
            client.dialing_permissions
        )
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)
        self.ip_records = ip_records.IPRecordsResourceWithStreamingResponse(client.ip_records)
        self.source_ip_mappings = source_ip_mappings.SourceIPMappingsResourceWithStreamingResponse(
            client.source_ip_mappings
        )


class AsyncTwilioVoiceOpenAPIWithStreamedResponse:
    def __init__(self, client: AsyncTwilioVoiceOpenAPI) -> None:
        self.archives = archives.AsyncArchivesResourceWithStreamingResponse(client.archives)
        self.byoc_trunks = byoc_trunks.AsyncByocTrunksResourceWithStreamingResponse(client.byoc_trunks)
        self.connection_policies = connection_policies.AsyncConnectionPoliciesResourceWithStreamingResponse(
            client.connection_policies
        )
        self.dialing_permissions = dialing_permissions.AsyncDialingPermissionsResourceWithStreamingResponse(
            client.dialing_permissions
        )
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)
        self.ip_records = ip_records.AsyncIPRecordsResourceWithStreamingResponse(client.ip_records)
        self.source_ip_mappings = source_ip_mappings.AsyncSourceIPMappingsResourceWithStreamingResponse(
            client.source_ip_mappings
        )


Client = TwilioVoiceOpenAPI

AsyncClient = AsyncTwilioVoiceOpenAPI
