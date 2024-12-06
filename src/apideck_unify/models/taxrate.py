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
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ComponentsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    name: NotRequired[str]
    rate: NotRequired[Nullable[float]]
    compound: NotRequired[Nullable[bool]]


class Components(BaseModel):
    id: OptionalNullable[str] = UNSET

    name: Optional[str] = None

    rate: OptionalNullable[float] = UNSET

    compound: OptionalNullable[bool] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "name", "rate", "compound"]
        nullable_fields = ["id", "rate", "compound"]
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


class TaxRateStatus(str, Enum):
    r"""Tax rate status"""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class SubsidiariesModelTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The ID of the subsidiary."""


class SubsidiariesModel(BaseModel):
    id: Optional[str] = None
    r"""The ID of the subsidiary."""


class TaxRateTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""ID assigned to identify this tax rate."""
    name: NotRequired[str]
    r"""Name assigned to identify this tax rate."""
    code: NotRequired[Nullable[str]]
    r"""Tax code assigned to identify this tax rate."""
    description: NotRequired[Nullable[str]]
    r"""Description of tax rate"""
    effective_tax_rate: NotRequired[Nullable[float]]
    r"""Effective tax rate"""
    total_tax_rate: NotRequired[Nullable[float]]
    r"""Not compounded sum of the components of a tax rate"""
    tax_payable_account_id: NotRequired[Nullable[str]]
    r"""Unique identifier for the account for tax collected."""
    tax_remitted_account_id: NotRequired[Nullable[str]]
    r"""Unique identifier for the account for tax remitted."""
    components: NotRequired[Nullable[List[ComponentsTypedDict]]]
    type: NotRequired[Nullable[str]]
    r"""Tax type used to indicate the source of tax collected or paid"""
    report_tax_type: NotRequired[Nullable[str]]
    r"""Report Tax type to aggregate tax collected or paid for reporting purposes"""
    original_tax_rate_id: NotRequired[Nullable[str]]
    r"""ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities."""
    status: NotRequired[Nullable[TaxRateStatus]]
    r"""Tax rate status"""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
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
    subsidiaries: NotRequired[List[SubsidiariesModelTypedDict]]
    r"""The subsidiaries this belongs to."""


class TaxRate(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""ID assigned to identify this tax rate."""

    name: Optional[str] = None
    r"""Name assigned to identify this tax rate."""

    code: OptionalNullable[str] = UNSET
    r"""Tax code assigned to identify this tax rate."""

    description: OptionalNullable[str] = UNSET
    r"""Description of tax rate"""

    effective_tax_rate: OptionalNullable[float] = UNSET
    r"""Effective tax rate"""

    total_tax_rate: OptionalNullable[float] = UNSET
    r"""Not compounded sum of the components of a tax rate"""

    tax_payable_account_id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the account for tax collected."""

    tax_remitted_account_id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the account for tax remitted."""

    components: OptionalNullable[List[Components]] = UNSET

    type: OptionalNullable[str] = UNSET
    r"""Tax type used to indicate the source of tax collected or paid"""

    report_tax_type: OptionalNullable[str] = UNSET
    r"""Report Tax type to aggregate tax collected or paid for reporting purposes"""

    original_tax_rate_id: OptionalNullable[str] = UNSET
    r"""ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities."""

    status: OptionalNullable[TaxRateStatus] = UNSET
    r"""Tax rate status"""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

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

    subsidiaries: Optional[List[SubsidiariesModel]] = None
    r"""The subsidiaries this belongs to."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "name",
            "code",
            "description",
            "effective_tax_rate",
            "total_tax_rate",
            "tax_payable_account_id",
            "tax_remitted_account_id",
            "components",
            "type",
            "report_tax_type",
            "original_tax_rate_id",
            "status",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
            "subsidiaries",
        ]
        nullable_fields = [
            "id",
            "code",
            "description",
            "effective_tax_rate",
            "total_tax_rate",
            "tax_payable_account_id",
            "tax_remitted_account_id",
            "components",
            "type",
            "report_tax_type",
            "original_tax_rate_id",
            "status",
            "custom_mappings",
            "row_version",
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


class TaxRateInputTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""ID assigned to identify this tax rate."""
    name: NotRequired[str]
    r"""Name assigned to identify this tax rate."""
    code: NotRequired[Nullable[str]]
    r"""Tax code assigned to identify this tax rate."""
    description: NotRequired[Nullable[str]]
    r"""Description of tax rate"""
    effective_tax_rate: NotRequired[Nullable[float]]
    r"""Effective tax rate"""
    total_tax_rate: NotRequired[Nullable[float]]
    r"""Not compounded sum of the components of a tax rate"""
    tax_payable_account_id: NotRequired[Nullable[str]]
    r"""Unique identifier for the account for tax collected."""
    tax_remitted_account_id: NotRequired[Nullable[str]]
    r"""Unique identifier for the account for tax remitted."""
    components: NotRequired[Nullable[List[ComponentsTypedDict]]]
    type: NotRequired[Nullable[str]]
    r"""Tax type used to indicate the source of tax collected or paid"""
    report_tax_type: NotRequired[Nullable[str]]
    r"""Report Tax type to aggregate tax collected or paid for reporting purposes"""
    original_tax_rate_id: NotRequired[Nullable[str]]
    r"""ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities."""
    status: NotRequired[Nullable[TaxRateStatus]]
    r"""Tax rate status"""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
    subsidiaries: NotRequired[List[SubsidiariesModelTypedDict]]
    r"""The subsidiaries this belongs to."""


class TaxRateInput(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""ID assigned to identify this tax rate."""

    name: Optional[str] = None
    r"""Name assigned to identify this tax rate."""

    code: OptionalNullable[str] = UNSET
    r"""Tax code assigned to identify this tax rate."""

    description: OptionalNullable[str] = UNSET
    r"""Description of tax rate"""

    effective_tax_rate: OptionalNullable[float] = UNSET
    r"""Effective tax rate"""

    total_tax_rate: OptionalNullable[float] = UNSET
    r"""Not compounded sum of the components of a tax rate"""

    tax_payable_account_id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the account for tax collected."""

    tax_remitted_account_id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the account for tax remitted."""

    components: OptionalNullable[List[Components]] = UNSET

    type: OptionalNullable[str] = UNSET
    r"""Tax type used to indicate the source of tax collected or paid"""

    report_tax_type: OptionalNullable[str] = UNSET
    r"""Report Tax type to aggregate tax collected or paid for reporting purposes"""

    original_tax_rate_id: OptionalNullable[str] = UNSET
    r"""ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities."""

    status: OptionalNullable[TaxRateStatus] = UNSET
    r"""Tax rate status"""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    subsidiaries: Optional[List[SubsidiariesModel]] = None
    r"""The subsidiaries this belongs to."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "name",
            "code",
            "description",
            "effective_tax_rate",
            "total_tax_rate",
            "tax_payable_account_id",
            "tax_remitted_account_id",
            "components",
            "type",
            "report_tax_type",
            "original_tax_rate_id",
            "status",
            "row_version",
            "pass_through",
            "subsidiaries",
        ]
        nullable_fields = [
            "id",
            "code",
            "description",
            "effective_tax_rate",
            "total_tax_rate",
            "tax_payable_account_id",
            "tax_remitted_account_id",
            "components",
            "type",
            "report_tax_type",
            "original_tax_rate_id",
            "status",
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
