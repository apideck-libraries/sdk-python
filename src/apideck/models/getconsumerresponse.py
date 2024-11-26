"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .consumer import Consumer, ConsumerTypedDict
from apideck.types import BaseModel
from typing_extensions import TypedDict


class GetConsumerResponseTypedDict(TypedDict):
    r"""Consumer"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: ConsumerTypedDict


class GetConsumerResponse(BaseModel):
    r"""Consumer"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: Consumer