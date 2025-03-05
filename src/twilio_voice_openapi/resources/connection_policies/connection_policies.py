# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import (
    connection_policy_list_params,
    connection_policy_create_params,
    connection_policy_update_params,
)
from .targets import (
    TargetsResource,
    AsyncTargetsResource,
    TargetsResourceWithRawResponse,
    AsyncTargetsResourceWithRawResponse,
    TargetsResourceWithStreamingResponse,
    AsyncTargetsResourceWithStreamingResponse,
)
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
from ...types.connection_policy import ConnectionPolicy
from ...types.connection_policy_list_response import ConnectionPolicyListResponse

__all__ = ["ConnectionPoliciesResource", "AsyncConnectionPoliciesResource"]


class ConnectionPoliciesResource(SyncAPIResource):
    @cached_property
    def targets(self) -> TargetsResource:
        return TargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectionPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return ConnectionPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicy:
        """
        Args:
          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ConnectionPolicies",
            body=maybe_transform(
                {"friendly_name": friendly_name}, connection_policy_create_params.ConnectionPolicyCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicy:
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
            f"/v1/ConnectionPolicies/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicy:
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
            f"/v1/ConnectionPolicies/{sid}",
            body=maybe_transform(
                {"friendly_name": friendly_name}, connection_policy_update_params.ConnectionPolicyUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicyListResponse:
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
            "/v1/ConnectionPolicies",
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
                    connection_policy_list_params.ConnectionPolicyListParams,
                ),
            ),
            cast_to=ConnectionPolicyListResponse,
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
            f"/v1/ConnectionPolicies/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConnectionPoliciesResource(AsyncAPIResource):
    @cached_property
    def targets(self) -> AsyncTargetsResource:
        return AsyncTargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectionPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/twilio-voice-openapi-python#with_streaming_response
        """
        return AsyncConnectionPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        friendly_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionPolicy:
        """
        Args:
          friendly_name: A descriptive string that you create to describe the resource. It is not unique
              and can be up to 255 characters long.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ConnectionPolicies",
            body=await async_maybe_transform(
                {"friendly_name": friendly_name}, connection_policy_create_params.ConnectionPolicyCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicy:
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
            f"/v1/ConnectionPolicies/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicy:
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
            f"/v1/ConnectionPolicies/{sid}",
            body=await async_maybe_transform(
                {"friendly_name": friendly_name}, connection_policy_update_params.ConnectionPolicyUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionPolicy,
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
    ) -> ConnectionPolicyListResponse:
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
            "/v1/ConnectionPolicies",
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
                    connection_policy_list_params.ConnectionPolicyListParams,
                ),
            ),
            cast_to=ConnectionPolicyListResponse,
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
            f"/v1/ConnectionPolicies/{sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConnectionPoliciesResourceWithRawResponse:
    def __init__(self, connection_policies: ConnectionPoliciesResource) -> None:
        self._connection_policies = connection_policies

        self.create = to_raw_response_wrapper(
            connection_policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connection_policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connection_policies.update,
        )
        self.list = to_raw_response_wrapper(
            connection_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            connection_policies.delete,
        )

    @cached_property
    def targets(self) -> TargetsResourceWithRawResponse:
        return TargetsResourceWithRawResponse(self._connection_policies.targets)


class AsyncConnectionPoliciesResourceWithRawResponse:
    def __init__(self, connection_policies: AsyncConnectionPoliciesResource) -> None:
        self._connection_policies = connection_policies

        self.create = async_to_raw_response_wrapper(
            connection_policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connection_policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connection_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            connection_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connection_policies.delete,
        )

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithRawResponse:
        return AsyncTargetsResourceWithRawResponse(self._connection_policies.targets)


class ConnectionPoliciesResourceWithStreamingResponse:
    def __init__(self, connection_policies: ConnectionPoliciesResource) -> None:
        self._connection_policies = connection_policies

        self.create = to_streamed_response_wrapper(
            connection_policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connection_policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connection_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            connection_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            connection_policies.delete,
        )

    @cached_property
    def targets(self) -> TargetsResourceWithStreamingResponse:
        return TargetsResourceWithStreamingResponse(self._connection_policies.targets)


class AsyncConnectionPoliciesResourceWithStreamingResponse:
    def __init__(self, connection_policies: AsyncConnectionPoliciesResource) -> None:
        self._connection_policies = connection_policies

        self.create = async_to_streamed_response_wrapper(
            connection_policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connection_policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connection_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connection_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connection_policies.delete,
        )

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithStreamingResponse:
        return AsyncTargetsResourceWithStreamingResponse(self._connection_policies.targets)
