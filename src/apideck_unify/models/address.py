"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class Type(str, Enum):
    r"""The type of address."""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    HOME = "home"
    OFFICE = "office"
    SHIPPING = "shipping"
    BILLING = "billing"
    OTHER = "other"


class AddressTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""Unique identifier for the address."""
    type: NotRequired[Nullable[Type]]
    r"""The type of address."""
    string: NotRequired[Nullable[str]]
    r"""The address string. Some APIs don't provide structured address data."""
    name: NotRequired[Nullable[str]]
    r"""The name of the address."""
    line1: NotRequired[Nullable[str]]
    r"""Line 1 of the address e.g. number, street, suite, apt #, etc."""
    line2: NotRequired[Nullable[str]]
    r"""Line 2 of the address"""
    line3: NotRequired[Nullable[str]]
    r"""Line 3 of the address"""
    line4: NotRequired[Nullable[str]]
    r"""Line 4 of the address"""
    street_number: NotRequired[Nullable[str]]
    r"""Street number"""
    city: NotRequired[Nullable[str]]
    r"""Name of city."""
    state: NotRequired[Nullable[str]]
    r"""Name of state"""
    postal_code: NotRequired[Nullable[str]]
    r"""Zip code or equivalent."""
    country: NotRequired[Nullable[str]]
    r"""country code according to ISO 3166-1 alpha-2."""
    latitude: NotRequired[Nullable[str]]
    r"""Latitude of the address"""
    longitude: NotRequired[Nullable[str]]
    r"""Longitude of the address"""
    county: NotRequired[Nullable[str]]
    r"""Address field that holds a sublocality, such as a county"""
    contact_name: NotRequired[Nullable[str]]
    r"""Name of the contact person at the address"""
    salutation: NotRequired[Nullable[str]]
    r"""Salutation of the contact person at the address"""
    phone_number: NotRequired[Nullable[str]]
    r"""Phone number of the address"""
    fax: NotRequired[Nullable[str]]
    r"""Fax number of the address"""
    email: NotRequired[Nullable[str]]
    r"""Email address of the address"""
    website: NotRequired[Nullable[str]]
    r"""Website of the address"""
    notes: NotRequired[Nullable[str]]
    r"""Additional notes"""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""


class Address(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the address."""

    type: OptionalNullable[Type] = UNSET
    r"""The type of address."""

    string: OptionalNullable[str] = UNSET
    r"""The address string. Some APIs don't provide structured address data."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the address."""

    line1: OptionalNullable[str] = UNSET
    r"""Line 1 of the address e.g. number, street, suite, apt #, etc."""

    line2: OptionalNullable[str] = UNSET
    r"""Line 2 of the address"""

    line3: OptionalNullable[str] = UNSET
    r"""Line 3 of the address"""

    line4: OptionalNullable[str] = UNSET
    r"""Line 4 of the address"""

    street_number: OptionalNullable[str] = UNSET
    r"""Street number"""

    city: OptionalNullable[str] = UNSET
    r"""Name of city."""

    state: OptionalNullable[str] = UNSET
    r"""Name of state"""

    postal_code: OptionalNullable[str] = UNSET
    r"""Zip code or equivalent."""

    country: OptionalNullable[str] = UNSET
    r"""country code according to ISO 3166-1 alpha-2."""

    latitude: OptionalNullable[str] = UNSET
    r"""Latitude of the address"""

    longitude: OptionalNullable[str] = UNSET
    r"""Longitude of the address"""

    county: OptionalNullable[str] = UNSET
    r"""Address field that holds a sublocality, such as a county"""

    contact_name: OptionalNullable[str] = UNSET
    r"""Name of the contact person at the address"""

    salutation: OptionalNullable[str] = UNSET
    r"""Salutation of the contact person at the address"""

    phone_number: OptionalNullable[str] = UNSET
    r"""Phone number of the address"""

    fax: OptionalNullable[str] = UNSET
    r"""Fax number of the address"""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the address"""

    website: OptionalNullable[str] = UNSET
    r"""Website of the address"""

    notes: OptionalNullable[str] = UNSET
    r"""Additional notes"""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "type",
            "string",
            "name",
            "line1",
            "line2",
            "line3",
            "line4",
            "street_number",
            "city",
            "state",
            "postal_code",
            "country",
            "latitude",
            "longitude",
            "county",
            "contact_name",
            "salutation",
            "phone_number",
            "fax",
            "email",
            "website",
            "notes",
            "row_version",
        ]
        nullable_fields = [
            "id",
            "type",
            "string",
            "name",
            "line1",
            "line2",
            "line3",
            "line4",
            "street_number",
            "city",
            "state",
            "postal_code",
            "country",
            "latitude",
            "longitude",
            "county",
            "contact_name",
            "salutation",
            "phone_number",
            "fax",
            "email",
            "website",
            "notes",
            "row_version",
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
