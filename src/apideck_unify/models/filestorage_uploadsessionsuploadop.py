"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updateuploadsessionresponse import (
    UpdateUploadSessionResponse,
    UpdateUploadSessionResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import io
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


FILE_STORAGE_UPLOAD_SESSIONS_UPLOAD_OP_SERVERS = [
    "https://upload.apideck.com",
]


class FileStorageUploadSessionsUploadGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class FileStorageUploadSessionsUploadGlobals(BaseModel):
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


class FileStorageUploadSessionsUploadRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    part_number: float
    r"""Part number of the file part being uploaded."""
    request_body: Union[bytes, IO[bytes], io.BufferedReader]
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    digest: NotRequired[str]
    r"""The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)"""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class FileStorageUploadSessionsUploadRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    part_number: Annotated[
        float, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Part number of the file part being uploaded."""

    request_body: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        FieldMetadata(request=RequestMetadata(media_type="*/*")),
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

    digest: Annotated[
        Optional[str],
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)"""

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""


class FileStorageUploadSessionsUploadResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    update_upload_session_response: NotRequired[UpdateUploadSessionResponseTypedDict]
    r"""UploadSessions"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class FileStorageUploadSessionsUploadResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    update_upload_session_response: Optional[UpdateUploadSessionResponse] = None
    r"""UploadSessions"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
