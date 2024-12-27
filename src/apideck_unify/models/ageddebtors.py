"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .outstandingbalancebycustomer import (
    OutstandingBalanceByCustomer,
    OutstandingBalanceByCustomerTypedDict,
)
from apideck_unify.types import BaseModel
from datetime import date, datetime
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AgedDebtorsTypedDict(TypedDict):
    report_generated_at: NotRequired[datetime]
    r"""The exact date and time the report was generated."""
    report_as_of_date: NotRequired[date]
    r"""The cutoff date for transactions included in the report."""
    period_count: NotRequired[int]
    r"""Number of aging periods shown in the report."""
    period_length: NotRequired[int]
    r"""Length of each aging period in days."""
    outstanding_balances: NotRequired[List[OutstandingBalanceByCustomerTypedDict]]


class AgedDebtors(BaseModel):
    report_generated_at: Optional[datetime] = None
    r"""The exact date and time the report was generated."""

    report_as_of_date: Optional[date] = None
    r"""The cutoff date for transactions included in the report."""

    period_count: Optional[int] = 4
    r"""Number of aging periods shown in the report."""

    period_length: Optional[int] = 30
    r"""Length of each aging period in days."""

    outstanding_balances: Optional[List[OutstandingBalanceByCustomer]] = None
