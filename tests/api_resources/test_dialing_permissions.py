# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from twilio_voice_openapi import TwilioVoiceOpenAPI, AsyncTwilioVoiceOpenAPI
from twilio_voice_openapi.types import (
    DialingPermissionCreateBulkCountryUpdatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDialingPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_bulk_country_updates(self, client: TwilioVoiceOpenAPI) -> None:
        dialing_permission = client.dialing_permissions.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        )
        assert_matches_type(DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_bulk_country_updates(self, client: TwilioVoiceOpenAPI) -> None:
        response = client.dialing_permissions.with_raw_response.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialing_permission = response.parse()
        assert_matches_type(DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_bulk_country_updates(self, client: TwilioVoiceOpenAPI) -> None:
        with client.dialing_permissions.with_streaming_response.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialing_permission = response.parse()
            assert_matches_type(
                DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDialingPermissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_bulk_country_updates(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        dialing_permission = await async_client.dialing_permissions.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        )
        assert_matches_type(DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_bulk_country_updates(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        response = await async_client.dialing_permissions.with_raw_response.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialing_permission = await response.parse()
        assert_matches_type(DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_bulk_country_updates(self, async_client: AsyncTwilioVoiceOpenAPI) -> None:
        async with async_client.dialing_permissions.with_streaming_response.create_bulk_country_updates(
            update_request='[ { "iso_code": "GB", "low_risk_numbers": "Enabled", "high_risk_special_numbers":"Enabled", "high_risk_irsf_numbers": "Enabled" } ]',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialing_permission = await response.parse()
            assert_matches_type(
                DialingPermissionCreateBulkCountryUpdatesResponse, dialing_permission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
