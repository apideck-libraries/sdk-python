"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .balancebytransaction import BalanceByTransaction, BalanceByTransactionTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import date
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BalanceByPeriodTypedDict(TypedDict):
    start_date: NotRequired[Nullable[date]]
    r"""The starting date of the period. If not provided, it represents the oldest period, where all transactions due before the specified `end_date` are included."""
    end_date: NotRequired[Nullable[date]]
    r"""The ending date of the period. If not provided, it represents an open-ended period starting from the `start_date`, typically capturing future-dated transactions that are not yet aged."""
    total_amount: NotRequired[float]
    r"""Total amount of the period."""
    balances_by_transaction: NotRequired[List[BalanceByTransactionTypedDict]]


class BalanceByPeriod(BaseModel):
    start_date: OptionalNullable[date] = UNSET
    r"""The starting date of the period. If not provided, it represents the oldest period, where all transactions due before the specified `end_date` are included."""

    end_date: OptionalNullable[date] = UNSET
    r"""The ending date of the period. If not provided, it represents an open-ended period starting from the `start_date`, typically capturing future-dated transactions that are not yet aged."""

    total_amount: Optional[float] = None
    r"""Total amount of the period."""

    balances_by_transaction: Optional[List[BalanceByTransaction]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "start_date",
            "end_date",
            "total_amount",
            "balances_by_transaction",
        ]
        nullable_fields = ["start_date", "end_date"]
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
