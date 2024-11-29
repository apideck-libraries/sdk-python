"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from enum import Enum
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class EventSource(str, Enum):
    r"""Unify event source"""

    NATIVE = "native"
    VIRTUAL = "virtual"


class ConnectorEventTypedDict(TypedDict):
    r"""Unify event that is supported on the connector. Events are delivered via Webhooks."""

    event_type: NotRequired[str]
    r"""Unify event type"""
    event_source: NotRequired[EventSource]
    r"""Unify event source"""
    downstream_event_type: NotRequired[str]
    r"""Downstream event type"""
    resources: NotRequired[List[str]]
    entity_type: NotRequired[str]
    r"""Unify entity type"""


class ConnectorEvent(BaseModel):
    r"""Unify event that is supported on the connector. Events are delivered via Webhooks."""

    event_type: Optional[str] = None
    r"""Unify event type"""

    event_source: Optional[EventSource] = None
    r"""Unify event source"""

    downstream_event_type: Optional[str] = None
    r"""Downstream event type"""

    resources: Optional[List[str]] = None

    entity_type: Optional[str] = None
    r"""Unify entity type"""