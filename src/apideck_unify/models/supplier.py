"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .bankaccount import BankAccount, BankAccountTypedDict
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .email import Email, EmailTypedDict
from .linkedledgeraccount import LinkedLedgerAccount, LinkedLedgerAccountTypedDict
from .linkedledgeraccount_input import (
    LinkedLedgerAccountInput,
    LinkedLedgerAccountInputTypedDict,
)
from .linkedtaxrate import LinkedTaxRate, LinkedTaxRateTypedDict
from .linkedtaxrate_input import LinkedTaxRateInput, LinkedTaxRateInputTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from .website import Website, WebsiteTypedDict
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
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class SupplierStatus(str, Enum):
    r"""Supplier status"""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
    GDPR_ERASURE_REQUEST = "gdpr-erasure-request"
    UNKNOWN = "unknown"


class SupplierTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    display_id: NotRequired[Nullable[str]]
    r"""Display ID"""
    display_name: NotRequired[Nullable[str]]
    r"""Display name"""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    supplier_category: NotRequired[Nullable[str]]
    r"""The category/type of the supplier"""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the person."""
    middle_name: NotRequired[Nullable[str]]
    r"""Middle name of the person."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the person."""
    suffix: NotRequired[Nullable[str]]
    individual: NotRequired[Nullable[bool]]
    r"""Is this an individual or business supplier"""
    addresses: NotRequired[List[AddressTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    emails: NotRequired[List[EmailTypedDict]]
    websites: NotRequired[List[WebsiteTypedDict]]
    bank_accounts: NotRequired[List[BankAccountTypedDict]]
    notes: NotRequired[Nullable[str]]
    r"""Some notes about this supplier"""
    tax_rate: NotRequired[LinkedTaxRateTypedDict]
    tax_number: NotRequired[Nullable[str]]
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    status: NotRequired[Nullable[SupplierStatus]]
    r"""Supplier status"""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    custom_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
    subsidiary_id: NotRequired[str]
    r"""The subsidiary the supplier belongs to."""


class Supplier(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    display_id: OptionalNullable[str] = UNSET
    r"""Display ID"""

    display_name: OptionalNullable[str] = UNSET
    r"""Display name"""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    supplier_category: OptionalNullable[str] = UNSET
    r"""The category/type of the supplier"""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the person."""

    middle_name: OptionalNullable[str] = UNSET
    r"""Middle name of the person."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the person."""

    suffix: OptionalNullable[str] = UNSET

    individual: OptionalNullable[bool] = UNSET
    r"""Is this an individual or business supplier"""

    addresses: Optional[List[Address]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    emails: Optional[List[Email]] = None

    websites: Optional[List[Website]] = None

    bank_accounts: Optional[List[BankAccount]] = None

    notes: OptionalNullable[str] = UNSET
    r"""Some notes about this supplier"""

    tax_rate: Optional[LinkedTaxRate] = None

    tax_number: OptionalNullable[str] = UNSET

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    account: OptionalNullable[LinkedLedgerAccount] = UNSET

    status: OptionalNullable[SupplierStatus] = UNSET
    r"""Supplier status"""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    custom_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    custom_fields: Optional[List[CustomField]] = None

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    subsidiary_id: Optional[str] = None
    r"""The subsidiary the supplier belongs to."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "downstream_id",
            "display_id",
            "display_name",
            "company_name",
            "company_id",
            "supplier_category",
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "individual",
            "addresses",
            "phone_numbers",
            "emails",
            "websites",
            "bank_accounts",
            "notes",
            "tax_rate",
            "tax_number",
            "currency",
            "account",
            "status",
            "payment_method",
            "terms",
            "channel",
            "custom_mappings",
            "custom_fields",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "row_version",
            "pass_through",
            "subsidiary_id",
        ]
        nullable_fields = [
            "downstream_id",
            "display_id",
            "display_name",
            "company_name",
            "company_id",
            "supplier_category",
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "individual",
            "notes",
            "tax_number",
            "currency",
            "account",
            "status",
            "payment_method",
            "terms",
            "channel",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "row_version",
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


class SupplierInputTypedDict(TypedDict):
    display_id: NotRequired[Nullable[str]]
    r"""Display ID"""
    display_name: NotRequired[Nullable[str]]
    r"""Display name"""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    supplier_category: NotRequired[Nullable[str]]
    r"""The category/type of the supplier"""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the person."""
    middle_name: NotRequired[Nullable[str]]
    r"""Middle name of the person."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the person."""
    suffix: NotRequired[Nullable[str]]
    individual: NotRequired[Nullable[bool]]
    r"""Is this an individual or business supplier"""
    addresses: NotRequired[List[AddressTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    emails: NotRequired[List[EmailTypedDict]]
    websites: NotRequired[List[WebsiteTypedDict]]
    bank_accounts: NotRequired[List[BankAccountTypedDict]]
    notes: NotRequired[Nullable[str]]
    r"""Some notes about this supplier"""
    tax_rate: NotRequired[LinkedTaxRateInputTypedDict]
    tax_number: NotRequired[Nullable[str]]
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    status: NotRequired[Nullable[SupplierStatus]]
    r"""Supplier status"""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
    subsidiary_id: NotRequired[str]
    r"""The subsidiary the supplier belongs to."""


class SupplierInput(BaseModel):
    display_id: OptionalNullable[str] = UNSET
    r"""Display ID"""

    display_name: OptionalNullable[str] = UNSET
    r"""Display name"""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    supplier_category: OptionalNullable[str] = UNSET
    r"""The category/type of the supplier"""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the person."""

    middle_name: OptionalNullable[str] = UNSET
    r"""Middle name of the person."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the person."""

    suffix: OptionalNullable[str] = UNSET

    individual: OptionalNullable[bool] = UNSET
    r"""Is this an individual or business supplier"""

    addresses: Optional[List[Address]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    emails: Optional[List[Email]] = None

    websites: Optional[List[Website]] = None

    bank_accounts: Optional[List[BankAccount]] = None

    notes: OptionalNullable[str] = UNSET
    r"""Some notes about this supplier"""

    tax_rate: Optional[LinkedTaxRateInput] = None

    tax_number: OptionalNullable[str] = UNSET

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    status: OptionalNullable[SupplierStatus] = UNSET
    r"""Supplier status"""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    custom_fields: Optional[List[CustomField]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    subsidiary_id: Optional[str] = None
    r"""The subsidiary the supplier belongs to."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "display_id",
            "display_name",
            "company_name",
            "company_id",
            "supplier_category",
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "individual",
            "addresses",
            "phone_numbers",
            "emails",
            "websites",
            "bank_accounts",
            "notes",
            "tax_rate",
            "tax_number",
            "currency",
            "account",
            "status",
            "payment_method",
            "terms",
            "channel",
            "custom_fields",
            "row_version",
            "pass_through",
            "subsidiary_id",
        ]
        nullable_fields = [
            "display_id",
            "display_name",
            "company_name",
            "company_id",
            "supplier_category",
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "individual",
            "notes",
            "tax_number",
            "currency",
            "account",
            "status",
            "payment_method",
            "terms",
            "channel",
            "row_version",
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
