# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ip_record import IPRecord

__all__ = ["IPRecordListResponse", "Meta"]


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class IPRecordListResponse(BaseModel):
    ip_records: Optional[List[IPRecord]] = None

    meta: Optional[Meta] = None
