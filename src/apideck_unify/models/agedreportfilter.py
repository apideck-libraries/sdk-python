"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AgedReportFilterTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""Filter by customer id"""
    report_as_of_date: NotRequired[str]
    r"""The cutoff date for considering transactions"""
    period_count: NotRequired[int]
    r"""Number of periods to split the aged creditors report into"""
    period_length: NotRequired[int]
    r"""Length of each period in days"""


class AgedReportFilter(BaseModel):
    customer_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by customer id"""

    report_as_of_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""The cutoff date for considering transactions"""

    period_count: Annotated[Optional[int], FieldMetadata(query=True)] = None
    r"""Number of periods to split the aged creditors report into"""

    period_length: Annotated[Optional[int], FieldMetadata(query=True)] = None
    r"""Length of each period in days"""
