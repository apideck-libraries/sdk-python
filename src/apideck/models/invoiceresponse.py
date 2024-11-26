"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InvoiceResponseTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""


class InvoiceResponse(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "downstream_id"]
        nullable_fields = ["downstream_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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