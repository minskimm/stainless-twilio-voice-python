# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IPRecordUpdateParams"]


class IPRecordUpdateParams(TypedDict, total=False):
    friendly_name: Annotated[str, PropertyInfo(alias="FriendlyName")]
    """A descriptive string that you create to describe the resource.

    It is not unique and can be up to 255 characters long.
    """
