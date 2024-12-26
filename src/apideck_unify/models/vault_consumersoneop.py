"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconsumerresponse import GetConsumerResponse, GetConsumerResponseTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VaultConsumersOneGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConsumersOneGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class VaultConsumersOneRequestTypedDict(TypedDict):
    consumer_id: str
    r"""ID of the consumer to return"""


class VaultConsumersOneRequest(BaseModel):
    consumer_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the consumer to return"""


class VaultConsumersOneResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    get_consumer_response: NotRequired[GetConsumerResponseTypedDict]
    r"""Consumer"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class VaultConsumersOneResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    get_consumer_response: Optional[GetConsumerResponse] = None
    r"""Consumer"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
