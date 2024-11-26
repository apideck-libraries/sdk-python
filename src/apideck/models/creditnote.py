"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .allocation import (
    Allocation,
    AllocationInput,
    AllocationInputTypedDict,
    AllocationTypedDict,
)
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .invoicelineitem import (
    InvoiceLineItem,
    InvoiceLineItemInput,
    InvoiceLineItemInputTypedDict,
    InvoiceLineItemTypedDict,
)
from .linkedcustomer import LinkedCustomer, LinkedCustomerTypedDict
from .linkedcustomer_input import LinkedCustomerInput, LinkedCustomerInputTypedDict
from .linkedledgeraccount import LinkedLedgerAccount, LinkedLedgerAccountTypedDict
from .linkedledgeraccount_input import (
    LinkedLedgerAccountInput,
    LinkedLedgerAccountInputTypedDict,
)
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class CreditNoteStatus(str, Enum):
    r"""Status of credit notes"""

    DRAFT = "draft"
    AUTHORISED = "authorised"
    PAID = "paid"
    VOIDED = "voided"
    DELETED = "deleted"


class CreditNoteType(str, Enum):
    r"""Type of payment"""

    ACCOUNTS_RECEIVABLE_CREDIT = "accounts_receivable_credit"
    ACCOUNTS_PAYABLE_CREDIT = "accounts_payable_credit"


class CreditNoteTypedDict(TypedDict):
    id: str
    r"""Unique identifier representing the entity"""
    total_amount: float
    r"""Amount of transaction"""
    number: NotRequired[Nullable[str]]
    r"""Credit note number."""
    customer: NotRequired[Nullable[LinkedCustomerTypedDict]]
    r"""The customer this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    balance: NotRequired[Nullable[float]]
    r"""The balance reflecting any payments made against the transaction."""
    remaining_credit: NotRequired[Nullable[float]]
    r"""Indicates the total credit amount still available to apply towards the payment."""
    status: NotRequired[CreditNoteStatus]
    r"""Status of credit notes"""
    reference: NotRequired[Nullable[str]]
    r"""Optional reference message ie: Debit remittance detail."""
    date_issued: NotRequired[datetime]
    r"""Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD"""
    date_paid: NotRequired[Nullable[datetime]]
    r"""Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD"""
    type: NotRequired[CreditNoteType]
    r"""Type of payment"""
    account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    line_items: NotRequired[List[InvoiceLineItemTypedDict]]
    allocations: NotRequired[List[AllocationTypedDict]]
    note: NotRequired[Nullable[str]]
    r"""Optional note to be associated with the credit note."""
    terms: NotRequired[Nullable[str]]
    r"""Optional terms to be associated with the credit note."""
    billing_address: NotRequired[AddressTypedDict]
    shipping_address: NotRequired[AddressTypedDict]
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
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


class CreditNote(BaseModel):
    id: str
    r"""Unique identifier representing the entity"""

    total_amount: float
    r"""Amount of transaction"""

    number: OptionalNullable[str] = UNSET
    r"""Credit note number."""

    customer: OptionalNullable[LinkedCustomer] = UNSET
    r"""The customer this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    balance: OptionalNullable[float] = UNSET
    r"""The balance reflecting any payments made against the transaction."""

    remaining_credit: OptionalNullable[float] = UNSET
    r"""Indicates the total credit amount still available to apply towards the payment."""

    status: Optional[CreditNoteStatus] = None
    r"""Status of credit notes"""

    reference: OptionalNullable[str] = UNSET
    r"""Optional reference message ie: Debit remittance detail."""

    date_issued: Optional[datetime] = None
    r"""Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD"""

    date_paid: OptionalNullable[datetime] = UNSET
    r"""Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD"""

    type: Optional[CreditNoteType] = None
    r"""Type of payment"""

    account: OptionalNullable[LinkedLedgerAccount] = UNSET

    line_items: Optional[List[InvoiceLineItem]] = None

    allocations: Optional[List[Allocation]] = None

    note: OptionalNullable[str] = UNSET
    r"""Optional note to be associated with the credit note."""

    terms: OptionalNullable[str] = UNSET
    r"""Optional terms to be associated with the credit note."""

    billing_address: Optional[Address] = None

    shipping_address: Optional[Address] = None

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    custom_fields: Optional[List[CustomField]] = None

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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "number",
            "customer",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "balance",
            "remaining_credit",
            "status",
            "reference",
            "date_issued",
            "date_paid",
            "type",
            "account",
            "line_items",
            "allocations",
            "note",
            "terms",
            "billing_address",
            "shipping_address",
            "tracking_categories",
            "custom_mappings",
            "custom_fields",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "number",
            "customer",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "balance",
            "remaining_credit",
            "reference",
            "date_paid",
            "account",
            "note",
            "terms",
            "tracking_categories",
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


