"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .balancesheetfilter import BalanceSheetFilter, BalanceSheetFilterTypedDict
from .getbalancesheetresponse import (
    GetBalanceSheetResponse,
    GetBalanceSheetResponseTypedDict,
)
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingBalanceSheetOneGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingBalanceSheetOneGlobals(BaseModel):
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


class AccountingBalanceSheetOneRequestTypedDict(TypedDict):
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    pass_through: NotRequired[Dict[str, Any]]
    r"""Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads"""
    filter_: NotRequired[BalanceSheetFilterTypedDict]
    r"""Apply filters"""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingBalanceSheetOneRequest(BaseModel):
    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""

    pass_through: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads"""

    filter_: Annotated[
        Optional[BalanceSheetFilter],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Apply filters"""

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingBalanceSheetOneResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    get_balance_sheet_response: NotRequired[GetBalanceSheetResponseTypedDict]
    r"""BalanceSheet"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class AccountingBalanceSheetOneResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    get_balance_sheet_response: Optional[GetBalanceSheetResponse] = None
    r"""BalanceSheet"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""