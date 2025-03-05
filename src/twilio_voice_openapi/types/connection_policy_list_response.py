# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .connection_policy import ConnectionPolicy

__all__ = ["ConnectionPolicyListResponse", "Meta"]


class Meta(BaseModel):
    first_page_url: Optional[str] = None

    key: Optional[str] = None

    next_page_url: Optional[str] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    previous_page_url: Optional[str] = None

    url: Optional[str] = None


class ConnectionPolicyListResponse(BaseModel):
    connection_policies: Optional[List[ConnectionPolicy]] = None

    meta: Optional[Meta] = None
