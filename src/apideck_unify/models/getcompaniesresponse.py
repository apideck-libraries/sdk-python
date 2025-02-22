"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .company import Company, CompanyTypedDict
from .links import Links, LinksTypedDict
from .meta import Meta, MetaTypedDict
from apideck_unify.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GetCompaniesResponseTypedDict(TypedDict):
    r"""Companies"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    service: str
    r"""Apideck ID of service provider"""
    resource: str
    r"""Unified API resource name"""
    operation: str
    r"""Operation performed"""
    data: List[CompanyTypedDict]
    meta: NotRequired[MetaTypedDict]
    r"""Response metadata"""
    links: NotRequired[LinksTypedDict]
    r"""Links to navigate to previous or next pages through the API"""


class GetCompaniesResponse(BaseModel):
    r"""Companies"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    service: str
    r"""Apideck ID of service provider"""

    resource: str
    r"""Unified API resource name"""

    operation: str
    r"""Operation performed"""

    data: List[Company]

    meta: Optional[Meta] = None
    r"""Response metadata"""

    links: Optional[Links] = None
    r"""Links to navigate to previous or next pages through the API"""
