"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from typing import Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class TwoTypedDict(TypedDict):
    pass


class Two(BaseModel):
    pass


DetailTypedDict = TypeAliasType("DetailTypedDict", Union[TwoTypedDict, str])
r"""Contains parameter or domain specific information related to the error and why it occurred."""


Detail = TypeAliasType("Detail", Union[Two, str])
r"""Contains parameter or domain specific information related to the error and why it occurred."""


class UnexpectedErrorResponseTypedDict(TypedDict):
    r"""Unexpected error"""

    status_code: NotRequired[float]
    r"""HTTP status code"""
    error: NotRequired[str]
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""
    type_name: NotRequired[str]
    r"""The type of error returned"""
    message: NotRequired[str]
    r"""A human-readable message providing more details about the error."""
    detail: NotRequired[DetailTypedDict]
    r"""Contains parameter or domain specific information related to the error and why it occurred."""
    ref: NotRequired[str]
    r"""Link to documentation of error type"""


class UnexpectedErrorResponse(BaseModel):
    r"""Unexpected error"""

    status_code: Optional[float] = None
    r"""HTTP status code"""

    error: Optional[str] = None
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""

    type_name: Optional[str] = None
    r"""The type of error returned"""

    message: Optional[str] = None
    r"""A human-readable message providing more details about the error."""

    detail: Optional[Detail] = None
    r"""Contains parameter or domain specific information related to the error and why it occurred."""

    ref: Optional[str] = None
    r"""Link to documentation of error type"""