"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .deleteconsumerresponse import (
    DeleteConsumerResponse,
    DeleteConsumerResponseTypedDict,
)
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VaultConsumersDeleteGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConsumersDeleteGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class VaultConsumersDeleteRequestTypedDict(TypedDict):
    consumer_id: str
    r"""ID of the consumer to return"""


class VaultConsumersDeleteRequest(BaseModel):
    consumer_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the consumer to return"""


class VaultConsumersDeleteResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    delete_consumer_response: NotRequired[DeleteConsumerResponseTypedDict]
    r"""Consumer deleted"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class VaultConsumersDeleteResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    delete_consumer_response: Optional[DeleteConsumerResponse] = None
    r"""Consumer deleted"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
