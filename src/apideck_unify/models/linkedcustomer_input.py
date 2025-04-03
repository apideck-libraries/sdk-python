"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinkedCustomerInputTypedDict(TypedDict):
    r"""The customer this entity is linked to."""

    id: NotRequired[str]
    r"""The ID of the customer this entity is linked to."""
    display_name: NotRequired[Nullable[str]]
    r"""The display name of the customer."""
    name: NotRequired[str]
    r"""The name of the customer. Deprecated, use display_name instead."""
    email: NotRequired[str]
    r"""The email address of the customer."""


class LinkedCustomerInput(BaseModel):
    r"""The customer this entity is linked to."""

    id: Optional[str] = None
    r"""The ID of the customer this entity is linked to."""

    display_name: OptionalNullable[str] = UNSET
    r"""The display name of the customer."""

    name: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""The name of the customer. Deprecated, use display_name instead."""

    email: Optional[str] = None
    r"""The email address of the customer."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "display_name", "name", "email"]
        nullable_fields = ["display_name"]
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
