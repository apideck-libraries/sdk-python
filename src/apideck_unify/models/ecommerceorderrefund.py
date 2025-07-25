"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EcommerceOrderRefundTypedDict(TypedDict):
    r"""A refund for an ecommerce order."""

    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    amount: NotRequired[str]
    r"""The amount of the refund."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    reason: NotRequired[str]
    r"""The reason for the refund."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""


class EcommerceOrderRefund(BaseModel):
    r"""A refund for an ecommerce order."""

    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    amount: Optional[str] = None
    r"""The amount of the refund."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    reason: Optional[str] = None
    r"""The reason for the refund."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "amount", "currency", "reason", "created_at"]
        nullable_fields = ["id", "currency", "created_at"]
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
