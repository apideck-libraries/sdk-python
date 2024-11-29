"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DriveTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    name: str
    r"""The name of the drive"""
    description: NotRequired[Nullable[str]]
    r"""A description of the object."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class Drive(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    name: str
    r"""The name of the drive"""

    description: OptionalNullable[str] = UNSET
    r"""A description of the object."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "description",
            "custom_mappings",
            "updated_by",
            "created_by",
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