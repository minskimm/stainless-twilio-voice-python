# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ConnectionPolicyTarget"]


class ConnectionPolicyTarget(BaseModel):
    account_sid: Optional[str] = None
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that
    created the Target resource.
    """

    connection_policy_sid: Optional[str] = None
    """The SID of the Connection Policy that owns the Target."""

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

    enabled: Optional[bool] = None
    """Whether the target is enabled. The default is `true`."""

    friendly_name: Optional[str] = None
    """The string that you assigned to describe the resource."""

    priority: Optional[int] = None
    """The relative importance of the target.

    Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest
    number represents the most important target.
    """

    sid: Optional[str] = None
    """The unique string that we created to identify the Target resource."""

    target: Optional[str] = None
    """The SIP address you want Twilio to route your calls to.

    This must be a `sip:` schema. `sips` is NOT supported.
    """

    url: Optional[str] = None
    """The absolute URL of the resource."""

    weight: Optional[int] = None
    """
    The value that determines the relative share of the load the Target should
    receive compared to other Targets with the same priority. Can be an integer from
    1 to 65535, inclusive, and the default is 10. Targets with higher values receive
    more load than those with lower ones with the same priority.
    """
