"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateCallbackStateResponseDataTypedDict(TypedDict):
    state: NotRequired[str]
    r"""Callback state"""


class CreateCallbackStateResponseData(BaseModel):
    state: Optional[str] = None
    r"""Callback state"""


class CreateCallbackStateResponseTypedDict(TypedDict):
    r"""Callback state created"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: CreateCallbackStateResponseDataTypedDict


class CreateCallbackStateResponse(BaseModel):
    r"""Callback state created"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: CreateCallbackStateResponseData
