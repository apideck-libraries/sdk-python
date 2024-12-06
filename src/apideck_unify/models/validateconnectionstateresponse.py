"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectionstate import ConnectionState
from apideck_unify.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ValidateConnectionStateResponseDataTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The unique identifier of the connection."""
    state: NotRequired[ConnectionState]
    r"""[Connection state flow](#section/Connection-state)"""


class ValidateConnectionStateResponseData(BaseModel):
    id: Optional[str] = None
    r"""The unique identifier of the connection."""

    state: Optional[ConnectionState] = None
    r"""[Connection state flow](#section/Connection-state)"""


class ValidateConnectionStateResponseTypedDict(TypedDict):
    r"""Connection access token refreshed"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: ValidateConnectionStateResponseDataTypedDict


class ValidateConnectionStateResponse(BaseModel):
    r"""Connection access token refreshed"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: ValidateConnectionStateResponseData
