# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types import (
    IPRecord,
    IPRecordListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.create(
            ip_address="10.2.3.4",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.create(
            ip_address="10.2.3.4",
            cidr_prefix_length=30,
            friendly_name="friendly_name",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.ip_records.with_raw_response.create(
            ip_address="10.2.3.4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: TwilioVoiceOpenAPI) -> None:
        with client.ip_records.with_streaming_response.create(
            ip_address="10.2.3.4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.ip_records.with_raw_response.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.ip_records.with_streaming_response.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.ip_records.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            friendly_name="update_name",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.ip_records.with_raw_response.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: TwilioVoiceOpenAPI) -> None:
        with client.ip_records.with_streaming_response.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.ip_records.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.list()
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.ip_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = response.parse()
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.ip_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = response.parse()
            assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: TwilioVoiceOpenAPI) -> None:
        ip_record = client.ip_records.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert ip_record is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.ip_records.with_raw_response.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = response.parse()
        assert ip_record is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with client.ip_records.with_streaming_response.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = response.parse()
            assert ip_record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.ip_records.with_raw_response.delete(
                "",
            )


class TestAsyncIPRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.create(
            ip_address="10.2.3.4",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.create(
            ip_address="10.2.3.4",
            cidr_prefix_length=30,
            friendly_name="friendly_name",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.ip_records.with_raw_response.create(
            ip_address="10.2.3.4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = await response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.ip_records.with_streaming_response.create(
            ip_address="10.2.3.4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = await response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.ip_records.with_raw_response.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = await response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.ip_records.with_streaming_response.retrieve(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = await response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.ip_records.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            friendly_name="update_name",
        )
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.ip_records.with_raw_response.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = await response.parse()
        assert_matches_type(IPRecord, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.ip_records.with_streaming_response.update(
            sid="ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = await response.parse()
            assert_matches_type(IPRecord, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.ip_records.with_raw_response.update(
                sid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.list()
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.list(
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.ip_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = await response.parse()
        assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.ip_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = await response.parse()
            assert_matches_type(IPRecordListResponse, ip_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        ip_record = await async_client.ip_records.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert ip_record is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.ip_records.with_raw_response.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_record = await response.parse()
        assert ip_record is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.ip_records.with_streaming_response.delete(
            "ILE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_record = await response.parse()
            assert ip_record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.ip_records.with_raw_response.delete(
                "",
            )
