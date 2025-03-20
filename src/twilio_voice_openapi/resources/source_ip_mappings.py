# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    source_ip_mapping_list_params,
    source_ip_mapping_create_params,
    source_ip_mapping_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.source_ip_mapping import SourceIPMapping
from ..types.source_ip_mapping_list_response import SourceIPMappingListResponse

__all__ = ["SourceIPMappingsResource", "AsyncSourceIPMappingsResource"]


class SourceIPMappingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceIPMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return SourceIPMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceIPMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return SourceIPMappingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ip_record_sid: str,
        sip_domain_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to
              map from.

          sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/SourceIpMappings",
            body=maybe_transform(
                {
                    "ip_record_sid": ip_record_sid,
                    "sip_domain_sid": sip_domain_sid,
                },
                source_ip_mapping_create_params.SourceIPMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    def retrieve(
        self,
        sid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._get(
            f"/v1/SourceIpMappings/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    def update(
        self,
        sid: str,
        *,
        sip_domain_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._post(
            f"/v1/SourceIpMappings/{sid}",
            body=maybe_transform(
                {"sip_domain_sid": sip_domain_sid}, source_ip_mapping_update_params.SourceIPMappingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    def list(
        self,
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
    ) -> SourceIPMappingListResponse:
        """Args:
          page: The page index.

        This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/SourceIpMappings",
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
                    source_ip_mapping_list_params.SourceIPMappingListParams,
                ),
            ),
            cast_to=SourceIPMappingListResponse,
        )

    def delete(
        self,
        sid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/SourceIpMappings/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSourceIPMappingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceIPMappingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourceIPMappingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceIPMappingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return AsyncSourceIPMappingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ip_record_sid: str,
        sip_domain_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to
              map from.

          sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/SourceIpMappings",
            body=await async_maybe_transform(
                {
                    "ip_record_sid": ip_record_sid,
                    "sip_domain_sid": sip_domain_sid,
                },
                source_ip_mapping_create_params.SourceIPMappingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    async def retrieve(
        self,
        sid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._get(
            f"/v1/SourceIpMappings/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    async def update(
        self,
        sid: str,
        *,
        sip_domain_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SourceIPMapping:
        """
        Args:
          sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._post(
            f"/v1/SourceIpMappings/{sid}",
            body=await async_maybe_transform(
                {"sip_domain_sid": sip_domain_sid}, source_ip_mapping_update_params.SourceIPMappingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceIPMapping,
        )

    async def list(
        self,
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
    ) -> SourceIPMappingListResponse:
        """Args:
          page: The page index.

        This value is simply for client state.

          page_size: How many resources to return in each list page. The default is 50, and the
              maximum is 1000.

          page_token: The page token. This is provided by the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/SourceIpMappings",
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
                    source_ip_mapping_list_params.SourceIPMappingListParams,
                ),
            ),
            cast_to=SourceIPMappingListResponse,
        )

    async def delete(
        self,
        sid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/SourceIpMappings/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SourceIPMappingsResourceWithRawResponse:
    def __init__(self, source_ip_mappings: SourceIPMappingsResource) -> None:
        self._source_ip_mappings = source_ip_mappings

        self.create = to_raw_response_wrapper(
            source_ip_mappings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            source_ip_mappings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            source_ip_mappings.update,
        )
        self.list = to_raw_response_wrapper(
            source_ip_mappings.list,
        )
        self.delete = to_raw_response_wrapper(
            source_ip_mappings.delete,
        )


class AsyncSourceIPMappingsResourceWithRawResponse:
    def __init__(self, source_ip_mappings: AsyncSourceIPMappingsResource) -> None:
        self._source_ip_mappings = source_ip_mappings

        self.create = async_to_raw_response_wrapper(
            source_ip_mappings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            source_ip_mappings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            source_ip_mappings.update,
        )
        self.list = async_to_raw_response_wrapper(
            source_ip_mappings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            source_ip_mappings.delete,
        )


class SourceIPMappingsResourceWithStreamingResponse:
    def __init__(self, source_ip_mappings: SourceIPMappingsResource) -> None:
        self._source_ip_mappings = source_ip_mappings

        self.create = to_streamed_response_wrapper(
            source_ip_mappings.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            source_ip_mappings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            source_ip_mappings.update,
        )
        self.list = to_streamed_response_wrapper(
            source_ip_mappings.list,
        )
        self.delete = to_streamed_response_wrapper(
            source_ip_mappings.delete,
        )


class AsyncSourceIPMappingsResourceWithStreamingResponse:
    def __init__(self, source_ip_mappings: AsyncSourceIPMappingsResource) -> None:
        self._source_ip_mappings = source_ip_mappings

        self.create = async_to_streamed_response_wrapper(
            source_ip_mappings.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            source_ip_mappings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            source_ip_mappings.update,
        )
        self.list = async_to_streamed_response_wrapper(
            source_ip_mappings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            source_ip_mappings.delete,
        )
