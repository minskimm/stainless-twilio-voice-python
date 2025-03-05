# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["IPRecord"]


class IPRecord(BaseModel):
    account_sid: Optional[str] = None
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that
    created the IP Record resource.
    """

    cidr_prefix_length: Optional[int] = None
    """
    An integer representing the length of the
    [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address.
    By default the entire IP address is used, which for IPv4 is value 32.
    """

    date_created: Optional[datetime] = None
    """
    The date and time in GMT that the resource was created specified in
    [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    date_updated: Optional[datetime] = None
    """
    The date and time in GMT that the resource was last updated specified in
    [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    friendly_name: Optional[str] = None
    """The string that you assigned to describe the resource."""

    ip_address: Optional[str] = None
    """An IP address in dotted decimal notation, IPv4 only."""

    sid: Optional[str] = None
    """The unique string that we created to identify the IP Record resource."""

    url: Optional[str] = None
    """The absolute URL of the resource."""
