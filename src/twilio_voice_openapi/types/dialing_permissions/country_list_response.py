# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CountryListResponse", "Content", "Meta"]


class Content(BaseModel):
    continent: Optional[str] = None
    """The name of the continent in which the country is located."""

    country_codes: Optional[List[str]] = None
    """
    The E.164 assigned
    [country codes(s)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    """

    high_risk_special_numbers_enabled: Optional[bool] = None
    """Whether dialing to high-risk special services numbers is enabled.

    These prefixes include number ranges allocated by the country and include
    premium numbers, special services, shared cost, and others
    """

    high_risk_tollfraud_numbers_enabled: Optional[bool] = None
    """
    Whether dialing to high-risk
    [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html)
    numbers is enabled. These prefixes include narrow number ranges that have a
    high-risk of international revenue sharing fraud (IRSF) attacks, also known as
    [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html).
    These prefixes are collected from anti-fraud databases and verified by analyzing
    calls on our network. These prefixes are not available for download and are
    updated frequently
    """

    iso_code: Optional[str] = None
    """The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)."""

    links: Optional[object] = None
    """A list of URLs related to this resource."""

    low_risk_numbers_enabled: Optional[bool] = None
    """Whether dialing to low-risk numbers is enabled."""

    name: Optional[str] = None
    """The name of the country."""

    url: Optional[str] = None
    """The absolute URL of this resource."""


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class CountryListResponse(BaseModel):
    content: Optional[List[Content]] = None

    meta: Optional[Meta] = None
