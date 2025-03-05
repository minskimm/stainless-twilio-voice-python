# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types import (
    ConnectionPolicy,
    ConnectionPolicyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectionPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.create()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.create(
            friendly_name="friendly_name",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.with_raw_response.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.with_streaming_response.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            friendly_name="updated_name",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.with_raw_response.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.with_streaming_response.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.list()
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = response.parse()
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = response.parse()
            assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: TwilioVoiceOpenAPI) -> None:
        connection_policy = client.connection_policies.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert connection_policy is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.with_raw_response.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = response.parse()
        assert connection_policy is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.with_streaming_response.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = response.parse()
            assert connection_policy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.with_raw_response.delete(
                "",
            )


class TestAsyncConnectionPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.create()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.create(
            friendly_name="friendly_name",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = await response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = await response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.with_raw_response.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = await response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.with_streaming_response.retrieve(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = await response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            friendly_name="updated_name",
        )
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.with_raw_response.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = await response.parse()
        assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.with_streaming_response.update(
            sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = await response.parse()
            assert_matches_type(ConnectionPolicy, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.list()
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = await response.parse()
        assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = await response.parse()
            assert_matches_type(ConnectionPolicyListResponse, connection_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        connection_policy = await async_client.connection_policies.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert connection_policy is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.with_raw_response.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_policy = await response.parse()
        assert connection_policy is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.with_streaming_response.delete(
            "NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_policy = await response.parse()
            assert connection_policy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.with_raw_response.delete(
                "",
            )
