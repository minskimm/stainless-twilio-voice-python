# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DialingPermissionCreateBulkCountryUpdatesResponse"]


class DialingPermissionCreateBulkCountryUpdatesResponse(BaseModel):
    update_count: Optional[int] = None
    """The number of countries updated"""

    update_request: Optional[str] = None
    """
    A bulk update request to change voice dialing country permissions stored as a
    URL-encoded, JSON array of update objects. For example :
    `[ { "iso_code": "GB", "low_risk_numbers_enabled": "true", "high_risk_special_numbers_enabled":"true", "high_risk_tollfraud_numbers_enabled": "false" } ]`
    """
