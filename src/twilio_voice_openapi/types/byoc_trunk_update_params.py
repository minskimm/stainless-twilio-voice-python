# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ByocTrunkUpdateParams"]


class ByocTrunkUpdateParams(TypedDict, total=False):
    cnam_lookup_enabled: Annotated[bool, PropertyInfo(alias="CnamLookupEnabled")]
    """Whether Caller ID Name (CNAM) lookup is enabled for the trunk.

    If enabled, all inbound calls to the BYOC Trunk from the United States and
    Canada automatically perform a CNAM Lookup and display Caller ID data on your
    phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for
    more information.
    """

    connection_policy_sid: Annotated[str, PropertyInfo(alias="ConnectionPolicySid")]
    """
    The SID of the Connection Policy that Twilio will use when routing traffic to
    your communications infrastructure.
    """

    friendly_name: Annotated[str, PropertyInfo(alias="FriendlyName")]
    """A descriptive string that you create to describe the resource.

    It is not unique and can be up to 255 characters long.
    """

    from_domain_sid: Annotated[str, PropertyInfo(alias="FromDomainSid")]
    """
    The SID of the SIP Domain that should be used in the `From` header of
    originating calls sent to your SIP infrastructure. If your SIP infrastructure
    allows users to "call back" an incoming call, configure this with a
    [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper
    routing. If not configured, the from domain will default to "sip.twilio.com".
    """

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """The HTTP method we should use to call `status_callback_url`.

    Can be: `GET` or `POST`.
    """

    status_callback_url: Annotated[str, PropertyInfo(alias="StatusCallbackUrl")]
    """
    The URL that we should call to pass status parameters (such as call ended) to
    your application.
    """

    voice_fallback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="VoiceFallbackMethod")]
    """The HTTP method we should use to call `voice_fallback_url`.

    Can be: `GET` or `POST`.
    """

    voice_fallback_url: Annotated[str, PropertyInfo(alias="VoiceFallbackUrl")]
    """
    The URL that we should call when an error occurs while retrieving or executing
    the TwiML requested by `voice_url`.
    """

    voice_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="VoiceMethod")]
    """The HTTP method we should use to call `voice_url`"""

    voice_url: Annotated[str, PropertyInfo(alias="VoiceUrl")]
    """The URL we should call when the BYOC Trunk receives a call."""
