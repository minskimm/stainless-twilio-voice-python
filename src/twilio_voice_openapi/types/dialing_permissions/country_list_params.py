# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CountryListParams"]


class CountryListParams(TypedDict, total=False):
    continent: Annotated[str, PropertyInfo(alias="Continent")]
    """Filter to retrieve the country permissions by specifying the continent"""

    country_code: Annotated[str, PropertyInfo(alias="CountryCode")]
    """
    Filter the results by specified
    [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    """

    high_risk_special_numbers_enabled: Annotated[bool, PropertyInfo(alias="HighRiskSpecialNumbersEnabled")]
    """
    Filter to retrieve the country permissions with dialing to high-risk special
    service numbers enabled. Can be: `true` or `false`
    """

    high_risk_tollfraud_numbers_enabled: Annotated[bool, PropertyInfo(alias="HighRiskTollfraudNumbersEnabled")]
    """
    Filter to retrieve the country permissions with dialing to high-risk
    [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html)
    numbers enabled. Can be: `true` or `false`.
    """

    iso_code: Annotated[str, PropertyInfo(alias="IsoCode")]
    """
    Filter to retrieve the country permissions by specifying the
    [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
    """

    low_risk_numbers_enabled: Annotated[bool, PropertyInfo(alias="LowRiskNumbersEnabled")]
    """
    Filter to retrieve the country permissions with dialing to low-risk numbers
    enabled. Can be: `true` or `false`.
    """

    page: Annotated[int, PropertyInfo(alias="Page")]
    """The page index. This value is simply for client state."""

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """How many resources to return in each list page.

    The default is 50, and the maximum is 1000.
    """

    page_token: Annotated[str, PropertyInfo(alias="PageToken")]
    """The page token. This is provided by the API."""
