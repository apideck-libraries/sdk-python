"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createsessionresponse import CreateSessionResponse, CreateSessionResponseTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .session import Session, SessionTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VaultSessionsCreateGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultSessionsCreateGlobals(BaseModel):
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


class VaultSessionsCreateRequestTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    session: NotRequired[SessionTypedDict]
    r"""Additional redirect uri and/or consumer metadata"""


class VaultSessionsCreateRequest(BaseModel):
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

    session: Annotated[
        Optional[Session],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Additional redirect uri and/or consumer metadata"""


class VaultSessionsCreateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    create_session_response: NotRequired[CreateSessionResponseTypedDict]
    r"""Session created"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class VaultSessionsCreateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    create_session_response: Optional[CreateSessionResponse] = None
    r"""Session created"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
