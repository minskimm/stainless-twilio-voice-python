# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IPRecordCreateParams"]


class IPRecordCreateParams(TypedDict, total=False):
    ip_address: Required[Annotated[str, PropertyInfo(alias="IpAddress")]]
    """An IP address in dotted decimal notation, IPv4 only."""

    cidr_prefix_length: Annotated[int, PropertyInfo(alias="CidrPrefixLength")]
    """
    An integer representing the length of the
    [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address.
    By default the entire IP address is used, which for IPv4 is value 32.
    """

    friendly_name: Annotated[str, PropertyInfo(alias="FriendlyName")]
    """A descriptive string that you create to describe the resource.

    It is not unique and can be up to 255 characters long.
    """
