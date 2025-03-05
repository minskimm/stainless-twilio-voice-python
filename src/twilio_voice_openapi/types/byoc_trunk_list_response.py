# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .byoc_trunk import ByocTrunk

__all__ = ["ByocTrunkListResponse", "Meta"]


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class ByocTrunkListResponse(BaseModel):
    byoc_trunks: Optional[List[ByocTrunk]] = None

    meta: Optional[Meta] = None
