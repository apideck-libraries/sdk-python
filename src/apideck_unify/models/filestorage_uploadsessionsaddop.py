"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createuploadsessionrequest import (
    CreateUploadSessionRequest,
    CreateUploadSessionRequestTypedDict,
)
from .createuploadsessionresponse import (
    CreateUploadSessionResponse,
    CreateUploadSessionResponseTypedDict,
)
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


FILE_STORAGE_UPLOAD_SESSIONS_ADD_OP_SERVERS = [
    "https://upload.apideck.com",
]


class FileStorageUploadSessionsAddGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class FileStorageUploadSessionsAddGlobals(BaseModel):
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


class FileStorageUploadSessionsAddRequestTypedDict(TypedDict):
    create_upload_session_request: CreateUploadSessionRequestTypedDict
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


class FileStorageUploadSessionsAddRequest(BaseModel):
    create_upload_session_request: Annotated[
        CreateUploadSessionRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""

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


class FileStorageUploadSessionsAddResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    create_upload_session_response: NotRequired[CreateUploadSessionResponseTypedDict]
    r"""UploadSessions"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class FileStorageUploadSessionsAddResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    create_upload_session_response: Optional[CreateUploadSessionResponse] = None
    r"""UploadSessions"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
