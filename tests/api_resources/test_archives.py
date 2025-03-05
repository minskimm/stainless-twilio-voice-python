# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_call(self, client: TwilioVoiceOpenAPI) -> None:
        archive = client.archives.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        )
        assert archive is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_call(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.archives.with_raw_response.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert archive is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_call(self, client: TwilioVoiceOpenAPI) -> None:
        with client.archives.with_streaming_response.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert archive is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_call(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.archives.with_raw_response.delete_call(
                sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            client.archives.with_raw_response.delete_call(
                sid="",
                date=parse_date("2019-12-27"),
            )


class TestAsyncArchives:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_call(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        archive = await async_client.archives.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        )
        assert archive is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_call(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.archives.with_raw_response.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert archive is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_call(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.archives.with_streaming_response.delete_call(
            sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert archive is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_call(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.archives.with_raw_response.delete_call(
                sid="CAE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sid` but received ''"):
            await async_client.archives.with_raw_response.delete_call(
                sid="",
                date=parse_date("2019-12-27"),
            )