class CreditNoteInputTypedDict(TypedDict):
    total_amount: float
    r"""Amount of transaction"""
    number: NotRequired[Nullable[str]]
    r"""Credit note number."""
    customer: NotRequired[Nullable[LinkedCustomerInputTypedDict]]
    r"""The customer this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    balance: NotRequired[Nullable[float]]
    r"""The balance reflecting any payments made against the transaction."""
    remaining_credit: NotRequired[Nullable[float]]
    r"""Indicates the total credit amount still available to apply towards the payment."""
    status: NotRequired[CreditNoteStatus]
    r"""Status of credit notes"""
    reference: NotRequired[Nullable[str]]
    r"""Optional reference message ie: Debit remittance detail."""
    date_issued: NotRequired[datetime]
    r"""Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD"""
    date_paid: NotRequired[Nullable[datetime]]
    r"""Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD"""
    type: NotRequired[CreditNoteType]
    r"""Type of payment"""
    account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    line_items: NotRequired[List[InvoiceLineItemInputTypedDict]]
    allocations: NotRequired[List[AllocationInputTypedDict]]
    note: NotRequired[Nullable[str]]
    r"""Optional note to be associated with the credit note."""
    terms: NotRequired[Nullable[str]]
    r"""Optional terms to be associated with the credit note."""
    billing_address: NotRequired[AddressTypedDict]
    shipping_address: NotRequired[AddressTypedDict]
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class CreditNoteInput(BaseModel):
    total_amount: float
    r"""Amount of transaction"""

    number: OptionalNullable[str] = UNSET
    r"""Credit note number."""

    customer: OptionalNullable[LinkedCustomerInput] = UNSET
    r"""The customer this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    balance: OptionalNullable[float] = UNSET
    r"""The balance reflecting any payments made against the transaction."""

    remaining_credit: OptionalNullable[float] = UNSET
    r"""Indicates the total credit amount still available to apply towards the payment."""

    status: Optional[CreditNoteStatus] = None
    r"""Status of credit notes"""

    reference: OptionalNullable[str] = UNSET
    r"""Optional reference message ie: Debit remittance detail."""

    date_issued: Optional[datetime] = None
    r"""Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD"""

    date_paid: OptionalNullable[datetime] = UNSET
    r"""Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD"""

    type: Optional[CreditNoteType] = None
    r"""Type of payment"""

    account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    line_items: Optional[List[InvoiceLineItemInput]] = None

    allocations: Optional[List[AllocationInput]] = None

    note: OptionalNullable[str] = UNSET
    r"""Optional note to be associated with the credit note."""

    terms: OptionalNullable[str] = UNSET
    r"""Optional terms to be associated with the credit note."""

    billing_address: Optional[Address] = None

    shipping_address: Optional[Address] = None

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    custom_fields: Optional[List[CustomField]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "number",
            "customer",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "balance",
            "remaining_credit",
            "status",
            "reference",
            "date_issued",
            "date_paid",
            "type",
            "account",
            "line_items",
            "allocations",
            "note",
            "terms",
            "billing_address",
            "shipping_address",
            "tracking_categories",
            "custom_fields",
            "row_version",
            "pass_through",
        ]
        nullable_fields = [
            "number",
            "customer",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "sub_total",
            "total_tax",
            "tax_code",
            "balance",
            "remaining_credit",
            "reference",
            "date_paid",
            "account",
            "note",
            "terms",
            "tracking_categories",
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