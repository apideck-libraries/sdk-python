"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from typing import Any, Dict, Optional, Union
from typing_extensions import TypeAliasType


UnauthorizedResponseDetailTypedDict = TypeAliasType(
    "UnauthorizedResponseDetailTypedDict", Union[str, Dict[str, Any]]
)
r"""Contains parameter or domain specific information related to the error and why it occurred."""


UnauthorizedResponseDetail = TypeAliasType(
    "UnauthorizedResponseDetail", Union[str, Dict[str, Any]]
)
r"""Contains parameter or domain specific information related to the error and why it occurred."""


class UnauthorizedResponseData(BaseModel):
    status_code: Optional[float] = None
    r"""HTTP status code"""

    error: Optional[str] = None
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""

    type_name: Optional[str] = None
    r"""The type of error returned"""

    message: Optional[str] = None
    r"""A human-readable message providing more details about the error."""

    detail: Optional[UnauthorizedResponseDetail] = None
    r"""Contains parameter or domain specific information related to the error and why it occurred."""

    ref: Optional[str] = None
    r"""Link to documentation of error type"""


class UnauthorizedResponse(Exception):
    r"""Unauthorized"""

    data: UnauthorizedResponseData

    def __init__(self, data: UnauthorizedResponseData):
        self.data = data

    def __str__(self) -> str:
        return self.data.message if self.data.message is not None else "unknown error"
