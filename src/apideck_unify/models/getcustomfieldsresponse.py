"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customfieldfinder import CustomFieldFinder, CustomFieldFinderTypedDict
from apideck_unify.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GetCustomFieldsResponseTypedDict(TypedDict):
    r"""Custom mapping"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: List[CustomFieldFinderTypedDict]


class GetCustomFieldsResponse(BaseModel):
    r"""Custom mapping"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: List[CustomFieldFinder]