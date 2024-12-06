"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LeadsFilterTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the lead to filter on"""
    first_name: NotRequired[str]
    r"""First name of the lead to filter on"""
    last_name: NotRequired[str]
    r"""Last name of the lead to filter on"""
    email: NotRequired[str]
    r"""E-mail of the lead to filter on"""
    phone_number: NotRequired[str]
    r"""Phone number of the lead to filter on"""


class LeadsFilter(BaseModel):
    name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Name of the lead to filter on"""

    first_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""First name of the lead to filter on"""

    last_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Last name of the lead to filter on"""

    email: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""E-mail of the lead to filter on"""

    phone_number: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Phone number of the lead to filter on"""
