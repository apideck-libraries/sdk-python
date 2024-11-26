"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sortdirection import SortDirection
from apideck.types import BaseModel
from apideck.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PurchaseOrdersSortBy(str, Enum):
    r"""The field on which to sort the Purchase Orders"""

    UPDATED_AT = "updated_at"
    CREATED_AT = "created_at"


class PurchaseOrdersSortTypedDict(TypedDict):
    by: NotRequired[PurchaseOrdersSortBy]
    r"""The field on which to sort the Purchase Orders"""
    direction: NotRequired[SortDirection]
    r"""The direction in which to sort the results"""


class PurchaseOrdersSort(BaseModel):
    by: Annotated[Optional[PurchaseOrdersSortBy], FieldMetadata(query=True)] = None
    r"""The field on which to sort the Purchase Orders"""

    direction: Annotated[Optional[SortDirection], FieldMetadata(query=True)] = (
        SortDirection.ASC
    )
    r"""The direction in which to sort the results"""