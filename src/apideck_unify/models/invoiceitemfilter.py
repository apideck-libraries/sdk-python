"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from apideck_unify.utils import FieldMetadata
from enum import Enum
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoiceItemFilterInvoiceItemType(str, Enum):
    r"""The type of invoice item, indicating whether it is an inventory item, a service, or another type."""

    INVENTORY = "inventory"
    SERVICE = "service"
    OTHER = "other"


class InvoiceItemFilterTypedDict(TypedDict):
    type: NotRequired[Nullable[InvoiceItemFilterInvoiceItemType]]
    r"""The type of invoice item, indicating whether it is an inventory item, a service, or another type."""


class InvoiceItemFilter(BaseModel):
    type: Annotated[
        OptionalNullable[InvoiceItemFilterInvoiceItemType], FieldMetadata(query=True)
    ] = UNSET
    r"""The type of invoice item, indicating whether it is an inventory item, a service, or another type."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type"]
        nullable_fields = ["type"]
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
