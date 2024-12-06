"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .email import Email, EmailTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UserTypedDict(TypedDict):
    emails: List[EmailTypedDict]
    id: NotRequired[str]
    r"""The unique identifier for the user"""
    parent_id: NotRequired[Nullable[str]]
    r"""The parent user id"""
    username: NotRequired[Nullable[str]]
    r"""The username of the user"""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the person."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the person."""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    division: NotRequired[Nullable[str]]
    r"""The division the person is currently in. Usually a collection of departments or teams or regions."""
    department: NotRequired[Nullable[str]]
    r"""The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field."""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    employee_number: NotRequired[Nullable[str]]
    r"""An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company."""
    description: NotRequired[Nullable[str]]
    r"""A description of the object."""
    image: NotRequired[Nullable[str]]
    r"""The URL of the user's avatar"""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    status: NotRequired[Nullable[str]]
    r"""The status of the user"""
    addresses: NotRequired[List[AddressTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    updated_at: NotRequired[Nullable[str]]
    r"""The date and time when the user was last updated."""
    created_at: NotRequired[Nullable[str]]
    r"""The date and time when the user was created."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class User(BaseModel):
    emails: List[Email]

    id: Optional[str] = None
    r"""The unique identifier for the user"""

    parent_id: OptionalNullable[str] = UNSET
    r"""The parent user id"""

    username: OptionalNullable[str] = UNSET
    r"""The username of the user"""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the person."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the person."""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    division: OptionalNullable[str] = UNSET
    r"""The division the person is currently in. Usually a collection of departments or teams or regions."""

    department: Annotated[
        OptionalNullable[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET
    r"""The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field."""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    employee_number: OptionalNullable[str] = UNSET
    r"""An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company."""

    description: OptionalNullable[str] = UNSET
    r"""A description of the object."""

    image: OptionalNullable[str] = UNSET
    r"""The URL of the user's avatar"""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    status: OptionalNullable[str] = UNSET
    r"""The status of the user"""

    addresses: Optional[List[Address]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    updated_at: OptionalNullable[str] = UNSET
    r"""The date and time when the user was last updated."""

    created_at: OptionalNullable[str] = UNSET
    r"""The date and time when the user was created."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "parent_id",
            "username",
            "first_name",
            "last_name",
            "title",
            "division",
            "department",
            "company_name",
            "employee_number",
            "description",
            "image",
            "language",
            "status",
            "addresses",
            "phone_numbers",
            "custom_mappings",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "parent_id",
            "username",
            "first_name",
            "last_name",
            "title",
            "division",
            "department",
            "company_name",
            "employee_number",
            "description",
            "image",
            "language",
            "status",
            "custom_mappings",
            "updated_at",
            "created_at",
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
