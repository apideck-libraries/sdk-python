"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .profitandlossindicator import (
    ProfitAndLossIndicator,
    ProfitAndLossIndicatorTypedDict,
)
from .profitandlosstype import ProfitAndLossType
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Any, Optional
from typing_extensions import NotRequired, TypedDict


class IncomeTypedDict(TypedDict):
    r"""The operating income accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class Income(BaseModel):
    r"""The operating income accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class CostOfGoodsSoldTypedDict(TypedDict):
    r"""The cost of goods sold accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class CostOfGoodsSold(BaseModel):
    r"""The cost of goods sold accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class ExpensesModelTypedDict(TypedDict):
    r"""The operating expenses accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class ExpensesModel(BaseModel):
    r"""The operating expenses accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class OtherIncomeTypedDict(TypedDict):
    r"""The other income accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class OtherIncome(BaseModel):
    r"""The other income accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class OtherExpensesTypedDict(TypedDict):
    r"""The other expenses accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class OtherExpenses(BaseModel):
    r"""The other expenses accounts"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class UncategorizedAccountsTypedDict(TypedDict):
    r"""The accounts not categorized in the other sections"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""
    records: Any
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    code: NotRequired[str]
    r"""The account code of the account"""
    title: NotRequired[str]
    r"""The name of the account."""
    type: NotRequired[Nullable[ProfitAndLossType]]
    r"""The type of profit and loss"""


class UncategorizedAccounts(BaseModel):
    r"""The accounts not categorized in the other sections"""

    total: Nullable[float]
    r"""The aggregated total of all accounts within this category."""

    records: Any

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    code: Optional[str] = None
    r"""The account code of the account"""

    title: Optional[str] = None
    r"""The name of the account."""

    type: OptionalNullable[ProfitAndLossType] = UNSET
    r"""The type of profit and loss"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "code", "title", "type"]
        nullable_fields = ["total", "type"]
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


class ProfitAndLossTypedDict(TypedDict):
    report_name: str
    r"""The name of the report"""
    currency: Nullable[Currency]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    income: IncomeTypedDict
    r"""The operating income accounts"""
    expenses: ExpensesModelTypedDict
    r"""The operating expenses accounts"""
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    start_date: NotRequired[str]
    r"""The start date of the report"""
    end_date: NotRequired[str]
    r"""The end date of the report"""
    cost_of_goods_sold: NotRequired[CostOfGoodsSoldTypedDict]
    r"""The cost of goods sold accounts"""
    other_income: NotRequired[OtherIncomeTypedDict]
    r"""The other income accounts"""
    other_expenses: NotRequired[OtherExpensesTypedDict]
    r"""The other expenses accounts"""
    uncategorized_accounts: NotRequired[UncategorizedAccountsTypedDict]
    r"""The accounts not categorized in the other sections"""
    gross_profit: NotRequired[ProfitAndLossIndicatorTypedDict]
    net_operating_income: NotRequired[ProfitAndLossIndicatorTypedDict]
    net_income: NotRequired[ProfitAndLossIndicatorTypedDict]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    customer: NotRequired[str]
    r"""The customer id"""


class ProfitAndLoss(BaseModel):
    report_name: str
    r"""The name of the report"""

    currency: Nullable[Currency]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    income: Income
    r"""The operating income accounts"""

    expenses: ExpensesModel
    r"""The operating expenses accounts"""

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    start_date: Optional[str] = None
    r"""The start date of the report"""

    end_date: Optional[str] = None
    r"""The end date of the report"""

    cost_of_goods_sold: Optional[CostOfGoodsSold] = None
    r"""The cost of goods sold accounts"""

    other_income: Optional[OtherIncome] = None
    r"""The other income accounts"""

    other_expenses: Optional[OtherExpenses] = None
    r"""The other expenses accounts"""

    uncategorized_accounts: Optional[UncategorizedAccounts] = None
    r"""The accounts not categorized in the other sections"""

    gross_profit: Optional[ProfitAndLossIndicator] = None

    net_operating_income: Optional[ProfitAndLossIndicator] = None

    net_income: Optional[ProfitAndLossIndicator] = None

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    customer: Optional[str] = None
    r"""The customer id"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "start_date",
            "end_date",
            "cost_of_goods_sold",
            "other_income",
            "other_expenses",
            "uncategorized_accounts",
            "gross_profit",
            "net_operating_income",
            "net_income",
            "custom_mappings",
            "customer",
        ]
        nullable_fields = ["currency", "custom_mappings"]
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
