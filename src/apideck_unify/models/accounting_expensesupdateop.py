"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .expense_input import ExpenseInput, ExpenseInputTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updateexpenseresponse import UpdateExpenseResponse, UpdateExpenseResponseTypedDict
from apideck_unify.types import BaseModel
from apideck_unify.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingExpensesUpdateGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingExpensesUpdateGlobals(BaseModel):
    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class AccountingExpensesUpdateRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    expense: ExpenseInputTypedDict
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingExpensesUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    expense: Annotated[
        ExpenseInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""

    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingExpensesUpdateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    update_expense_response: NotRequired[UpdateExpenseResponseTypedDict]
    r"""Expenses"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class AccountingExpensesUpdateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    update_expense_response: Optional[UpdateExpenseResponse] = None
    r"""Expenses"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
