# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import dialing_permission_create_bulk_country_updates_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dialing_permission_create_bulk_country_updates_response import (
    DialingPermissionCreateBulkCountryUpdatesResponse,
)

__all__ = ["DialingPermissionsResource", "AsyncDialingPermissionsResource"]


class DialingPermissionsResource(SyncAPIResource):
    @cached_property
    def countries(self) -> CountriesResource:
        return CountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DialingPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return DialingPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DialingPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return DialingPermissionsResourceWithStreamingResponse(self)

    def create_bulk_country_updates(
        self,
        *,
        update_request: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialingPermissionCreateBulkCountryUpdatesResponse:
        """
        Create a bulk update request to change voice dialing country permissions of one
        or more countries identified by the corresponding
        [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Args:
          update_request:
              URL encoded JSON array of update objects. example :
              `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/DialingPermissions/BulkCountryUpdates",
            body=maybe_transform(
                {"update_request": update_request},
                dialing_permission_create_bulk_country_updates_params.DialingPermissionCreateBulkCountryUpdatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialingPermissionCreateBulkCountryUpdatesResponse,
        )


class AsyncDialingPermissionsResource(AsyncAPIResource):
    @cached_property
    def countries(self) -> AsyncCountriesResource:
        return AsyncCountriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDialingPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDialingPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDialingPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return AsyncDialingPermissionsResourceWithStreamingResponse(self)

    async def create_bulk_country_updates(
        self,
        *,
        update_request: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialingPermissionCreateBulkCountryUpdatesResponse:
        """
        Create a bulk update request to change voice dialing country permissions of one
        or more countries identified by the corresponding
        [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Args:
          update_request:
              URL encoded JSON array of update objects. example :
              `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/DialingPermissions/BulkCountryUpdates",
            body=await async_maybe_transform(
                {"update_request": update_request},
                dialing_permission_create_bulk_country_updates_params.DialingPermissionCreateBulkCountryUpdatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialingPermissionCreateBulkCountryUpdatesResponse,
        )


class DialingPermissionsResourceWithRawResponse:
    def __init__(self, dialing_permissions: DialingPermissionsResource) -> None:
        self._dialing_permissions = dialing_permissions

        self.create_bulk_country_updates = to_raw_response_wrapper(
            dialing_permissions.create_bulk_country_updates,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        return CountriesResourceWithRawResponse(self._dialing_permissions.countries)


class AsyncDialingPermissionsResourceWithRawResponse:
    def __init__(self, dialing_permissions: AsyncDialingPermissionsResource) -> None:
        self._dialing_permissions = dialing_permissions

        self.create_bulk_country_updates = async_to_raw_response_wrapper(
            dialing_permissions.create_bulk_country_updates,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        return AsyncCountriesResourceWithRawResponse(self._dialing_permissions.countries)


class DialingPermissionsResourceWithStreamingResponse:
    def __init__(self, dialing_permissions: DialingPermissionsResource) -> None:
        self._dialing_permissions = dialing_permissions

        self.create_bulk_country_updates = to_streamed_response_wrapper(
            dialing_permissions.create_bulk_country_updates,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        return CountriesResourceWithStreamingResponse(self._dialing_permissions.countries)


class AsyncDialingPermissionsResourceWithStreamingResponse:
    def __init__(self, dialing_permissions: AsyncDialingPermissionsResource) -> None:
        self._dialing_permissions = dialing_permissions

        self.create_bulk_country_updates = async_to_streamed_response_wrapper(
            dialing_permissions.create_bulk_country_updates,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        return AsyncCountriesResourceWithStreamingResponse(self._dialing_permissions.countries)
