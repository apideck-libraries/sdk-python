"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccount import BankAccount, BankAccountTypedDict
from .billlineitem import (
    BillLineItem,
    BillLineItemInput,
    BillLineItemInputTypedDict,
    BillLineItemTypedDict,
)
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .linkedledgeraccount import LinkedLedgerAccount, LinkedLedgerAccountTypedDict
from .linkedledgeraccount_input import (
    LinkedLedgerAccountInput,
    LinkedLedgerAccountInputTypedDict,
)
from .linkedsupplier import LinkedSupplier, LinkedSupplierTypedDict
from .linkedsupplier_input import LinkedSupplierInput, LinkedSupplierInputTypedDict
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
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
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BillStatus(str, Enum):
    r"""Invoice status"""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    AUTHORISED = "authorised"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    VOID = "void"
    CREDIT = "credit"
    DELETED = "deleted"


class BillTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    bill_number: NotRequired[Nullable[str]]
    r"""Reference to supplier bill number"""
    supplier: NotRequired[Nullable[LinkedSupplierTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    bill_date: NotRequired[Nullable[date]]
    r"""Date bill was issued - YYYY-MM-DD."""
    due_date: NotRequired[Nullable[date]]
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""
    paid_date: NotRequired[Nullable[date]]
    r"""The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD."""
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""
    reference: NotRequired[Nullable[str]]
    r"""Optional bill reference."""
    line_items: NotRequired[List[BillLineItemTypedDict]]
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    balance: NotRequired[Nullable[float]]
    r"""Balance of bill due."""
    deposit: NotRequired[Nullable[float]]
    r"""Amount of deposit made to this bill."""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this bill."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of bill, including tax."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    notes: NotRequired[Nullable[str]]
    status: NotRequired[Nullable[BillStatus]]
    r"""Invoice status"""
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    bank_account: NotRequired[BankAccountTypedDict]
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this transaction."""
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
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
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
    accounting_period: NotRequired[Nullable[str]]
    r"""Accounting period"""


class Bill(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    bill_number: OptionalNullable[str] = UNSET
    r"""Reference to supplier bill number"""

    supplier: OptionalNullable[LinkedSupplier] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    bill_date: OptionalNullable[date] = UNSET
    r"""Date bill was issued - YYYY-MM-DD."""

    due_date: OptionalNullable[date] = UNSET
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""

    paid_date: OptionalNullable[date] = UNSET
    r"""The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD."""

    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional bill reference."""

    line_items: Optional[List[BillLineItem]] = None

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    balance: OptionalNullable[float] = UNSET
    r"""Balance of bill due."""

    deposit: OptionalNullable[float] = UNSET
    r"""Amount of deposit made to this bill."""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this bill."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of bill, including tax."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    notes: OptionalNullable[str] = UNSET

    status: OptionalNullable[BillStatus] = UNSET
    r"""Invoice status"""

    ledger_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    bank_account: Optional[BankAccount] = None

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this transaction."""

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

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

    custom_fields: Optional[List[CustomField]] = None

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    accounting_period: OptionalNullable[str] = UNSET
    r"""Accounting period"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "downstream_id",
            "bill_number",
            "supplier",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "bill_date",
            "due_date",
            "paid_date",
            "po_number",
            "reference",
            "line_items",
            "terms",
            "balance",
            "deposit",
            "sub_total",
            "total_tax",
            "total",
            "tax_code",
            "notes",
            "status",
            "ledger_account",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "bank_account",
            "discount_percentage",
            "tracking_categories",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "row_version",
            "custom_fields",
            "custom_mappings",
            "pass_through",
            "accounting_period",
        ]
        nullable_fields = [
            "downstream_id",
            "bill_number",
            "supplier",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "bill_date",
            "due_date",
            "paid_date",
            "po_number",
            "reference",
            "terms",
            "balance",
            "deposit",
            "sub_total",
            "total_tax",
            "total",
            "tax_code",
            "notes",
            "status",
            "ledger_account",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "discount_percentage",
            "tracking_categories",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "row_version",
            "custom_mappings",
            "accounting_period",
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


class BillInputTypedDict(TypedDict):
    bill_number: NotRequired[Nullable[str]]
    r"""Reference to supplier bill number"""
    supplier: NotRequired[Nullable[LinkedSupplierInputTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    bill_date: NotRequired[Nullable[date]]
    r"""Date bill was issued - YYYY-MM-DD."""
    due_date: NotRequired[Nullable[date]]
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""
    paid_date: NotRequired[Nullable[date]]
    r"""The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD."""
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""
    reference: NotRequired[Nullable[str]]
    r"""Optional bill reference."""
    line_items: NotRequired[List[BillLineItemInputTypedDict]]
    terms: NotRequired[Nullable[str]]
    r"""Terms of payment."""
    balance: NotRequired[Nullable[float]]
    r"""Balance of bill due."""
    deposit: NotRequired[Nullable[float]]
    r"""Amount of deposit made to this bill."""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this bill."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of bill, including tax."""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    notes: NotRequired[Nullable[str]]
    status: NotRequired[Nullable[BillStatus]]
    r"""Invoice status"""
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    language: NotRequired[Nullable[str]]
    r"""language code according to ISO 639-1. For the United States - EN"""
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    bank_account: NotRequired[BankAccountTypedDict]
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this transaction."""
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
    accounting_period: NotRequired[Nullable[str]]
    r"""Accounting period"""


class BillInput(BaseModel):
    bill_number: OptionalNullable[str] = UNSET
    r"""Reference to supplier bill number"""

    supplier: OptionalNullable[LinkedSupplierInput] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    bill_date: OptionalNullable[date] = UNSET
    r"""Date bill was issued - YYYY-MM-DD."""

    due_date: OptionalNullable[date] = UNSET
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""

    paid_date: OptionalNullable[date] = UNSET
    r"""The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD."""

    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional bill reference."""

    line_items: Optional[List[BillLineItemInput]] = None

    terms: OptionalNullable[str] = UNSET
    r"""Terms of payment."""

    balance: OptionalNullable[float] = UNSET
    r"""Balance of bill due."""

    deposit: OptionalNullable[float] = UNSET
    r"""Amount of deposit made to this bill."""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this bill."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of bill, including tax."""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    notes: OptionalNullable[str] = UNSET

    status: OptionalNullable[BillStatus] = UNSET
    r"""Invoice status"""

    ledger_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    language: OptionalNullable[str] = UNSET
    r"""language code according to ISO 639-1. For the United States - EN"""

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    bank_account: Optional[BankAccount] = None

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this transaction."""

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    custom_fields: Optional[List[CustomField]] = None

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    accounting_period: OptionalNullable[str] = UNSET
    r"""Accounting period"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "bill_number",
            "supplier",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "bill_date",
            "due_date",
            "paid_date",
            "po_number",
            "reference",
            "line_items",
            "terms",
            "balance",
            "deposit",
            "sub_total",
            "total_tax",
            "total",
            "tax_code",
            "notes",
            "status",
            "ledger_account",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "bank_account",
            "discount_percentage",
            "tracking_categories",
            "row_version",
            "custom_fields",
            "pass_through",
            "accounting_period",
        ]
        nullable_fields = [
            "bill_number",
            "supplier",
            "company_id",
            "currency",
            "currency_rate",
            "tax_inclusive",
            "bill_date",
            "due_date",
            "paid_date",
            "po_number",
            "reference",
            "terms",
            "balance",
            "deposit",
            "sub_total",
            "total_tax",
            "total",
            "tax_code",
            "notes",
            "status",
            "ledger_account",
            "payment_method",
            "channel",
            "language",
            "accounting_by_row",
            "discount_percentage",
            "tracking_categories",
            "row_version",
            "accounting_period",
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
