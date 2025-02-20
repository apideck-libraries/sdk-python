"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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
from .paymentstatus import PaymentStatus
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


class BillPaymentType(str, Enum):
    r"""Type of payment"""

    ACCOUNTS_PAYABLE_CREDIT = "accounts_payable_credit"
    ACCOUNTS_PAYABLE_OVERPAYMENT = "accounts_payable_overpayment"
    ACCOUNTS_PAYABLE_PREPAYMENT = "accounts_payable_prepayment"
    ACCOUNTS_PAYABLE = "accounts_payable"


class BillPaymentAllocationType(str, Enum):
    r"""Type of entity this payment should be attributed to."""

    BILL = "bill"
    EXPENSE = "expense"
    CREDIT_MEMO = "credit_memo"
    OVER_PAYMENT = "over_payment"
    PRE_PAYMENT = "pre_payment"
    JOURNAL_ENTRY = "journal_entry"
    OTHER = "other"


class AllocationsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    type: NotRequired[BillPaymentAllocationType]
    r"""Type of entity this payment should be attributed to."""
    code: NotRequired[str]
    amount: NotRequired[Nullable[float]]
    r"""Amount of payment that should be attributed to this allocation. If null, the total_amount will be used."""
    allocation_id: NotRequired[str]
    r"""Unique identifier of the allocation"""


