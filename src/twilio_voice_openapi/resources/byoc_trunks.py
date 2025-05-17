# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import byoc_trunk_list_params, byoc_trunk_create_params, byoc_trunk_update_params
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
from ..types.byoc_trunk import ByocTrunk
from ..types.byoc_trunk_list_response import ByocTrunkListResponse

__all__ = ["ByocTrunksResource", "AsyncByocTrunksResource"]


class ByocTrunksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByocTrunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return ByocTrunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByocTrunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return ByocTrunksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cnam_lookup_enabled: bool | NotGiven = NOT_GIVEN,
        connection_policy_sid: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        from_domain_sid: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status_callback_url: str | NotGiven = NOT_GIVEN,
        voice_fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByocTrunk:
        """
        Args:
          cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all
              inbound calls to the BYOC Trunk from the United States and Canada automatically
              perform a CNAM Lookup and display Caller ID data on your phone. See
              [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more
              information.

          connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to
              your communications infrastructure.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of
              originating calls sent to your SIP infrastructure. If your SIP infrastructure
              allows users to "call back" an incoming call, configure this with a
              [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
              routing. If not configured, the from domain will default to "sip.twilio.com".

          status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or
              `POST`.

          status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
              your application.

          voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or
              `POST`.

          voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing
              the TwiML from `voice_url`.

          voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

          voice_url: The URL we should call when the BYOC Trunk receives a call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ByocTrunks" if self._client._base_url_overridden else "https://voice.twilio.com/v1/ByocTrunks",
            body=maybe_transform(
                {
                    "cnam_lookup_enabled": cnam_lookup_enabled,
                    "connection_policy_sid": connection_policy_sid,
                    "friendly_name": friendly_name,
                    "from_domain_sid": from_domain_sid,
                    "status_callback_method": status_callback_method,
                    "status_callback_url": status_callback_url,
                    "voice_fallback_method": voice_fallback_method,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                    "voice_url": voice_url,
                },
                byoc_trunk_create_params.ByocTrunkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
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
    ) -> ByocTrunk:
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
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
        )

    def update(
        self,
        sid: str,
        *,
        cnam_lookup_enabled: bool | NotGiven = NOT_GIVEN,
        connection_policy_sid: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        from_domain_sid: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status_callback_url: str | NotGiven = NOT_GIVEN,
        voice_fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByocTrunk:
        """
        Args:
          cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all
              inbound calls to the BYOC Trunk from the United States and Canada automatically
              perform a CNAM Lookup and display Caller ID data on your phone. See
              [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more
              information.

          connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to
              your communications infrastructure.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of
              originating calls sent to your SIP infrastructure. If your SIP infrastructure
              allows users to "call back" an incoming call, configure this with a
              [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
              routing. If not configured, the from domain will default to "sip.twilio.com".

          status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or
              `POST`.

          status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
              your application.

          voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or
              `POST`.

          voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing
              the TwiML requested by `voice_url`.

          voice_method: The HTTP method we should use to call `voice_url`

          voice_url: The URL we should call when the BYOC Trunk receives a call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._post(
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            body=maybe_transform(
                {
                    "cnam_lookup_enabled": cnam_lookup_enabled,
                    "connection_policy_sid": connection_policy_sid,
                    "friendly_name": friendly_name,
                    "from_domain_sid": from_domain_sid,
                    "status_callback_method": status_callback_method,
                    "status_callback_url": status_callback_url,
                    "voice_fallback_method": voice_fallback_method,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                    "voice_url": voice_url,
                },
                byoc_trunk_update_params.ByocTrunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
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
    ) -> ByocTrunkListResponse:
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
            "/v1/ByocTrunks" if self._client._base_url_overridden else "https://voice.twilio.com/v1/ByocTrunks",
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
                    byoc_trunk_list_params.ByocTrunkListParams,
                ),
            ),
            cast_to=ByocTrunkListResponse,
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
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncByocTrunksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByocTrunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#accessing-raw-response-data-eg-headers
        """
        return AsyncByocTrunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByocTrunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/minskimm/stainless-twilio-voice-python#with_streaming_response
        """
        return AsyncByocTrunksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cnam_lookup_enabled: bool | NotGiven = NOT_GIVEN,
        connection_policy_sid: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        from_domain_sid: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status_callback_url: str | NotGiven = NOT_GIVEN,
        voice_fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByocTrunk:
        """
        Args:
          cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all
              inbound calls to the BYOC Trunk from the United States and Canada automatically
              perform a CNAM Lookup and display Caller ID data on your phone. See
              [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more
              information.

          connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to
              your communications infrastructure.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of
              originating calls sent to your SIP infrastructure. If your SIP infrastructure
              allows users to "call back" an incoming call, configure this with a
              [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
              routing. If not configured, the from domain will default to "sip.twilio.com".

          status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or
              `POST`.

          status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
              your application.

          voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or
              `POST`.

          voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing
              the TwiML from `voice_url`.

          voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

          voice_url: The URL we should call when the BYOC Trunk receives a call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ByocTrunks" if self._client._base_url_overridden else "https://voice.twilio.com/v1/ByocTrunks",
            body=await async_maybe_transform(
                {
                    "cnam_lookup_enabled": cnam_lookup_enabled,
                    "connection_policy_sid": connection_policy_sid,
                    "friendly_name": friendly_name,
                    "from_domain_sid": from_domain_sid,
                    "status_callback_method": status_callback_method,
                    "status_callback_url": status_callback_url,
                    "voice_fallback_method": voice_fallback_method,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                    "voice_url": voice_url,
                },
                byoc_trunk_create_params.ByocTrunkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
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
    ) -> ByocTrunk:
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
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
        )

    async def update(
        self,
        sid: str,
        *,
        cnam_lookup_enabled: bool | NotGiven = NOT_GIVEN,
        connection_policy_sid: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        from_domain_sid: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status_callback_url: str | NotGiven = NOT_GIVEN,
        voice_fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_fallback_url: str | NotGiven = NOT_GIVEN,
        voice_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        voice_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByocTrunk:
        """
        Args:
          cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all
              inbound calls to the BYOC Trunk from the United States and Canada automatically
              perform a CNAM Lookup and display Caller ID data on your phone. See
              [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more
              information.

          connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to
              your communications infrastructure.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of
              originating calls sent to your SIP infrastructure. If your SIP infrastructure
              allows users to "call back" an incoming call, configure this with a
              [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
              routing. If not configured, the from domain will default to "sip.twilio.com".

          status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or
              `POST`.

          status_callback_url: The URL that we should call to pass status parameters (such as call ended) to
              your application.

          voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or
              `POST`.

          voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing
              the TwiML requested by `voice_url`.

          voice_method: The HTTP method we should use to call `voice_url`

          voice_url: The URL we should call when the BYOC Trunk receives a call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._post(
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            body=await async_maybe_transform(
                {
                    "cnam_lookup_enabled": cnam_lookup_enabled,
                    "connection_policy_sid": connection_policy_sid,
                    "friendly_name": friendly_name,
                    "from_domain_sid": from_domain_sid,
                    "status_callback_method": status_callback_method,
                    "status_callback_url": status_callback_url,
                    "voice_fallback_method": voice_fallback_method,
                    "voice_fallback_url": voice_fallback_url,
                    "voice_method": voice_method,
                    "voice_url": voice_url,
                },
                byoc_trunk_update_params.ByocTrunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByocTrunk,
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
    ) -> ByocTrunkListResponse:
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
            "/v1/ByocTrunks" if self._client._base_url_overridden else "https://voice.twilio.com/v1/ByocTrunks",
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
                    byoc_trunk_list_params.ByocTrunkListParams,
                ),
            ),
            cast_to=ByocTrunkListResponse,
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
            f"/v1/ByocTrunks/{sid}"
            if self._client._base_url_overridden
            else f"https://voice.twilio.com/v1/ByocTrunks/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ByocTrunksResourceWithRawResponse:
    def __init__(self, byoc_trunks: ByocTrunksResource) -> None:
        self._byoc_trunks = byoc_trunks

        self.create = to_raw_response_wrapper(
            byoc_trunks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            byoc_trunks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            byoc_trunks.update,
        )
        self.list = to_raw_response_wrapper(
            byoc_trunks.list,
        )
        self.delete = to_raw_response_wrapper(
            byoc_trunks.delete,
        )


class AsyncByocTrunksResourceWithRawResponse:
    def __init__(self, byoc_trunks: AsyncByocTrunksResource) -> None:
        self._byoc_trunks = byoc_trunks

        self.create = async_to_raw_response_wrapper(
            byoc_trunks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            byoc_trunks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            byoc_trunks.update,
        )
        self.list = async_to_raw_response_wrapper(
            byoc_trunks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            byoc_trunks.delete,
        )


class ByocTrunksResourceWithStreamingResponse:
    def __init__(self, byoc_trunks: ByocTrunksResource) -> None:
        self._byoc_trunks = byoc_trunks

        self.create = to_streamed_response_wrapper(
            byoc_trunks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            byoc_trunks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            byoc_trunks.update,
        )
        self.list = to_streamed_response_wrapper(
            byoc_trunks.list,
        )
        self.delete = to_streamed_response_wrapper(
            byoc_trunks.delete,
        )


class AsyncByocTrunksResourceWithStreamingResponse:
    def __init__(self, byoc_trunks: AsyncByocTrunksResource) -> None:
        self._byoc_trunks = byoc_trunks

        self.create = async_to_streamed_response_wrapper(
            byoc_trunks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            byoc_trunks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            byoc_trunks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            byoc_trunks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            byoc_trunks.delete,
        )
