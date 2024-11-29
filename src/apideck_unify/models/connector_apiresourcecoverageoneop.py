"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getapiresourcecoverageresponse import (
    GetAPIResourceCoverageResponse,
    GetAPIResourceCoverageResponseTypedDict,
)
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


class ConnectorAPIResourceCoverageOneGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class ConnectorAPIResourceCoverageOneGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class ConnectorAPIResourceCoverageOneRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    resource_id: str
    r"""ID of the resource you are acting upon."""


class ConnectorAPIResourceCoverageOneRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    resource_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the resource you are acting upon."""


class ConnectorAPIResourceCoverageOneResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    get_api_resource_coverage_response: NotRequired[
        GetAPIResourceCoverageResponseTypedDict
    ]
    r"""ApiResources"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class ConnectorAPIResourceCoverageOneResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    get_api_resource_coverage_response: Optional[GetAPIResourceCoverageResponse] = None
    r"""ApiResources"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""