# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dialing_permissions import country_list_params, country_fetch_high_risk_special_prefixes_params
from ...types.dialing_permissions.country_list_response import CountryListResponse
from ...types.dialing_permissions.country_retrieve_response import CountryRetrieveResponse
from ...types.dialing_permissions.country_fetch_high_risk_special_prefixes_response import (
    CountryFetchHighRiskSpecialPrefixesResponse,
)

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        iso_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryRetrieveResponse:
        """
        Retrieve voice dialing country permissions identified by the given ISO country
        code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not iso_code:
            raise ValueError(f"Expected a non-empty value for `iso_code` but received {iso_code!r}")
        return self._get(
            f"/v1/DialingPermissions/Countries/{iso_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryRetrieveResponse,
        )

    def list(
        self,
        *,
        continent: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        high_risk_special_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        high_risk_tollfraud_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        iso_code: str | NotGiven = NOT_GIVEN,
        low_risk_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Retrieve all voice dialing country permissions for this account

        Args:
          continent: Filter to retrieve the country permissions by specifying the continent

          country_code: Filter the results by specified
              [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)

          high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special
              service numbers enabled. Can be: `true` or `false`

          high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk
              [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html)
              numbers enabled. Can be: `true` or `false`.

          iso_code: Filter to retrieve the country permissions by specifying the
              [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers
              enabled. Can be: `true` or `false`.

          page: The page index. This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/DialingPermissions/Countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continent": continent,
                        "country_code": country_code,
                        "high_risk_special_numbers_enabled": high_risk_special_numbers_enabled,
                        "high_risk_tollfraud_numbers_enabled": high_risk_tollfraud_numbers_enabled,
                        "iso_code": iso_code,
                        "low_risk_numbers_enabled": low_risk_numbers_enabled,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )

    def fetch_high_risk_special_prefixes(
        self,
        iso_code: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryFetchHighRiskSpecialPrefixesResponse:
        """
        Fetch the high-risk special services prefixes from the country resource
        corresponding to the
        [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Args:
          page: The page index. This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not iso_code:
            raise ValueError(f"Expected a non-empty value for `iso_code` but received {iso_code!r}")
        return self._get(
            f"/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    country_fetch_high_risk_special_prefixes_params.CountryFetchHighRiskSpecialPrefixesParams,
                ),
            ),
            cast_to=CountryFetchHighRiskSpecialPrefixesResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        iso_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryRetrieveResponse:
        """
        Retrieve voice dialing country permissions identified by the given ISO country
        code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not iso_code:
            raise ValueError(f"Expected a non-empty value for `iso_code` but received {iso_code!r}")
        return await self._get(
            f"/v1/DialingPermissions/Countries/{iso_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryRetrieveResponse,
        )

    async def list(
        self,
        *,
        continent: str | NotGiven = NOT_GIVEN,
        country_code: str | NotGiven = NOT_GIVEN,
        high_risk_special_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        high_risk_tollfraud_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        iso_code: str | NotGiven = NOT_GIVEN,
        low_risk_numbers_enabled: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Retrieve all voice dialing country permissions for this account

        Args:
          continent: Filter to retrieve the country permissions by specifying the continent

          country_code: Filter the results by specified
              [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)

          high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special
              service numbers enabled. Can be: `true` or `false`

          high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk
              [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html)
              numbers enabled. Can be: `true` or `false`.

          iso_code: Filter to retrieve the country permissions by specifying the
              [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers
              enabled. Can be: `true` or `false`.

          page: The page index. This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/DialingPermissions/Countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continent": continent,
                        "country_code": country_code,
                        "high_risk_special_numbers_enabled": high_risk_special_numbers_enabled,
                        "high_risk_tollfraud_numbers_enabled": high_risk_tollfraud_numbers_enabled,
                        "iso_code": iso_code,
                        "low_risk_numbers_enabled": low_risk_numbers_enabled,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )

    async def fetch_high_risk_special_prefixes(
        self,
        iso_code: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryFetchHighRiskSpecialPrefixesResponse:
        """
        Fetch the high-risk special services prefixes from the country resource
        corresponding to the
        [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

        Args:
          page: The page index. This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not iso_code:
            raise ValueError(f"Expected a non-empty value for `iso_code` but received {iso_code!r}")
        return await self._get(
            f"/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    country_fetch_high_risk_special_prefixes_params.CountryFetchHighRiskSpecialPrefixesParams,
                ),
            ),
            cast_to=CountryFetchHighRiskSpecialPrefixesResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.retrieve = to_raw_response_wrapper(
            countries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            countries.list,
        )
        self.fetch_high_risk_special_prefixes = to_raw_response_wrapper(
            countries.fetch_high_risk_special_prefixes,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.retrieve = async_to_raw_response_wrapper(
            countries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            countries.list,
        )
        self.fetch_high_risk_special_prefixes = async_to_raw_response_wrapper(
            countries.fetch_high_risk_special_prefixes,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.retrieve = to_streamed_response_wrapper(
            countries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            countries.list,
        )
        self.fetch_high_risk_special_prefixes = to_streamed_response_wrapper(
            countries.fetch_high_risk_special_prefixes,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.retrieve = async_to_streamed_response_wrapper(
            countries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            countries.list,
        )
        self.fetch_high_risk_special_prefixes = async_to_streamed_response_wrapper(
            countries.fetch_high_risk_special_prefixes,
        )
