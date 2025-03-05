# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TargetListParams"]


class TargetListParams(TypedDict, total=False):
    page: Annotated[int, PropertyInfo(alias="Page")]
    """The page index. This value is simply for client state."""

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """How many resources to return in each list page.

    The default is 50, and the maximum is 1000.
    """

    page_token: Annotated[str, PropertyInfo(alias="PageToken")]
    """The page token. This is provided by the API."""
