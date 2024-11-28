"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .validateconnectionstateresponse import (
    ValidateConnectionStateResponse,
    ValidateConnectionStateResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VaultValidateConnectionStateGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultValidateConnectionStateGlobals(BaseModel):
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


class VaultValidateConnectionStateRequestBodyTypedDict(TypedDict):
    pass


class VaultValidateConnectionStateRequestBody(BaseModel):
    pass


class VaultValidateConnectionStateRequestTypedDict(TypedDict):
    service_id: str
    r"""Service ID of the resource to return"""
    unified_api: str
    r"""Unified API"""
    request_body: NotRequired[VaultValidateConnectionStateRequestBodyTypedDict]


class VaultValidateConnectionStateRequest(BaseModel):
    service_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Service ID of the resource to return"""

    unified_api: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unified API"""

    request_body: Annotated[
        Optional[VaultValidateConnectionStateRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class VaultValidateConnectionStateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    validate_connection_state_response: NotRequired[
        ValidateConnectionStateResponseTypedDict
    ]
    r"""Connection access token refreshed"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class VaultValidateConnectionStateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    validate_connection_state_response: Optional[ValidateConnectionStateResponse] = None
    r"""Connection access token refreshed"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
