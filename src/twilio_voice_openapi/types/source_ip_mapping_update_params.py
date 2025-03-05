# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SourceIPMappingUpdateParams"]


class SourceIPMappingUpdateParams(TypedDict, total=False):
    sip_domain_sid: Required[Annotated[str, PropertyInfo(alias="SipDomainSid")]]
    """The SID of the SIP Domain that the IP Record should be mapped to."""
