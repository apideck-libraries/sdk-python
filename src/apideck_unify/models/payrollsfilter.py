"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PayrollsFilterTypedDict(TypedDict):
    start_date: NotRequired[str]
    r"""Return payrolls whose pay period is after the start date"""
    end_date: NotRequired[str]
    r"""Return payrolls whose pay period is before the end date"""


class PayrollsFilter(BaseModel):
    start_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Return payrolls whose pay period is after the start date"""

    end_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Return payrolls whose pay period is before the end date"""
