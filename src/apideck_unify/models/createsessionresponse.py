"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from typing_extensions import TypedDict


class CreateSessionResponseDataTypedDict(TypedDict):
    session_uri: str
    session_token: str


class CreateSessionResponseData(BaseModel):
    session_uri: str

    session_token: str


class CreateSessionResponseTypedDict(TypedDict):
    r"""Session created"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: CreateSessionResponseDataTypedDict


class CreateSessionResponse(BaseModel):
    r"""Session created"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: CreateSessionResponseData