class Allocations(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    type: Optional[BillPaymentAllocationType] = None
    r"""Type of entity this payment should be attributed to."""

    code: Optional[str] = None

    amount: OptionalNullable[float] = UNSET
    r"""Amount of payment that should be attributed to this allocation. If null, the total_amount will be used."""

    allocation_id: Optional[str] = None
    r"""Unique identifier of the allocation"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type", "code", "amount", "allocation_id"]
        nullable_fields = ["id", "amount"]
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


class BillPaymentTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    total_amount: Nullable[float]
    r"""The total amount of the transaction"""
    transaction_date: Nullable[datetime]
    r"""The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD"""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    reference: NotRequired[Nullable[str]]
    r"""Optional transaction reference message ie: Debit remittance detail."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    payment_method_reference: NotRequired[Nullable[str]]
    r"""Optional reference message returned by payment method on processing"""
    payment_method_id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    supplier: NotRequired[Nullable[LinkedSupplierTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    reconciled: NotRequired[Nullable[bool]]
    r"""Indicates if the transaction has been reconciled."""
    status: NotRequired[PaymentStatus]
    r"""Status of payment"""
    type: NotRequired[BillPaymentType]
    r"""Type of payment"""
    allocations: NotRequired[List[AllocationsTypedDict]]
    note: NotRequired[Nullable[str]]
    r"""Note associated with the transaction"""
    number: NotRequired[Nullable[str]]
    r"""Number associated with the transaction"""
    tracking_categories: NotRequired[
        Nullable[List[Nullable[LinkedTrackingCategoryTypedDict]]]
    ]
    r"""A list of linked tracking categories."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    display_id: NotRequired[Nullable[str]]
    r"""Id to be displayed."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class BillPayment(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    total_amount: Nullable[float]
    r"""The total amount of the transaction"""

    transaction_date: Nullable[datetime]
    r"""The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD"""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional transaction reference message ie: Debit remittance detail."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    payment_method_reference: OptionalNullable[str] = UNSET
    r"""Optional reference message returned by payment method on processing"""

    payment_method_id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    account: OptionalNullable[LinkedLedgerAccount] = UNSET

    supplier: OptionalNullable[LinkedSupplier] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    reconciled: OptionalNullable[bool] = UNSET
    r"""Indicates if the transaction has been reconciled."""

    status: Optional[PaymentStatus] = None
    r"""Status of payment"""

    type: Optional[BillPaymentType] = None
    r"""Type of payment"""

    allocations: Optional[List[Allocations]] = None

    note: OptionalNullable[str] = UNSET
    r"""Note associated with the transaction"""

    number: OptionalNullable[str] = UNSET
    r"""Number associated with the transaction"""

    tracking_categories: OptionalNullable[List[Nullable[LinkedTrackingCategory]]] = (
        UNSET
    )
    r"""A list of linked tracking categories."""

    custom_fields: Optional[List[CustomField]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    display_id: OptionalNullable[str] = UNSET
    r"""Id to be displayed."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "downstream_id",
            "currency",
            "currency_rate",
            "reference",
            "payment_method",
            "payment_method_reference",
            "payment_method_id",
            "account",
            "supplier",
            "company_id",
            "reconciled",
            "status",
            "type",
            "allocations",
            "note",
            "number",
            "tracking_categories",
            "custom_fields",
            "row_version",
            "display_id",
            "custom_mappings",
            "updated_by",
            "created_by",
            "created_at",
            "updated_at",
            "pass_through",
        ]
        nullable_fields = [
            "total_amount",
            "transaction_date",
            "downstream_id",
            "currency",
            "currency_rate",
            "reference",
            "payment_method",
            "payment_method_reference",
            "payment_method_id",
            "account",
            "supplier",
            "company_id",
            "reconciled",
            "note",
            "number",
            "tracking_categories",
            "row_version",
            "display_id",
            "custom_mappings",
            "updated_by",
            "created_by",
            "created_at",
            "updated_at",
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


class BillPaymentAllocationsTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    type: NotRequired[BillPaymentAllocationType]
    r"""Type of entity this payment should be attributed to."""
    amount: NotRequired[Nullable[float]]
    r"""Amount of payment that should be attributed to this allocation. If null, the total_amount will be used."""
    allocation_id: NotRequired[str]
    r"""Unique identifier of the allocation"""


class BillPaymentAllocations(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    type: Optional[BillPaymentAllocationType] = None
    r"""Type of entity this payment should be attributed to."""

    amount: OptionalNullable[float] = UNSET
    r"""Amount of payment that should be attributed to this allocation. If null, the total_amount will be used."""

    allocation_id: Optional[str] = None
    r"""Unique identifier of the allocation"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type", "amount", "allocation_id"]
        nullable_fields = ["id", "amount"]
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


class BillPaymentInputTypedDict(TypedDict):
    total_amount: Nullable[float]
    r"""The total amount of the transaction"""
    transaction_date: Nullable[datetime]
    r"""The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    reference: NotRequired[Nullable[str]]
    r"""Optional transaction reference message ie: Debit remittance detail."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""
    payment_method_reference: NotRequired[Nullable[str]]
    r"""Optional reference message returned by payment method on processing"""
    payment_method_id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    supplier: NotRequired[Nullable[LinkedSupplierInputTypedDict]]
    r"""The supplier this entity is linked to."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    reconciled: NotRequired[Nullable[bool]]
    r"""Indicates if the transaction has been reconciled."""
    status: NotRequired[PaymentStatus]
    r"""Status of payment"""
    type: NotRequired[BillPaymentType]
    r"""Type of payment"""
    allocations: NotRequired[List[BillPaymentAllocationsTypedDict]]
    note: NotRequired[Nullable[str]]
    r"""Note associated with the transaction"""
    number: NotRequired[Nullable[str]]
    r"""Number associated with the transaction"""
    tracking_categories: NotRequired[
        Nullable[List[Nullable[LinkedTrackingCategoryTypedDict]]]
    ]
    r"""A list of linked tracking categories."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    display_id: NotRequired[Nullable[str]]
    r"""Id to be displayed."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class BillPaymentInput(BaseModel):
    total_amount: Nullable[float]
    r"""The total amount of the transaction"""

    transaction_date: Nullable[datetime]
    r"""The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    reference: OptionalNullable[str] = UNSET
    r"""Optional transaction reference message ie: Debit remittance detail."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for the transaction, such as cash, credit card, bank transfer, or check"""

    payment_method_reference: OptionalNullable[str] = UNSET
    r"""Optional reference message returned by payment method on processing"""

    payment_method_id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    supplier: OptionalNullable[LinkedSupplierInput] = UNSET
    r"""The supplier this entity is linked to."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    reconciled: OptionalNullable[bool] = UNSET
    r"""Indicates if the transaction has been reconciled."""

    status: Optional[PaymentStatus] = None
    r"""Status of payment"""

    type: Optional[BillPaymentType] = None
    r"""Type of payment"""

    allocations: Optional[List[BillPaymentAllocations]] = None

    note: OptionalNullable[str] = UNSET
    r"""Note associated with the transaction"""

    number: OptionalNullable[str] = UNSET
    r"""Number associated with the transaction"""

    tracking_categories: OptionalNullable[List[Nullable[LinkedTrackingCategory]]] = (
        UNSET
    )
    r"""A list of linked tracking categories."""

    custom_fields: Optional[List[CustomField]] = None

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    display_id: OptionalNullable[str] = UNSET
    r"""Id to be displayed."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "currency",
            "currency_rate",
            "reference",
            "payment_method",
            "payment_method_reference",
            "payment_method_id",
            "account",
            "supplier",
            "company_id",
            "reconciled",
            "status",
            "type",
            "allocations",
            "note",
            "number",
            "tracking_categories",
            "custom_fields",
            "row_version",
            "display_id",
            "pass_through",
        ]
        nullable_fields = [
            "total_amount",
            "transaction_date",
            "currency",
            "currency_rate",
            "reference",
            "payment_method",
            "payment_method_reference",
            "payment_method_id",
            "account",
            "supplier",
            "company_id",
            "reconciled",
            "note",
            "number",
            "tracking_categories",
            "row_version",
            "display_id",
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
