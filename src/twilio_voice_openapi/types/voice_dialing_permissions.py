# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VoiceDialingPermissions"]


class VoiceDialingPermissions(BaseModel):
    dialing_permissions_inheritance: Optional[bool] = None
    """
    `true` if the sub-account will inherit voice dialing permissions from the Master
    Project; otherwise `false`.
    """

    url: Optional[str] = None
    """The absolute URL of this resource."""
