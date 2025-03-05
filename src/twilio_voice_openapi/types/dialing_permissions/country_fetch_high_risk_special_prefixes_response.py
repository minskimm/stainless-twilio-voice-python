# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CountryFetchHighRiskSpecialPrefixesResponse", "Content", "Meta"]


class Content(BaseModel):
    prefix: Optional[str] = None
    """
    A prefix is a contiguous number range for a block of E.164 numbers that includes
    the E.164 assigned country code. For example, a North American Numbering Plan
    prefix like `+1510720` written like `+1(510) 720` matches all numbers inclusive
    from `+1(510) 720-0000` to `+1(510) 720-9999`.
    """


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class CountryFetchHighRiskSpecialPrefixesResponse(BaseModel):
    content: Optional[List[Content]] = None

    meta: Optional[Meta] = None
