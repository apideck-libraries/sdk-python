"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .requestcountallocation import (
    RequestCountAllocation,
    RequestCountAllocationTypedDict,
)
from apideck_unify.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ConsumerRequestCountsInDateRangeResponseDataTypedDict(TypedDict):
    application_id: NotRequired[str]
    consumer_id: NotRequired[str]
    start_datetime: NotRequired[str]
    end_datetime: NotRequired[str]
    aggregated_request_count: NotRequired[float]
    request_counts: NotRequired[RequestCountAllocationTypedDict]


class ConsumerRequestCountsInDateRangeResponseData(BaseModel):
    application_id: Optional[str] = None

    consumer_id: Optional[str] = None

    start_datetime: Optional[str] = None

    end_datetime: Optional[str] = None

    aggregated_request_count: Optional[float] = None

    request_counts: Optional[RequestCountAllocation] = None


class ConsumerRequestCountsInDateRangeResponseTypedDict(TypedDict):
    r"""Consumers Request Counts within Date Range"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: ConsumerRequestCountsInDateRangeResponseDataTypedDict


class ConsumerRequestCountsInDateRangeResponse(BaseModel):
    r"""Consumers Request Counts within Date Range"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: ConsumerRequestCountsInDateRangeResponseData
