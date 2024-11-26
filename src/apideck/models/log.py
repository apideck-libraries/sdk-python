"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class OperationTypedDict(TypedDict):
    r"""The request as defined in OpenApi Spec."""

    id: str
    r"""The OpenApi Operation Id associated with the request"""
    name: str
    r"""The OpenApi Operation name associated with the request"""


class Operation(BaseModel):
    r"""The request as defined in OpenApi Spec."""

    id: str
    r"""The OpenApi Operation Id associated with the request"""

    name: str
    r"""The OpenApi Operation name associated with the request"""


class ServiceTypedDict(TypedDict):
    r"""Apideck service provider associated with request."""

    id: str
    r"""Apideck service provider id."""
    name: str
    r"""Apideck service provider name."""


class Service(BaseModel):
    r"""Apideck service provider associated with request."""

    id: str
    r"""Apideck service provider id."""

    name: str
    r"""Apideck service provider name."""


class UnifiedAPI(str, Enum):
    r"""Which Unified Api request was made to."""

    CRM = "crm"
    LEAD = "lead"
    PROXY = "proxy"
    VAULT = "vault"
    ACCOUNTING = "accounting"
    HRIS = "hris"
    ATS = "ats"
    ECOMMERCE = "ecommerce"
    ISSUE_TRACKING = "issue-tracking"
    POS = "pos"
    FILE_STORAGE = "file-storage"
    SMS = "sms"


class LogTypedDict(TypedDict):
    api_style: str
    r"""Indicates if the request was made via REST or Graphql endpoint."""
    base_url: str
    r"""The Apideck base URL the request was made to."""
    child_request: bool
    r"""Indicates whether or not this is a child or parent request."""
    consumer_id: str
    r"""The consumer Id associated with the request."""
    duration: float
    r"""The entire execution time in milliseconds it took to call the Apideck service provider."""
    execution: int
    r"""The entire execution time in milliseconds it took to make the request."""
    has_children: bool
    r"""When request is a parent request, this indicates if there are child requests associated."""
    http_method: str
    r"""HTTP Method of request."""
    id: str
    r"""UUID acting as Request Identifier."""
    latency: float
    r"""Latency added by making this request via Unified Api."""
    operation: OperationTypedDict
    r"""The request as defined in OpenApi Spec."""
    parent_id: Nullable[str]
    r"""When request is a child request, this UUID indicates it's parent request."""
    path: str
    r"""The path component of the URI the request was made to."""
    sandbox: bool
    r"""Indicates whether the request was made using Apidecks sandbox credentials or not."""
    service: ServiceTypedDict
    r"""Apideck service provider associated with request."""
    status_code: int
    r"""HTTP Status code that was returned."""
    success: bool
    r"""Whether or not the request was successful."""
    timestamp: str
    r"""ISO Date and time when the request was made."""
    unified_api: UnifiedAPI
    r"""Which Unified Api request was made to."""
    error_message: NotRequired[Nullable[str]]
    r"""If error occurred, this is brief explanation"""
    source_ip: NotRequired[Nullable[str]]
    r"""The IP address of the source of the request."""


class Log(BaseModel):
    api_style: str
    r"""Indicates if the request was made via REST or Graphql endpoint."""

    base_url: str
    r"""The Apideck base URL the request was made to."""

    child_request: bool
    r"""Indicates whether or not this is a child or parent request."""

    consumer_id: str
    r"""The consumer Id associated with the request."""

    duration: float
    r"""The entire execution time in milliseconds it took to call the Apideck service provider."""

    execution: int
    r"""The entire execution time in milliseconds it took to make the request."""

    has_children: bool
    r"""When request is a parent request, this indicates if there are child requests associated."""

    http_method: str
    r"""HTTP Method of request."""

    id: str
    r"""UUID acting as Request Identifier."""

    latency: float
    r"""Latency added by making this request via Unified Api."""

    operation: Operation
    r"""The request as defined in OpenApi Spec."""

    parent_id: Nullable[str]
    r"""When request is a child request, this UUID indicates it's parent request."""

    path: str
    r"""The path component of the URI the request was made to."""

    sandbox: bool
    r"""Indicates whether the request was made using Apidecks sandbox credentials or not."""

    service: Service
    r"""Apideck service provider associated with request."""

    status_code: int
    r"""HTTP Status code that was returned."""

    success: bool
    r"""Whether or not the request was successful."""

    timestamp: str
    r"""ISO Date and time when the request was made."""

    unified_api: UnifiedAPI
    r"""Which Unified Api request was made to."""

    error_message: OptionalNullable[str] = UNSET
    r"""If error occurred, this is brief explanation"""

    source_ip: OptionalNullable[str] = UNSET
    r"""The IP address of the source of the request."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["error_message", "source_ip"]
        nullable_fields = ["parent_id", "error_message", "source_ip"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m