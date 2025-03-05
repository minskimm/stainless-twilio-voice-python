# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SourceIPMapping"]


class SourceIPMapping(BaseModel):
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

    ip_record_sid: Optional[str] = None
    """
    The Twilio-provided string that uniquely identifies the IP Record resource to
    map from.
    """

    sid: Optional[str] = None
    """The unique string that we created to identify the IP Record resource."""

    sip_domain_sid: Optional[str] = None
    """The SID of the SIP Domain that the IP Record is mapped to."""

    url: Optional[str] = None
    """The absolute URL of the resource."""
