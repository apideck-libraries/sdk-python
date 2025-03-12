"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PeriodType(str, Enum):
    r"""The type of period to include in the resource: month, quarter, year."""

    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"


class BalanceSheetFilterTypedDict(TypedDict):
    start_date: NotRequired[str]
    r"""The start date of the period to include in the resource."""
    end_date: NotRequired[str]
    r"""The end date of the period to include in the resource."""
    period_count: NotRequired[int]
    r"""The number of periods to include in the resource."""
    period_type: NotRequired[PeriodType]
    r"""The type of period to include in the resource: month, quarter, year."""


class BalanceSheetFilter(BaseModel):
    start_date: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
        FieldMetadata(query=True),
    ] = None
    r"""The start date of the period to include in the resource."""

    end_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""The end date of the period to include in the resource."""

    period_count: Annotated[Optional[int], FieldMetadata(query=True)] = None
    r"""The number of periods to include in the resource."""

    period_type: Annotated[Optional[PeriodType], FieldMetadata(query=True)] = None
    r"""The type of period to include in the resource: month, quarter, year."""
