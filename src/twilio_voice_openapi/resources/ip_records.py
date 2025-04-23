# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ip_record_list_params, ip_record_create_params, ip_record_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ip_record import IPRecord
from ..types.ip_record_list_response import IPRecordListResponse

__all__ = ["IPRecordsResource", "AsyncIPRecordsResource"]


class IPRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return IPRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return IPRecordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: int | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRecord:
        """
        Args:
          ip_address: An IP address in dotted decimal notation, IPv4 only.

          cidr_prefix_length: An integer representing the length of the
              [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address.
              By default the entire IP address is used, which for IPv4 is value 32.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/IpRecords",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "cidr_prefix_length": cidr_prefix_length,
                    "friendly_name": friendly_name,
                },
                ip_record_create_params.IPRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
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
    ) -> IPRecord:
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
            f"/v1/IpRecords/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
        )

    def update(
        self,
        sid: str,
        *,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRecord:
        """
        Args:
          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._post(
            f"/v1/IpRecords/{sid}",
            body=maybe_transform({"friendly_name": friendly_name}, ip_record_update_params.IPRecordUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
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
    ) -> IPRecordListResponse:
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
            "/v1/IpRecords",
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
                    ip_record_list_params.IPRecordListParams,
                ),
            ),
            cast_to=IPRecordListResponse,
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
            f"/v1/IpRecords/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncIPRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return AsyncIPRecordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ip_address: str,
        cidr_prefix_length: int | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRecord:
        """
        Args:
          ip_address: An IP address in dotted decimal notation, IPv4 only.

          cidr_prefix_length: An integer representing the length of the
              [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address.
              By default the entire IP address is used, which for IPv4 is value 32.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/IpRecords",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "cidr_prefix_length": cidr_prefix_length,
                    "friendly_name": friendly_name,
                },
                ip_record_create_params.IPRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
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
    ) -> IPRecord:
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
            f"/v1/IpRecords/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
        )

    async def update(
        self,
        sid: str,
        *,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRecord:
        """
        Args:
          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._post(
            f"/v1/IpRecords/{sid}",
            body=await async_maybe_transform(
                {"friendly_name": friendly_name}, ip_record_update_params.IPRecordUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRecord,
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
    ) -> IPRecordListResponse:
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
            "/v1/IpRecords",
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
                    ip_record_list_params.IPRecordListParams,
                ),
            ),
            cast_to=IPRecordListResponse,
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
            f"/v1/IpRecords/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class IPRecordsResourceWithRawResponse:
    def __init__(self, ip_records: IPRecordsResource) -> None:
        self._ip_records = ip_records

        self.create = to_raw_response_wrapper(
            ip_records.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ip_records.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ip_records.update,
        )
        self.list = to_raw_response_wrapper(
            ip_records.list,
        )
        self.delete = to_raw_response_wrapper(
            ip_records.delete,
        )


class AsyncIPRecordsResourceWithRawResponse:
    def __init__(self, ip_records: AsyncIPRecordsResource) -> None:
        self._ip_records = ip_records

        self.create = async_to_raw_response_wrapper(
            ip_records.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ip_records.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ip_records.update,
        )
        self.list = async_to_raw_response_wrapper(
            ip_records.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ip_records.delete,
        )


class IPRecordsResourceWithStreamingResponse:
    def __init__(self, ip_records: IPRecordsResource) -> None:
        self._ip_records = ip_records

        self.create = to_streamed_response_wrapper(
            ip_records.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ip_records.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ip_records.update,
        )
        self.list = to_streamed_response_wrapper(
            ip_records.list,
        )
        self.delete = to_streamed_response_wrapper(
            ip_records.delete,
        )


class AsyncIPRecordsResourceWithStreamingResponse:
    def __init__(self, ip_records: AsyncIPRecordsResource) -> None:
        self._ip_records = ip_records

        self.create = async_to_streamed_response_wrapper(
            ip_records.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ip_records.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ip_records.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ip_records.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ip_records.delete,
        )
