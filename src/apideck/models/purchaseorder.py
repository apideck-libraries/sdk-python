"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .bankaccount import BankAccount, BankAccountTypedDict
from .currency import Currency
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .invoicelineitem import (
    InvoiceLineItem,
    InvoiceLineItemInput,
    InvoiceLineItemInputTypedDict,
    InvoiceLineItemTypedDict,
)
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
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from datetime import date, datetime
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PurchaseOrderStatus(str, Enum):
    DRAFT = "draft"
    OPEN = "open"
    CLOSED = "closed"
    DELETED = "deleted"
    BILLED = "billed"
    OTHER = "other"


class PurchaseOrderTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer."""
    reference: NotRequired[Nullable[str]]
    r"""Optional purchase order reference."""
    supplier: NotRequired[Nullable[LinkedSupplierTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    status: NotRequired[Nullable[PurchaseOrderStatus]]
    issued_date: NotRequired[Nullable[date]]
    r"""Date purchase order was issued - YYYY-MM-DD."""
    delivery_date: NotRequired[Nullable[date]]
    r"""The date on which the purchase order is to be delivered - YYYY-MM-DD."""
    expected_arrival_date: NotRequired[Nullable[date]]
    r"""The date on which the order is expected to arrive - YYYY-MM-DD."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of invoice, including tax."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    line_items: NotRequired[List[InvoiceLineItemTypedDict]]
    shipping_address: NotRequired[AddressTypedDict]
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    template_id: NotRequired[Nullable[str]]
    r"""Optional purchase order template"""
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this transaction."""
    bank_account: NotRequired[BankAccountTypedDict]
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    due_date: NotRequired[date]
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    memo: NotRequired[Nullable[str]]
    r"""Message for the supplier. This text appears on the Purchase Order."""
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
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


class PurchaseOrder(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional purchase order reference."""

    supplier: OptionalNullable[LinkedSupplier] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    status: OptionalNullable[PurchaseOrderStatus] = UNSET

    issued_date: OptionalNullable[date] = UNSET
    r"""Date purchase order was issued - YYYY-MM-DD."""

    delivery_date: OptionalNullable[date] = UNSET
    r"""The date on which the purchase order is to be delivered - YYYY-MM-DD."""

    expected_arrival_date: OptionalNullable[date] = UNSET
    r"""The date on which the order is expected to arrive - YYYY-MM-DD."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of invoice, including tax."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    line_items: Optional[List[InvoiceLineItem]] = None

    shipping_address: Optional[Address] = None

    ledger_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    template_id: OptionalNullable[str] = UNSET
    r"""Optional purchase order template"""

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this transaction."""

    bank_account: Optional[BankAccount] = None

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    due_date: Optional[date] = None
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    memo: OptionalNullable[str] = UNSET
    r"""Message for the supplier. This text appears on the Purchase Order."""

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "downstream_id",
            "po_number",
            "reference",
            "supplier",
            "company_id",
            "status",
            "issued_date",
            "delivery_date",
            "expected_arrival_date",
            "currency",
            "currency_rate",
            "sub_total",
            "total_tax",
            "total",
            "tax_inclusive",
            "line_items",
            "shipping_address",
            "ledger_account",
            "template_id",
            "discount_percentage",
            "bank_account",
            "accounting_by_row",
            "due_date",
            "payment_method",
            "tax_code",
            "channel",
            "memo",
            "tracking_categories",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "downstream_id",
            "po_number",
            "reference",
            "supplier",
            "company_id",
            "status",
            "issued_date",
            "delivery_date",
            "expected_arrival_date",
            "currency",
            "currency_rate",
            "sub_total",
            "total_tax",
            "total",
            "tax_inclusive",
            "ledger_account",
            "template_id",
            "discount_percentage",
            "accounting_by_row",
            "payment_method",
            "tax_code",
            "channel",
            "memo",
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


