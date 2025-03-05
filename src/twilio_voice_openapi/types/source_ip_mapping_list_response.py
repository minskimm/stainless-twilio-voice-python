# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .source_ip_mapping import SourceIPMapping

__all__ = ["SourceIPMappingListResponse", "Meta"]


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class SourceIPMappingListResponse(BaseModel):
    meta: Optional[Meta] = None

    source_ip_mappings: Optional[List[SourceIPMapping]] = None
