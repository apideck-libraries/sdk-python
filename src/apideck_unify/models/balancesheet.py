"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from .custommappings import CustomMappings, CustomMappingsTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import Any, List, Optional
from typing_extensions import NotRequired, TypedDict


class BalanceSheetAssetsAccountTypedDict(TypedDict):
    r"""A balance sheet assets account represents the financial position of a company at a specific point in time."""

    account_id: NotRequired[str]
    r"""The unique identifier for the account."""
    code: NotRequired[str]
    r"""The account code of the account"""
    name: NotRequired[str]
    r"""The name of the account."""
    value: NotRequired[float]
    r"""The amount or value of the item"""
    items: NotRequired[Any]
    r"""A list of balance sheet accounts"""


class BalanceSheetAssetsAccount(BaseModel):
    r"""A balance sheet assets account represents the financial position of a company at a specific point in time."""

    account_id: Optional[str] = None
    r"""The unique identifier for the account."""

    code: Optional[str] = None
    r"""The account code of the account"""

    name: Optional[str] = None
    r"""The name of the account."""

    value: Optional[float] = None
    r"""The amount or value of the item"""

    items: Optional[Any] = None
    r"""A list of balance sheet accounts"""


class BalanceSheetLiabilitiesAccountTypedDict(TypedDict):
    r"""A balance sheet liabilities account represents the financial position of a company at a specific point in time."""

    account_id: NotRequired[str]
    r"""The unique identifier for the account."""
    code: NotRequired[str]
    r"""The account code of the account"""
    name: NotRequired[str]
    r"""The name of the account."""
    value: NotRequired[float]
    r"""The amount or value of the item"""
    items: NotRequired[Any]
    r"""A list of balance sheet accounts"""


class BalanceSheetLiabilitiesAccount(BaseModel):
    r"""A balance sheet liabilities account represents the financial position of a company at a specific point in time."""

    account_id: Optional[str] = None
    r"""The unique identifier for the account."""

    code: Optional[str] = None
    r"""The account code of the account"""

    name: Optional[str] = None
    r"""The name of the account."""

    value: Optional[float] = None
    r"""The amount or value of the item"""

    items: Optional[Any] = None
    r"""A list of balance sheet accounts"""


class BalanceSheetEquityAccountTypedDict(TypedDict):
    r"""A balance sheet equity account represents the financial position of a company at a specific point in time."""

    account_id: NotRequired[str]
    r"""The unique identifier for the account."""
    code: NotRequired[str]
    r"""The account code of the account"""
    name: NotRequired[str]
    r"""The name of the account."""
    value: NotRequired[float]
    r"""The amount or value of the item"""
    items: NotRequired[Any]
    r"""A list of balance sheet accounts"""


class BalanceSheetEquityAccount(BaseModel):
    r"""A balance sheet equity account represents the financial position of a company at a specific point in time."""

    account_id: Optional[str] = None
    r"""The unique identifier for the account."""

    code: Optional[str] = None
    r"""The account code of the account"""

    name: Optional[str] = None
    r"""The name of the account."""

    value: Optional[float] = None
    r"""The amount or value of the item"""

    items: Optional[Any] = None
    r"""A list of balance sheet accounts"""


class BalanceSheetUncategorizedItemsAccountTypedDict(TypedDict):
    r"""A balance sheet uncategorized items account represents the financial position of a company at a specific point in time."""

    account_id: NotRequired[str]
    r"""The unique identifier for the account."""
    code: NotRequired[str]
    r"""The account code of the account"""
    name: NotRequired[str]
    r"""The name of the account."""
    value: NotRequired[float]
    r"""The amount or value of the item"""
    items: NotRequired[Any]
    r"""A list of balance sheet accounts"""


class BalanceSheetUncategorizedItemsAccount(BaseModel):
    r"""A balance sheet uncategorized items account represents the financial position of a company at a specific point in time."""

    account_id: Optional[str] = None
    r"""The unique identifier for the account."""

    code: Optional[str] = None
    r"""The account code of the account"""

    name: Optional[str] = None
    r"""The name of the account."""

    value: Optional[float] = None
    r"""The amount or value of the item"""

    items: Optional[Any] = None
    r"""A list of balance sheet accounts"""


class ReportsTypedDict(TypedDict):
    end_date: str
    r"""The start date of the report"""
    assets: BalanceSheetAssetsAccountTypedDict
    r"""A balance sheet assets account represents the financial position of a company at a specific point in time."""
    liabilities: BalanceSheetLiabilitiesAccountTypedDict
    r"""A balance sheet liabilities account represents the financial position of a company at a specific point in time."""
    equity: BalanceSheetEquityAccountTypedDict
    r"""A balance sheet equity account represents the financial position of a company at a specific point in time."""
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    report_name: NotRequired[str]
    r"""The name of the report"""
    start_date: NotRequired[str]
    r"""The start date of the report"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    net_assets: NotRequired[float]
    r"""The net assets of the balance sheet"""
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
    uncategorized_items: NotRequired[BalanceSheetUncategorizedItemsAccountTypedDict]
    r"""A balance sheet uncategorized items account represents the financial position of a company at a specific point in time."""


class Reports(BaseModel):
    end_date: str
    r"""The start date of the report"""

    assets: BalanceSheetAssetsAccount
    r"""A balance sheet assets account represents the financial position of a company at a specific point in time."""

    liabilities: BalanceSheetLiabilitiesAccount
    r"""A balance sheet liabilities account represents the financial position of a company at a specific point in time."""

    equity: BalanceSheetEquityAccount
    r"""A balance sheet equity account represents the financial position of a company at a specific point in time."""

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    report_name: Optional[str] = None
    r"""The name of the report"""

    start_date: Optional[str] = None
    r"""The start date of the report"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    net_assets: Optional[float] = None
    r"""The net assets of the balance sheet"""

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

    uncategorized_items: Optional[BalanceSheetUncategorizedItemsAccount] = None
    r"""A balance sheet uncategorized items account represents the financial position of a company at a specific point in time."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "report_name",
            "start_date",
            "currency",
            "net_assets",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "uncategorized_items",
        ]
        nullable_fields = [
            "currency",
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


class BalanceSheetTypedDict(TypedDict):
    reports: List[ReportsTypedDict]


class BalanceSheet(BaseModel):
    reports: List[Reports]