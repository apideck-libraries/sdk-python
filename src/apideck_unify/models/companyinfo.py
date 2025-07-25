"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .currency import Currency
from .email import Email, EmailTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from .taxrate import TaxRate, TaxRateTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import date, datetime
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class CompanyStatus(str, Enum):
    r"""Based on the status some functionality is enabled or disabled."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class TheStartMonthOfFiscalYear(str, Enum):
    r"""The start month of fiscal year."""

    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"


class CompanyInfoTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    status: NotRequired[CompanyStatus]
    r"""Based on the status some functionality is enabled or disabled."""
    legal_name: NotRequired[str]
    r"""The legal name of the company"""
    country: NotRequired[Nullable[str]]
    r"""country code according to ISO 3166-1 alpha-2."""
    sales_tax_number: NotRequired[Nullable[str]]
    automated_sales_tax: NotRequired[bool]
    r"""Whether sales tax is calculated automatically for the company"""
    sales_tax_enabled: NotRequired[bool]
    r"""Whether sales tax is enabled for the company"""
    default_sales_tax: NotRequired[TaxRateTypedDict]
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    fiscal_year_start_month: NotRequired[TheStartMonthOfFiscalYear]
    r"""The start month of fiscal year."""
    company_start_date: NotRequired[date]
    r"""Date when company file was created"""
    addresses: NotRequired[List[AddressTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    emails: NotRequired[List[EmailTypedDict]]
    custom_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    tracking_categories_enabled: NotRequired[bool]
    r"""Whether tracking categories are enabled for the company on transactions"""
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


class CompanyInfo(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    status: Optional[CompanyStatus] = None
    r"""Based on the status some functionality is enabled or disabled."""

    legal_name: Optional[str] = None
    r"""The legal name of the company"""

    country: OptionalNullable[str] = UNSET
    r"""country code according to ISO 3166-1 alpha-2."""

    sales_tax_number: OptionalNullable[str] = UNSET

    automated_sales_tax: Optional[bool] = None
    r"""Whether sales tax is calculated automatically for the company"""

    sales_tax_enabled: Optional[bool] = None
    r"""Whether sales tax is enabled for the company"""

    default_sales_tax: Optional[TaxRate] = None

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    fiscal_year_start_month: Optional[TheStartMonthOfFiscalYear] = None
    r"""The start month of fiscal year."""

    company_start_date: Optional[date] = None
    r"""Date when company file was created"""

    addresses: Optional[List[Address]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    emails: Optional[List[Email]] = None

    custom_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    tracking_categories_enabled: Optional[bool] = None
    r"""Whether tracking categories are enabled for the company on transactions"""

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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "company_name",
            "status",
            "legal_name",
            "country",
            "sales_tax_number",
            "automated_sales_tax",
            "sales_tax_enabled",
            "default_sales_tax",
            "currency",
            "language",
            "fiscal_year_start_month",
            "company_start_date",
            "addresses",
            "phone_numbers",
            "emails",
            "custom_mappings",
            "tracking_categories_enabled",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
        ]
        nullable_fields = [
            "company_name",
            "country",
            "sales_tax_number",
            "currency",
            "language",
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
