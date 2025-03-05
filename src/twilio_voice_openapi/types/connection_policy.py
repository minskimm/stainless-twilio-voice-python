# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ConnectionPolicy"]


class ConnectionPolicy(BaseModel):
    account_sid: Optional[str] = None
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that
    created the Connection Policy resource.
    """

    date_created: Optional[datetime] = None
    """
    The date and time in GMT when the resource was created specified in
    [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    date_updated: Optional[datetime] = None
    """
    The date and time in GMT when the resource was last updated specified in
    [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    friendly_name: Optional[str] = None
    """The string that you assigned to describe the resource."""

    links: Optional[object] = None
    """The URLs of related resources."""

    sid: Optional[str] = None
    """The unique string that we created to identify the Connection Policy resource."""

    url: Optional[str] = None
    """The absolute URL of the resource."""
