# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    dialing_permissions_inheritance: Annotated[bool, PropertyInfo(alias="DialingPermissionsInheritance")]
    """
    `true` for the sub-account to inherit voice dialing permissions from the Master
    Project; otherwise `false`.
    """
