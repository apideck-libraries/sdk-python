"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class EcommerceAddressTypedDict(TypedDict):
    r"""An object representing a shipping or billing address."""

    line1: NotRequired[Nullable[str]]
    r"""Address line 1 of the billing address."""
    line2: NotRequired[Nullable[str]]
    r"""Address line 2 of the billing address."""
    company_name: NotRequired[Nullable[str]]
    r"""Company name of the customer"""
    city: NotRequired[Nullable[str]]
    r"""City of the billing address."""
    state: NotRequired[Nullable[str]]
    r"""State/province of the billing address."""
    postal_code: NotRequired[Nullable[str]]
    r"""Postal/ZIP code of the billing address."""
    country: NotRequired[Nullable[str]]
    r"""Country of the billing address."""


class EcommerceAddress(BaseModel):
    r"""An object representing a shipping or billing address."""

    line1: OptionalNullable[str] = UNSET
    r"""Address line 1 of the billing address."""

    line2: OptionalNullable[str] = UNSET
    r"""Address line 2 of the billing address."""

    company_name: OptionalNullable[str] = UNSET
    r"""Company name of the customer"""

    city: OptionalNullable[str] = UNSET
    r"""City of the billing address."""

    state: OptionalNullable[str] = UNSET
    r"""State/province of the billing address."""

    postal_code: OptionalNullable[str] = UNSET
    r"""Postal/ZIP code of the billing address."""

    country: OptionalNullable[str] = UNSET
    r"""Country of the billing address."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "line1",
            "line2",
            "company_name",
            "city",
            "state",
            "postal_code",
            "country",
        ]
        nullable_fields = [
            "line1",
            "line2",
            "company_name",
            "city",
            "state",
            "postal_code",
            "country",
        ]
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