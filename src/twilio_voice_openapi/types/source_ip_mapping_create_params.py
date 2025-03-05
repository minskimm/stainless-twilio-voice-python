# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SourceIPMappingCreateParams"]


class SourceIPMappingCreateParams(TypedDict, total=False):
    ip_record_sid: Required[Annotated[str, PropertyInfo(alias="IpRecordSid")]]
    """
    The Twilio-provided string that uniquely identifies the IP Record resource to
    map from.
    """

    sip_domain_sid: Required[Annotated[str, PropertyInfo(alias="SipDomainSid")]]
    """The SID of the SIP Domain that the IP Record should be mapped to."""