class PurchaseOrderInputTypedDict(TypedDict):
    po_number: NotRequired[Nullable[str]]
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer."""
    reference: NotRequired[Nullable[str]]
    r"""Optional purchase order reference."""
    supplier: NotRequired[Nullable[LinkedSupplierInputTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    status: NotRequired[Nullable[PurchaseOrderStatus]]
    issued_date: NotRequired[Nullable[date]]
    r"""Date purchase order was issued - YYYY-MM-DD."""
    delivery_date: NotRequired[Nullable[date]]
    r"""The date on which the purchase order is to be delivered - YYYY-MM-DD."""
    expected_arrival_date: NotRequired[Nullable[date]]
    r"""The date on which the order is expected to arrive - YYYY-MM-DD."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    sub_total: NotRequired[Nullable[float]]
    r"""Sub-total amount, normally before tax."""
    total_tax: NotRequired[Nullable[float]]
    r"""Total tax amount applied to this invoice."""
    total: NotRequired[Nullable[float]]
    r"""Total amount of invoice, including tax."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    line_items: NotRequired[List[InvoiceLineItemInputTypedDict]]
    shipping_address: NotRequired[AddressTypedDict]
    ledger_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    template_id: NotRequired[Nullable[str]]
    r"""Optional purchase order template"""
    discount_percentage: NotRequired[Nullable[float]]
    r"""Discount percentage applied to this transaction."""
    bank_account: NotRequired[BankAccountTypedDict]
    accounting_by_row: NotRequired[Nullable[bool]]
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""
    due_date: NotRequired[date]
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    channel: NotRequired[Nullable[str]]
    r"""The channel through which the transaction is processed."""
    memo: NotRequired[Nullable[str]]
    r"""Message for the supplier. This text appears on the Purchase Order."""
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class PurchaseOrderInput(BaseModel):
    po_number: OptionalNullable[str] = UNSET
    r"""A PO Number uniquely identifies a purchase order and is generally defined by the buyer."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional purchase order reference."""

    supplier: OptionalNullable[LinkedSupplierInput] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    status: OptionalNullable[PurchaseOrderStatus] = UNSET

    issued_date: OptionalNullable[date] = UNSET
    r"""Date purchase order was issued - YYYY-MM-DD."""

    delivery_date: OptionalNullable[date] = UNSET
    r"""The date on which the purchase order is to be delivered - YYYY-MM-DD."""

    expected_arrival_date: OptionalNullable[date] = UNSET
    r"""The date on which the order is expected to arrive - YYYY-MM-DD."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    sub_total: OptionalNullable[float] = UNSET
    r"""Sub-total amount, normally before tax."""

    total_tax: OptionalNullable[float] = UNSET
    r"""Total tax amount applied to this invoice."""

    total: OptionalNullable[float] = UNSET
    r"""Total amount of invoice, including tax."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    line_items: Optional[List[InvoiceLineItemInput]] = None

    shipping_address: Optional[Address] = None

    ledger_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    template_id: OptionalNullable[str] = UNSET
    r"""Optional purchase order template"""

    discount_percentage: OptionalNullable[float] = UNSET
    r"""Discount percentage applied to this transaction."""

    bank_account: Optional[BankAccount] = None

    accounting_by_row: OptionalNullable[bool] = UNSET
    r"""Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row."""

    due_date: Optional[date] = None
    r"""The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    channel: OptionalNullable[str] = UNSET
    r"""The channel through which the transaction is processed."""

    memo: OptionalNullable[str] = UNSET
    r"""Message for the supplier. This text appears on the Purchase Order."""

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "po_number",
            "reference",
            "supplier",
            "company_id",
            "status",
            "issued_date",
            "delivery_date",
            "expected_arrival_date",
            "currency",
            "currency_rate",
            "sub_total",
            "total_tax",
            "total",
            "tax_inclusive",
            "line_items",
            "shipping_address",
            "ledger_account",
            "template_id",
            "discount_percentage",
            "bank_account",
            "accounting_by_row",
            "due_date",
            "payment_method",
            "tax_code",
            "channel",
            "memo",
            "tracking_categories",
            "row_version",
            "pass_through",
        ]
        nullable_fields = [
            "po_number",
            "reference",
            "supplier",
            "company_id",
            "status",
            "issued_date",
            "delivery_date",
            "expected_arrival_date",
            "currency",
            "currency_rate",
            "sub_total",
            "total_tax",
            "total",
            "tax_inclusive",
            "ledger_account",
            "template_id",
            "discount_percentage",
            "accounting_by_row",
            "payment_method",
            "tax_code",
            "channel",
            "memo",
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