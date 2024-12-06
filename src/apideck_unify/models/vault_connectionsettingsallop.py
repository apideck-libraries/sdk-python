"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconnectionresponse import GetConnectionResponse, GetConnectionResponseTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConnectionSettingsAllGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConnectionSettingsAllGlobals(BaseModel):
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


class VaultConnectionSettingsAllRequestTypedDict(TypedDict):
    unified_api: str
    r"""Unified API"""
    service_id: str
    r"""Service ID of the resource to return"""
    resource: str
    r"""Name of the resource (plural)"""


class VaultConnectionSettingsAllRequest(BaseModel):
    unified_api: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unified API"""

    service_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Service ID of the resource to return"""

    resource: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the resource (plural)"""


VaultConnectionSettingsAllResponseTypedDict = TypeAliasType(
    "VaultConnectionSettingsAllResponseTypedDict",
    Union[GetConnectionResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConnectionSettingsAllResponse = TypeAliasType(
    "VaultConnectionSettingsAllResponse",
    Union[GetConnectionResponse, UnexpectedErrorResponse],
)
