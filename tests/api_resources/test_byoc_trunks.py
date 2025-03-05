# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types import (
    ByocTrunk,
    ByocTrunkListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByocTrunks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.create()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.create(
            cnam_lookup_enabled=False,
            connection_policy_sid="NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            friendly_name="friendly_name",
            from_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            status_callback_method="GET",
            status_callback_url="https://byoc.example.com/twilio/status_callback",
            voice_fallback_method="GET",
            voice_fallback_url="https://byoc.example.com/twilio/fallback",
            voice_method="GET",
            voice_url="https://byoc.example.com/twilio/app",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.byoc_trunks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        with client.byoc_trunks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.byoc_trunks.with_raw_response.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.byoc_trunks.with_streaming_response.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.byoc_trunks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            cnam_lookup_enabled=True,
            connection_policy_sid="NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            friendly_name="update_name",
            from_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            status_callback_method="GET",
            status_callback_url="https://byoc.example.com/twilio_updated/status_callback",
            voice_fallback_method="GET",
            voice_fallback_url="https://byoc.example.com/twilio_updated/fallback",
            voice_method="GET",
            voice_url="https://byoc.example.com/twilio_updated/app",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.byoc_trunks.with_raw_response.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        with client.byoc_trunks.with_streaming_response.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.byoc_trunks.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.list()
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.byoc_trunks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = response.parse()
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.byoc_trunks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = response.parse()
            assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: TwilioVoiceOpenAPI) -> None:
        byoc_trunk = client.byoc_trunks.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert byoc_trunk is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.byoc_trunks.with_raw_response.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = response.parse()
        assert byoc_trunk is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with client.byoc_trunks.with_streaming_response.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = response.parse()
            assert byoc_trunk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.byoc_trunks.with_raw_response.delete(
                "",
            )


class TestAsyncByocTrunks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.create()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.create(
            cnam_lookup_enabled=False,
            connection_policy_sid="NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            friendly_name="friendly_name",
            from_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            status_callback_method="GET",
            status_callback_url="https://byoc.example.com/twilio/status_callback",
            voice_fallback_method="GET",
            voice_fallback_url="https://byoc.example.com/twilio/fallback",
            voice_method="GET",
            voice_url="https://byoc.example.com/twilio/app",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.byoc_trunks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = await response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.byoc_trunks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = await response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.byoc_trunks.with_raw_response.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = await response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.byoc_trunks.with_streaming_response.retrieve(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = await response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.byoc_trunks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            cnam_lookup_enabled=True,
            connection_policy_sid="NYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            friendly_name="update_name",
            from_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            status_callback_method="GET",
            status_callback_url="https://byoc.example.com/twilio_updated/status_callback",
            voice_fallback_method="GET",
            voice_fallback_url="https://byoc.example.com/twilio_updated/fallback",
            voice_method="GET",
            voice_url="https://byoc.example.com/twilio_updated/app",
        )
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.byoc_trunks.with_raw_response.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = await response.parse()
        assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.byoc_trunks.with_streaming_response.update(
            sid="BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = await response.parse()
            assert_matches_type(ByocTrunk, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.byoc_trunks.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.list()
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.byoc_trunks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = await response.parse()
        assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.byoc_trunks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = await response.parse()
            assert_matches_type(ByocTrunkListResponse, byoc_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        byoc_trunk = await async_client.byoc_trunks.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert byoc_trunk is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.byoc_trunks.with_raw_response.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        byoc_trunk = await response.parse()
        assert byoc_trunk is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.byoc_trunks.with_streaming_response.delete(
            "BYE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            byoc_trunk = await response.parse()
            assert byoc_trunk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.byoc_trunks.with_raw_response.delete(
                "",
            )
