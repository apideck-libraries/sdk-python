"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CompaniesFilterTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the company to filter on"""


class CompaniesFilter(BaseModel):
    name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Name of the company to filter on"""
