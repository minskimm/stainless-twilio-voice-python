# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ArchivesResource", "AsyncArchivesResource"]


class ArchivesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return ArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return ArchivesResourceWithStreamingResponse(self)

    def delete_call(
        self,
        sid: str,
        *,
        date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an archived call record from Bulk Export.

        Note: this does not also delete
        the record from the Voice API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/Archives/{date}/Calls/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/Archives/{date}/Calls/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncArchivesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return AsyncArchivesResourceWithStreamingResponse(self)

    async def delete_call(
        self,
        sid: str,
        *,
        date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an archived call record from Bulk Export.

        Note: this does not also delete
        the record from the Voice API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/Archives/{date}/Calls/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/Archives/{date}/Calls/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ArchivesResourceWithRawResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.delete_call = to_raw_response_wrapper(
            archives.delete_call,
        )


class AsyncArchivesResourceWithRawResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.delete_call = async_to_raw_response_wrapper(
            archives.delete_call,
        )


class ArchivesResourceWithStreamingResponse:
    def __init__(self, archives: ArchivesResource) -> None:
        self._archives = archives

        self.delete_call = to_streamed_response_wrapper(
            archives.delete_call,
        )


class AsyncArchivesResourceWithStreamingResponse:
    def __init__(self, archives: AsyncArchivesResource) -> None:
        self._archives = archives

        self.delete_call = async_to_streamed_response_wrapper(
            archives.delete_call,
        )
