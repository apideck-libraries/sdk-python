"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CategoriesFilterType(str, Enum):
    r"""The type of the category."""

    SUPPLIER = "supplier"
    EXPENSE = "expense"
    REVENUE = "revenue"


class CategoriesFilterTypedDict(TypedDict):
    type: NotRequired[CategoriesFilterType]
    r"""The type of the category."""


class CategoriesFilter(BaseModel):
    type: Annotated[Optional[CategoriesFilterType], FieldMetadata(query=True)] = None
    r"""The type of the category."""
