"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connector import Connector, ConnectorTypedDict
from .links import Links, LinksTypedDict
from .meta import Meta, MetaTypedDict
from apideck_unify.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GetConnectorsResponseTypedDict(TypedDict):
    r"""Connectors"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: List[ConnectorTypedDict]
    meta: NotRequired[MetaTypedDict]
    r"""Response metadata"""
    links: NotRequired[LinksTypedDict]
    r"""Links to navigate to previous or next pages through the API"""


class GetConnectorsResponse(BaseModel):
    r"""Connectors"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: List[Connector]

    meta: Optional[Meta] = None
    r"""Response metadata"""

    links: Optional[Links] = None
    r"""Links to navigate to previous or next pages through the API"""
