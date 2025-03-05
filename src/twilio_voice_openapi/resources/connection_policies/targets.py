# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.connection_policies import target_list_params, target_create_params, target_update_params
from ...types.connection_policies.target_list_response import TargetListResponse
from ...types.connection_policies.connection_policy_target import ConnectionPolicyTarget

__all__ = ["TargetsResource", "AsyncTargetsResource"]


class TargetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return TargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return TargetsResourceWithStreamingResponse(self)

    def create(
        self,
        connection_policy_sid: str,
        *,
        target: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """Args:
          target: The SIP address you want Twilio to route your calls to.

        This must be a `sip:`
              schema. `sips` is NOT supported.

          enabled: Whether the Target is enabled. The default is `true`.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          priority: The relative importance of the target. Can be an integer from 0 to 65535,
              inclusive, and the default is 10. The lowest number represents the most
              important target.

          weight: The value that determines the relative share of the load the Target should
              receive compared to other Targets with the same priority. Can be an integer from
              1 to 65535, inclusive, and the default is 10. Targets with higher values receive
              more load than those with lower ones with the same priority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        return self._post(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets",
            body=maybe_transform(
                {
                    "target": target,
                    "enabled": enabled,
                    "friendly_name": friendly_name,
                    "priority": priority,
                    "weight": weight,
                },
                target_create_params.TargetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    def retrieve(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._get(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    def update(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        target: str | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """
        Args:
          enabled: Whether the Target is enabled.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          priority: The relative importance of the target. Can be an integer from 0 to 65535,
              inclusive. The lowest number represents the most important target.

          target: The SIP address you want Twilio to route your calls to. This must be a `sip:`
              schema. `sips` is NOT supported.

          weight: The value that determines the relative share of the load the Target should
              receive compared to other Targets with the same priority. Can be an integer from
              1 to 65535, inclusive. Targets with higher values receive more load than those
              with lower ones with the same priority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return self._post(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "friendly_name": friendly_name,
                    "priority": priority,
                    "target": target,
                    "weight": weight,
                },
                target_update_params.TargetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    def list(
        self,
        connection_policy_sid: str,
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
    ) -> TargetListResponse:
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
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        return self._get(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets",
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
                    target_list_params.TargetListParams,
                ),
            ),
            cast_to=TargetListResponse,
        )

    def delete(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
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
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTargetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return AsyncTargetsResourceWithStreamingResponse(self)

    async def create(
        self,
        connection_policy_sid: str,
        *,
        target: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """Args:
          target: The SIP address you want Twilio to route your calls to.

        This must be a `sip:`
              schema. `sips` is NOT supported.

          enabled: Whether the Target is enabled. The default is `true`.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          priority: The relative importance of the target. Can be an integer from 0 to 65535,
              inclusive, and the default is 10. The lowest number represents the most
              important target.

          weight: The value that determines the relative share of the load the Target should
              receive compared to other Targets with the same priority. Can be an integer from
              1 to 65535, inclusive, and the default is 10. Targets with higher values receive
              more load than those with lower ones with the same priority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        return await self._post(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets",
            body=await async_maybe_transform(
                {
                    "target": target,
                    "enabled": enabled,
                    "friendly_name": friendly_name,
                    "priority": priority,
                    "weight": weight,
                },
                target_create_params.TargetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    async def retrieve(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._get(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    async def update(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        target: str | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicyTarget:
        """
        Args:
          enabled: Whether the Target is enabled.

          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          priority: The relative importance of the target. Can be an integer from 0 to 65535,
              inclusive. The lowest number represents the most important target.

          target: The SIP address you want Twilio to route your calls to. This must be a `sip:`
              schema. `sips` is NOT supported.

          weight: The value that determines the relative share of the load the Target should
              receive compared to other Targets with the same priority. Can be an integer from
              1 to 65535, inclusive. Targets with higher values receive more load than those
              with lower ones with the same priority.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        return await self._post(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "friendly_name": friendly_name,
                    "priority": priority,
                    "target": target,
                    "weight": weight,
                },
                target_update_params.TargetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicyTarget,
        )

    async def list(
        self,
        connection_policy_sid: str,
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
    ) -> TargetListResponse:
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
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        return await self._get(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets",
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
                    target_list_params.TargetListParams,
                ),
            ),
            cast_to=TargetListResponse,
        )

    async def delete(
        self,
        sid: str,
        *,
        connection_policy_sid: str,
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
        if not connection_policy_sid:
            raise ValueError(
                f"Expected a non-empty value for `connection_policy_sid` but received {connection_policy_sid!r}"
            )
        if not sid:
            raise ValueError(f"Expected a non-empty value for `sid` but received {sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TargetsResourceWithRawResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_raw_response_wrapper(
            targets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            targets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            targets.update,
        )
        self.list = to_raw_response_wrapper(
            targets.list,
        )
        self.delete = to_raw_response_wrapper(
            targets.delete,
        )


class AsyncTargetsResourceWithRawResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_raw_response_wrapper(
            targets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            targets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            targets.update,
        )
        self.list = async_to_raw_response_wrapper(
            targets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            targets.delete,
        )


class TargetsResourceWithStreamingResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_streamed_response_wrapper(
            targets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            targets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            targets.update,
        )
        self.list = to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = to_streamed_response_wrapper(
            targets.delete,
        )


class AsyncTargetsResourceWithStreamingResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_streamed_response_wrapper(
            targets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            targets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            targets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            targets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            targets.delete,
        )
