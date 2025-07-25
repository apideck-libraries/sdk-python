"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.models import ApideckError
from apideck_unify.types import BaseModel
import httpx
from typing import Optional


class PaymentRequiredResponseData(BaseModel):
    status_code: Optional[float] = None
    r"""HTTP status code"""

    error: Optional[str] = None
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""

    type_name: Optional[str] = None
    r"""The type of error returned"""

    message: Optional[str] = None
    r"""A human-readable message providing more details about the error."""

    detail: Optional[str] = None
    r"""Contains parameter or domain specific information related to the error and why it occurred."""

    ref: Optional[str] = None
    r"""Link to documentation of error type"""


class PaymentRequiredResponse(ApideckError):
    r"""Payment Required"""

    data: PaymentRequiredResponseData

    def __init__(
        self,
        data: PaymentRequiredResponseData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        fallback = body or raw_response.text
        message = str(data.message) or fallback
        super().__init__(message, raw_response, body)
        self.data = data
