# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types.dialing_permissions import (
    CountryListResponse,
    CountryRetrieveResponse,
    CountryFetchHighRiskSpecialPrefixesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        country = client.dialing_permissions.countries.retrieve(
            "IsoCode",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.dialing_permissions.countries.with_raw_response.retrieve(
            "IsoCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with client.dialing_permissions.countries.with_streaming_response.retrieve(
            "IsoCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `iso_code` but received ''"):
            client.dialing_permissions.countries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: TwilioVoiceOpenAPI) -> None:
        country = client.dialing_permissions.countries.list()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        country = client.dialing_permissions.countries.list(
            continent="Continent",
            country_code="CountryCode",
            high_risk_special_numbers_enabled=True,
            high_risk_tollfraud_numbers_enabled=True,
            iso_code="IsoCode",
            low_risk_numbers_enabled=True,
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.dialing_permissions.countries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: TwilioVoiceOpenAPI) -> None:
        with client.dialing_permissions.countries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_fetch_high_risk_special_prefixes(self, client: TwilioVoiceOpenAPI) -> None:
        country = client.dialing_permissions.countries.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        )
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_fetch_high_risk_special_prefixes_with_all_params(self, client: TwilioVoiceOpenAPI) -> None:
        country = client.dialing_permissions.countries.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_fetch_high_risk_special_prefixes(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.dialing_permissions.countries.with_raw_response.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_fetch_high_risk_special_prefixes(self, client: TwilioVoiceOpenAPI) -> None:
        with client.dialing_permissions.countries.with_streaming_response.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_fetch_high_risk_special_prefixes(self, client: TwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `iso_code` but received ''"):
            client.dialing_permissions.countries.with_raw_response.fetch_high_risk_special_prefixes(
                iso_code="",
            )


class TestAsyncCountries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        country = await async_client.dialing_permissions.countries.retrieve(
            "IsoCode",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.dialing_permissions.countries.with_raw_response.retrieve(
            "IsoCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.dialing_permissions.countries.with_streaming_response.retrieve(
            "IsoCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `iso_code` but received ''"):
            await async_client.dialing_permissions.countries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        country = await async_client.dialing_permissions.countries.list()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        country = await async_client.dialing_permissions.countries.list(
            continent="Continent",
            country_code="CountryCode",
            high_risk_special_numbers_enabled=True,
            high_risk_tollfraud_numbers_enabled=True,
            iso_code="IsoCode",
            low_risk_numbers_enabled=True,
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.dialing_permissions.countries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.dialing_permissions.countries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_fetch_high_risk_special_prefixes(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        country = await async_client.dialing_permissions.countries.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        )
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_fetch_high_risk_special_prefixes_with_all_params(
        self, async_client: AsyncTwilioVoiceOpenAPI
    ) -> None:
        country = await async_client.dialing_permissions.countries.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
            page=0,
            page_size=1,
            page_token="PageToken",
        )
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_fetch_high_risk_special_prefixes(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.dialing_permissions.countries.with_raw_response.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_fetch_high_risk_special_prefixes(
        self, async_client: AsyncTwilioVoiceOpenAPI
    ) -> None:
        async with async_client.dialing_permissions.countries.with_streaming_response.fetch_high_risk_special_prefixes(
            iso_code="IsoCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryFetchHighRiskSpecialPrefixesResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_fetch_high_risk_special_prefixes(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `iso_code` but received ''"):
            await async_client.dialing_permissions.countries.with_raw_response.fetch_high_risk_special_prefixes(
                iso_code="",
            )
