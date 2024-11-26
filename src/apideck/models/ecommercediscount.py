"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class EcommerceDiscountTypedDict(TypedDict):
    r"""An object representing a discount applied to an ecommerce order or product."""

    code: NotRequired[Nullable[str]]
    r"""The code used to apply the discount."""
    amount: NotRequired[Nullable[str]]
    r"""The fixed amount of the discount."""
    percentage: NotRequired[Nullable[str]]
    r"""The percentage of the discount."""


class EcommerceDiscount(BaseModel):
    r"""An object representing a discount applied to an ecommerce order or product."""

    code: OptionalNullable[str] = UNSET
    r"""The code used to apply the discount."""

    amount: OptionalNullable[str] = UNSET
    r"""The fixed amount of the discount."""

    percentage: OptionalNullable[str] = UNSET
    r"""The percentage of the discount."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["code", "amount", "percentage"]
        nullable_fields = ["code", "amount", "percentage"]
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