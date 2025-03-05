# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types.connection_policies import (
    TargetListResponse,
    ConnectionPolicyTarget,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTargets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
            enabled=True,
            friendly_name="friendly_name",
            priority=1,
            weight=20,
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.targets.with_raw_response.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.targets.with_streaming_response.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            client.connection_policies.targets.with_raw_response.create(
                connection_policy_sid="",
                target="sip:sip-box.com:1234",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.targets.with_raw_response.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.targets.with_streaming_response.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            client.connection_policies.targets.with_raw_response.retrieve(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.targets.with_raw_response.retrieve(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            enabled=False,
            friendly_name="updated_name",
            priority=2,
            target="sip:sip-updated.com:4321",
            weight=10,
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.targets.with_raw_response.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.targets.with_streaming_response.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            client.connection_policies.targets.with_raw_response.update(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.targets.with_raw_response.update(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.targets.with_raw_response.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.targets.with_streaming_response.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetListResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            client.connection_policies.targets.with_raw_response.list(
                connection_policy_sid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: TwilioVoiceOpenAPI) -> None:
        target = client.connection_policies.targets.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert target is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.connection_policies.targets.with_raw_response.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert target is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with client.connection_policies.targets.with_streaming_response.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            client.connection_policies.targets.with_raw_response.delete(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.connection_policies.targets.with_raw_response.delete(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )


class TestAsyncTargets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
            enabled=True,
            friendly_name="friendly_name",
            priority=1,
            weight=20,
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.targets.with_raw_response.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.targets.with_streaming_response.create(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            target="sip:sip-box.com:1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.create(
                connection_policy_sid="",
                target="sip:sip-box.com:1234",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.targets.with_raw_response.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.targets.with_streaming_response.retrieve(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.retrieve(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.retrieve(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            enabled=False,
            friendly_name="updated_name",
            priority=2,
            target="sip:sip-updated.com:4321",
            weight=10,
        )
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.targets.with_raw_response.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.targets.with_streaming_response.update(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(ConnectionPolicyTarget, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.update(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.update(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.targets.with_raw_response.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetListResponse, target, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.targets.with_streaming_response.list(
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetListResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.list(
                connection_policy_sid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        target = await async_client.connection_policies.targets.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert target is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.connection_policies.targets.with_raw_response.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert target is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.connection_policies.targets.with_streaming_response.delete(
            sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_policy_sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.delete(
                sid="NEE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                connection_policy_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.connection_policies.targets.with_raw_response.delete(
                sid="",
                connection_policy_sid="NYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )
