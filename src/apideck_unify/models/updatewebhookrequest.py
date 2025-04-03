"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .status import Status
from .webhookeventtype import WebhookEventType
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class UpdateWebhookRequestTypedDict(TypedDict):
    description: NotRequired[Nullable[str]]
    r"""A description of the object."""
    status: NotRequired[Status]
    r"""The status of the webhook."""
    delivery_url: NotRequired[str]
    r"""The delivery url of the webhook endpoint."""
    events: NotRequired[List[WebhookEventType]]
    r"""The list of subscribed events for this webhook. [`*`] indicates that all events are enabled."""


class UpdateWebhookRequest(BaseModel):
    description: OptionalNullable[str] = UNSET
    r"""A description of the object."""

    status: Optional[Status] = None
    r"""The status of the webhook."""

    delivery_url: Optional[str] = None
    r"""The delivery url of the webhook endpoint."""

    events: Optional[List[WebhookEventType]] = None
    r"""The list of subscribed events for this webhook. [`*`] indicates that all events are enabled."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "status", "delivery_url", "events"]
        nullable_fields = ["description"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
