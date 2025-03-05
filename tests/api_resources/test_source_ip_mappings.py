# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types import (
    SourceIPMapping,
    SourceIPMappingListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSourceIPMappings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.source_ip_mappings.with_raw_response.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        with client.source_ip_mappings.with_streaming_response.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.source_ip_mappings.with_raw_response.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.source_ip_mappings.with_streaming_response.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.source_ip_mappings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.source_ip_mappings.with_raw_response.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        with client.source_ip_mappings.with_streaming_response.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.source_ip_mappings.with_raw_response.update(
                sid="",
                sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.list()
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.source_ip_mappings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = response.parse()
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.source_ip_mappings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = response.parse()
            assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: TwilioVoiceOpenAPI) -> None:
        source_ip_mapping = client.source_ip_mappings.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert source_ip_mapping is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.source_ip_mappings.with_raw_response.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = response.parse()
        assert source_ip_mapping is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with client.source_ip_mappings.with_streaming_response.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = response.parse()
            assert source_ip_mapping is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.source_ip_mappings.with_raw_response.delete(
                "",
            )


class TestAsyncSourceIPMappings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.source_ip_mappings.with_raw_response.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = await response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.source_ip_mappings.with_streaming_response.create(
            ip_record_sid="ILaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = await response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.source_ip_mappings.with_raw_response.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = await response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.source_ip_mappings.with_streaming_response.retrieve(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = await response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.source_ip_mappings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        )
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.source_ip_mappings.with_raw_response.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = await response.parse()
        assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.source_ip_mappings.with_streaming_response.update(
            sid="IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = await response.parse()
            assert_matches_type(SourceIPMapping, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.source_ip_mappings.with_raw_response.update(
                sid="",
                sip_domain_sid="SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.list()
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.source_ip_mappings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = await response.parse()
        assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.source_ip_mappings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = await response.parse()
            assert_matches_type(SourceIPMappingListResponse, source_ip_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        source_ip_mapping = await async_client.source_ip_mappings.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert source_ip_mapping is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.source_ip_mappings.with_raw_response.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_ip_mapping = await response.parse()
        assert source_ip_mapping is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.source_ip_mappings.with_streaming_response.delete(
            "IBE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_ip_mapping = await response.parse()
            assert source_ip_mapping is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.source_ip_mappings.with_raw_response.delete(
                "",
            )
