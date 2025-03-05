# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TargetCreateParams"]


class TargetCreateParams(TypedDict, total=False):
    target: Required[Annotated[str, PropertyInfo(alias="Target")]]
    """The SIP address you want Twilio to route your calls to.

    This must be a `sip:` schema. `sips` is NOT supported.
    """

    enabled: Annotated[bool, PropertyInfo(alias="Enabled")]
    """Whether the Target is enabled. The default is `true`."""

    friendly_name: Annotated[str, PropertyInfo(alias="FriendlyName")]
    """A descriptive string that you create to describe the resource.

    It is not unique and can be up to 255 characters long.
    """

    priority: Annotated[int, PropertyInfo(alias="Priority")]
    """The relative importance of the target.

    Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest
    number represents the most important target.
    """

    weight: Annotated[int, PropertyInfo(alias="Weight")]
    """
    The value that determines the relative share of the load the Target should
    receive compared to other Targets with the same priority. Can be an integer from
    1 to 65535, inclusive, and the default is 10. Targets with higher values receive
    more load than those with lower ones with the same priority.
    """
