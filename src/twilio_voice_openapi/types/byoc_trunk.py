# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ByocTrunk"]


class ByocTrunk(BaseModel):
    account_sid: Optional[str] = None
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that
    created the BYOC Trunk resource.
    """

    cnam_lookup_enabled: Optional[bool] = None
    """Whether Caller ID Name (CNAM) lookup is enabled for the trunk.

    If enabled, all inbound calls to the BYOC Trunk from the United States and
    Canada automatically perform a CNAM Lookup and display Caller ID data on your
    phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for
    more information.
    """

    connection_policy_sid: Optional[str] = None
    """
    The SID of the Connection Policy that Twilio will use when routing traffic to
    your communications infrastructure.
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

    from_domain_sid: Optional[str] = None
    """
    The SID of the SIP Domain that should be used in the `From` header of
    originating calls sent to your SIP infrastructure. If your SIP infrastructure
    allows users to "call back" an incoming call, configure this with a
    [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
    routing. If not configured, the from domain will default to "sip.twilio.com".
    """

    sid: Optional[str] = None
    """The unique string that that we created to identify the BYOC Trunk resource."""

    status_callback_method: Optional[Literal["GET", "POST"]] = None
    """The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`."""

    status_callback_url: Optional[str] = None
    """
    The URL that we call to pass status parameters (such as call ended) to your
    application.
    """

    url: Optional[str] = None
    """The absolute URL of the resource."""

    voice_fallback_method: Optional[Literal["GET", "POST"]] = None
    """The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`."""

    voice_fallback_url: Optional[str] = None
    """
    The URL that we call when an error occurs while retrieving or executing the
    TwiML requested from `voice_url`.
    """

    voice_method: Optional[Literal["GET", "POST"]] = None
    """The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`."""

    voice_url: Optional[str] = None
    """The URL we call using the `voice_method` when the BYOC Trunk receives a call."""
