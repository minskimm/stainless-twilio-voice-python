# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DialingPermissionCreateBulkCountryUpdatesParams"]


class DialingPermissionCreateBulkCountryUpdatesParams(TypedDict, total=False):
    update_request: Required[Annotated[str, PropertyInfo(alias="UpdateRequest")]]
    """URL encoded JSON array of update objects.

    example :
    `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`
    """
