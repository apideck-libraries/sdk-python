"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formfieldoption import FormFieldOption, FormFieldOptionTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class FormFieldType(str, Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"
    TEL = "tel"
    EMAIL = "email"
    URL = "url"
    TEXTAREA = "textarea"
    SELECT = "select"
    FILTERED_SELECT = "filtered-select"
    MULTI_SELECT = "multi-select"
    DATETIME = "datetime"
    DATE = "date"
    TIME = "time"
    NUMBER = "number"


class FormFieldTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The unique identifier of the form field."""
    label: NotRequired[str]
    r"""The label of the field"""
    placeholder: NotRequired[Nullable[str]]
    r"""The placeholder for the form field"""
    description: NotRequired[Nullable[str]]
    r"""The description of the form field"""
    type: NotRequired[FormFieldType]
    required: NotRequired[bool]
    r"""Indicates if the form field is required, which means it must be filled in before the form can be submitted"""
    custom_field: NotRequired[bool]
    allow_custom_values: NotRequired[bool]
    r"""Only applicable to select fields. Allow the user to add a custom value though the option select if the desired value is not in the option select list."""
    disabled: NotRequired[Nullable[bool]]
    r"""Indicates if the form field is displayed in a “read-only” mode."""
    hidden: NotRequired[Nullable[bool]]
    r"""Indicates if the form field is not displayed but the value that is being stored on the connection."""
    deprecated: NotRequired[Nullable[bool]]
    r"""When the setting is deprecated, it should be hidden from the user interface. The value will still be stored on the connection for the sake of backwards compatibility."""
    sensitive: NotRequired[Nullable[bool]]
    r"""Indicates if the form field contains sensitive data, which will display the value as a masked input."""
    prefix: NotRequired[Nullable[str]]
    r"""Prefix to display in front of the form field."""
    suffix: NotRequired[Nullable[str]]
    r"""Suffix to display next to the form field."""
    options: NotRequired[List[FormFieldOptionTypedDict]]


class FormField(BaseModel):
    id: Optional[str] = None
    r"""The unique identifier of the form field."""

    label: Optional[str] = None
    r"""The label of the field"""

    placeholder: OptionalNullable[str] = UNSET
    r"""The placeholder for the form field"""

    description: OptionalNullable[str] = UNSET
    r"""The description of the form field"""

    type: Optional[FormFieldType] = None

    required: Optional[bool] = None
    r"""Indicates if the form field is required, which means it must be filled in before the form can be submitted"""

    custom_field: Optional[bool] = None

    allow_custom_values: Optional[bool] = False
    r"""Only applicable to select fields. Allow the user to add a custom value though the option select if the desired value is not in the option select list."""

    disabled: OptionalNullable[bool] = UNSET
    r"""Indicates if the form field is displayed in a “read-only” mode."""

    hidden: OptionalNullable[bool] = UNSET
    r"""Indicates if the form field is not displayed but the value that is being stored on the connection."""

    deprecated: OptionalNullable[bool] = UNSET
    r"""When the setting is deprecated, it should be hidden from the user interface. The value will still be stored on the connection for the sake of backwards compatibility."""

    sensitive: OptionalNullable[bool] = UNSET
    r"""Indicates if the form field contains sensitive data, which will display the value as a masked input."""

    prefix: OptionalNullable[str] = UNSET
    r"""Prefix to display in front of the form field."""

    suffix: OptionalNullable[str] = UNSET
    r"""Suffix to display next to the form field."""

    options: Optional[List[FormFieldOption]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "label",
            "placeholder",
            "description",
            "type",
            "required",
            "custom_field",
            "allow_custom_values",
            "disabled",
            "hidden",
            "deprecated",
            "sensitive",
            "prefix",
            "suffix",
            "options",
        ]
        nullable_fields = [
            "placeholder",
            "description",
            "disabled",
            "hidden",
            "deprecated",
            "sensitive",
            "prefix",
            "suffix",
        ]
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
