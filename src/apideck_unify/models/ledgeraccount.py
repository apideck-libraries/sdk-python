"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccount import BankAccount, BankAccountTypedDict
from .currency import Currency
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .linkedtaxrate import LinkedTaxRate, LinkedTaxRateTypedDict
from .linkedtaxrate_input import LinkedTaxRateInput, LinkedTaxRateInputTypedDict
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
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Classification(str, Enum):
    r"""The classification of account."""

    ASSET = "asset"
    EQUITY = "equity"
    EXPENSE = "expense"
    LIABILITY = "liability"
    REVENUE = "revenue"
    INCOME = "income"
    OTHER_INCOME = "other_income"
    OTHER_EXPENSE = "other_expense"
    COSTS_OF_SALES = "costs_of_sales"
    OTHER = "other"


class LedgerAccountType(str, Enum):
    r"""The type of account."""

    ACCOUNTS_RECEIVABLE = "accounts_receivable"
    REVENUE = "revenue"
    SALES = "sales"
    OTHER_INCOME = "other_income"
    BANK = "bank"
    CURRENT_ASSET = "current_asset"
    FIXED_ASSET = "fixed_asset"
    NON_CURRENT_ASSET = "non_current_asset"
    OTHER_ASSET = "other_asset"
    BALANCESHEET = "balancesheet"
    EQUITY = "equity"
    EXPENSE = "expense"
    OTHER_EXPENSE = "other_expense"
    COSTS_OF_SALES = "costs_of_sales"
    ACCOUNTS_PAYABLE = "accounts_payable"
    CREDIT_CARD = "credit_card"
    CURRENT_LIABILITY = "current_liability"
    NON_CURRENT_LIABILITY = "non_current_liability"
    OTHER_LIABILITY = "other_liability"
    OTHER = "other"


class AccountStatus(str, Enum):
    r"""The status of the account."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class CategoriesTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    r"""The name of the category."""


class Categories(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None
    r"""The name of the category."""


class ParentAccountTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The ID of the parent account."""
    name: NotRequired[str]
    r"""The name of the parent account."""
    display_id: NotRequired[str]
    r"""The human readable display ID used when displaying the parent account"""


class ParentAccount(BaseModel):
    id: Optional[str] = None
    r"""The ID of the parent account."""

    name: Optional[str] = None
    r"""The name of the parent account."""

    display_id: Optional[str] = None
    r"""The human readable display ID used when displaying the parent account"""


class SubAccountsTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The ID of the sub account."""
    account_sub_name: NotRequired[str]
    r"""The name of the sub account."""


class SubAccounts(BaseModel):
    id: Optional[str] = None
    r"""The ID of the sub account."""

    account_sub_name: Optional[str] = None
    r"""The name of the sub account."""


class SubsidiariesModelTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The ID of the subsidiary."""


class SubsidiariesModel(BaseModel):
    id: Optional[str] = None
    r"""The ID of the subsidiary."""


class LedgerAccountTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    display_id: NotRequired[str]
    r"""The human readable display ID used when displaying the account"""
    nominal_code: NotRequired[Nullable[str]]
    r"""The nominal code of the ledger account."""
    code: NotRequired[Nullable[str]]
    r"""The code assigned to the account."""
    classification: NotRequired[Nullable[Classification]]
    r"""The classification of account."""
    type: NotRequired[LedgerAccountType]
    r"""The type of account."""
    sub_type: NotRequired[Nullable[str]]
    r"""The sub type of account."""
    name: NotRequired[Nullable[str]]
    r"""The name of the account."""
    fully_qualified_name: NotRequired[Nullable[str]]
    r"""The fully qualified name of the account."""
    description: NotRequired[Nullable[str]]
    r"""The description of the account."""
    opening_balance: NotRequired[Nullable[float]]
    r"""The opening balance of the account."""
    current_balance: NotRequired[Nullable[float]]
    r"""The current balance of the account."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    tax_type: NotRequired[Nullable[str]]
    r"""The tax type of the account."""
    tax_rate: NotRequired[LinkedTaxRateTypedDict]
    level: NotRequired[Nullable[float]]
    active: NotRequired[Nullable[bool]]
    r"""Whether the account is active or not."""
    status: NotRequired[Nullable[AccountStatus]]
    r"""The status of the account."""
    header: NotRequired[Nullable[bool]]
    r"""Whether the account is a header or not."""
    bank_account: NotRequired[BankAccountTypedDict]
    categories: NotRequired[List[CategoriesTypedDict]]
    r"""The categories of the account."""
    parent_account: NotRequired[ParentAccountTypedDict]
    sub_account: NotRequired[Nullable[bool]]
    r"""Whether the account is a sub account or not."""
    sub_accounts: NotRequired[List[SubAccountsTypedDict]]
    r"""The sub accounts of the account."""
    last_reconciliation_date: NotRequired[Nullable[date]]
    r"""Reconciliation Date means the last calendar day of each Reconciliation Period."""
    subsidiaries: NotRequired[List[SubsidiariesModelTypedDict]]
    r"""The subsidiaries the account belongs to."""
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


class LedgerAccount(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    display_id: Optional[str] = None
    r"""The human readable display ID used when displaying the account"""

    nominal_code: Annotated[
        OptionalNullable[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET
    r"""The nominal code of the ledger account."""

    code: OptionalNullable[str] = UNSET
    r"""The code assigned to the account."""

    classification: OptionalNullable[Classification] = UNSET
    r"""The classification of account."""

    type: Optional[LedgerAccountType] = None
    r"""The type of account."""

    sub_type: OptionalNullable[str] = UNSET
    r"""The sub type of account."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the account."""

    fully_qualified_name: OptionalNullable[str] = UNSET
    r"""The fully qualified name of the account."""

    description: OptionalNullable[str] = UNSET
    r"""The description of the account."""

    opening_balance: OptionalNullable[float] = UNSET
    r"""The opening balance of the account."""

    current_balance: OptionalNullable[float] = UNSET
    r"""The current balance of the account."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    tax_type: OptionalNullable[str] = UNSET
    r"""The tax type of the account."""

    tax_rate: Optional[LinkedTaxRate] = None

    level: OptionalNullable[float] = UNSET

    active: OptionalNullable[bool] = UNSET
    r"""Whether the account is active or not."""

    status: OptionalNullable[AccountStatus] = UNSET
    r"""The status of the account."""

    header: OptionalNullable[bool] = UNSET
    r"""Whether the account is a header or not."""

    bank_account: Optional[BankAccount] = None

    categories: Optional[List[Categories]] = None
    r"""The categories of the account."""

    parent_account: Optional[ParentAccount] = None

    sub_account: OptionalNullable[bool] = UNSET
    r"""Whether the account is a sub account or not."""

    sub_accounts: Optional[List[SubAccounts]] = None
    r"""The sub accounts of the account."""

    last_reconciliation_date: OptionalNullable[date] = UNSET
    r"""Reconciliation Date means the last calendar day of each Reconciliation Period."""

    subsidiaries: Optional[List[SubsidiariesModel]] = None
    r"""The subsidiaries the account belongs to."""

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
            "display_id",
            "nominal_code",
            "code",
            "classification",
            "type",
            "sub_type",
            "name",
            "fully_qualified_name",
            "description",
            "opening_balance",
            "current_balance",
            "currency",
            "tax_type",
            "tax_rate",
            "level",
            "active",
            "status",
            "header",
            "bank_account",
            "categories",
            "parent_account",
            "sub_account",
            "sub_accounts",
            "last_reconciliation_date",
            "subsidiaries",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "nominal_code",
            "code",
            "classification",
            "sub_type",
            "name",
            "fully_qualified_name",
            "description",
            "opening_balance",
            "current_balance",
            "currency",
            "tax_type",
            "level",
            "active",
            "status",
            "header",
            "sub_account",
            "last_reconciliation_date",
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


class LedgerAccountInputTypedDict(TypedDict):
    display_id: NotRequired[str]
    r"""The human readable display ID used when displaying the account"""
    nominal_code: NotRequired[Nullable[str]]
    r"""The nominal code of the ledger account."""
    code: NotRequired[Nullable[str]]
    r"""The code assigned to the account."""
    classification: NotRequired[Nullable[Classification]]
    r"""The classification of account."""
    type: NotRequired[LedgerAccountType]
    r"""The type of account."""
    sub_type: NotRequired[Nullable[str]]
    r"""The sub type of account."""
    name: NotRequired[Nullable[str]]
    r"""The name of the account."""
    fully_qualified_name: NotRequired[Nullable[str]]
    r"""The fully qualified name of the account."""
    description: NotRequired[Nullable[str]]
    r"""The description of the account."""
    opening_balance: NotRequired[Nullable[float]]
    r"""The opening balance of the account."""
    current_balance: NotRequired[Nullable[float]]
    r"""The current balance of the account."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    tax_type: NotRequired[Nullable[str]]
    r"""The tax type of the account."""
    tax_rate: NotRequired[LinkedTaxRateInputTypedDict]
    level: NotRequired[Nullable[float]]
    active: NotRequired[Nullable[bool]]
    r"""Whether the account is active or not."""
    status: NotRequired[Nullable[AccountStatus]]
    r"""The status of the account."""
    header: NotRequired[Nullable[bool]]
    r"""Whether the account is a header or not."""
    bank_account: NotRequired[BankAccountTypedDict]
    parent_account: NotRequired[ParentAccountTypedDict]
    sub_account: NotRequired[Nullable[bool]]
    r"""Whether the account is a sub account or not."""
    last_reconciliation_date: NotRequired[Nullable[date]]
    r"""Reconciliation Date means the last calendar day of each Reconciliation Period."""
    subsidiaries: NotRequired[List[SubsidiariesModelTypedDict]]
    r"""The subsidiaries the account belongs to."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class LedgerAccountInput(BaseModel):
    display_id: Optional[str] = None
    r"""The human readable display ID used when displaying the account"""

    nominal_code: Annotated[
        OptionalNullable[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET
    r"""The nominal code of the ledger account."""

    code: OptionalNullable[str] = UNSET
    r"""The code assigned to the account."""

    classification: OptionalNullable[Classification] = UNSET
    r"""The classification of account."""

    type: Optional[LedgerAccountType] = None
    r"""The type of account."""

    sub_type: OptionalNullable[str] = UNSET
    r"""The sub type of account."""

    name: OptionalNullable[str] = UNSET
    r"""The name of the account."""

    fully_qualified_name: OptionalNullable[str] = UNSET
    r"""The fully qualified name of the account."""

    description: OptionalNullable[str] = UNSET
    r"""The description of the account."""

    opening_balance: OptionalNullable[float] = UNSET
    r"""The opening balance of the account."""

    current_balance: OptionalNullable[float] = UNSET
    r"""The current balance of the account."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    tax_type: OptionalNullable[str] = UNSET
    r"""The tax type of the account."""

    tax_rate: Optional[LinkedTaxRateInput] = None

    level: OptionalNullable[float] = UNSET

    active: OptionalNullable[bool] = UNSET
    r"""Whether the account is active or not."""

    status: OptionalNullable[AccountStatus] = UNSET
    r"""The status of the account."""

    header: OptionalNullable[bool] = UNSET
    r"""Whether the account is a header or not."""

    bank_account: Optional[BankAccount] = None

    parent_account: Optional[ParentAccount] = None

    sub_account: OptionalNullable[bool] = UNSET
    r"""Whether the account is a sub account or not."""

    last_reconciliation_date: OptionalNullable[date] = UNSET
    r"""Reconciliation Date means the last calendar day of each Reconciliation Period."""

    subsidiaries: Optional[List[SubsidiariesModel]] = None
    r"""The subsidiaries the account belongs to."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "display_id",
            "nominal_code",
            "code",
            "classification",
            "type",
            "sub_type",
            "name",
            "fully_qualified_name",
            "description",
            "opening_balance",
            "current_balance",
            "currency",
            "tax_type",
            "tax_rate",
            "level",
            "active",
            "status",
            "header",
            "bank_account",
            "parent_account",
            "sub_account",
            "last_reconciliation_date",
            "subsidiaries",
            "row_version",
            "pass_through",
        ]
        nullable_fields = [
            "nominal_code",
            "code",
            "classification",
            "sub_type",
            "name",
            "fully_qualified_name",
            "description",
            "opening_balance",
            "current_balance",
            "currency",
            "tax_type",
            "level",
            "active",
            "status",
            "header",
            "sub_account",
            "last_reconciliation_date",
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