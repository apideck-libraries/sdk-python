"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class LinkedTaxRateTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""The ID of the object."""
    code: NotRequired[Nullable[str]]
    r"""Tax rate code"""
    name: NotRequired[Nullable[str]]
    r"""Name of the tax rate"""
    rate: NotRequired[Nullable[float]]
    r"""Rate of the tax rate"""


class LinkedTaxRate(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""The ID of the object."""

    code: OptionalNullable[str] = UNSET
    r"""Tax rate code"""

    name: OptionalNullable[str] = UNSET
    r"""Name of the tax rate"""

    rate: OptionalNullable[float] = UNSET
    r"""Rate of the tax rate"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "name", "rate"]
        nullable_fields = ["id", "code", "name", "rate"]
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
