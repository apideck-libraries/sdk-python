"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updateconsumerrequest import UpdateConsumerRequest, UpdateConsumerRequestTypedDict
from .updateconsumerresponse import (
    UpdateConsumerResponse,
    UpdateConsumerResponseTypedDict,
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


class VaultConsumersUpdateGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConsumersUpdateGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class VaultConsumersUpdateRequestTypedDict(TypedDict):
    consumer_id: str
    r"""ID of the consumer to return"""
    update_consumer_request: UpdateConsumerRequestTypedDict


class VaultConsumersUpdateRequest(BaseModel):
    consumer_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the consumer to return"""

    update_consumer_request: Annotated[
        UpdateConsumerRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class VaultConsumersUpdateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    update_consumer_response: NotRequired[UpdateConsumerResponseTypedDict]
    r"""Consumer updated"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class VaultConsumersUpdateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    update_consumer_response: Optional[UpdateConsumerResponse] = None
    r"""Consumer updated"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
