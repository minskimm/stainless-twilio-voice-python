from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `twilio_voice_openapi.resources` module.

    This is used so that we can lazily import `twilio_voice_openapi.resources` only when
    needed *and* so that users can just import `twilio_voice_openapi` and reference `twilio_voice_openapi.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("twilio_voice_openapi.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
