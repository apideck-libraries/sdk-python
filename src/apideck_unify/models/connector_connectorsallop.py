"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectorsfilter import ConnectorsFilter, ConnectorsFilterTypedDict
from .getconnectorsresponse import GetConnectorsResponse, GetConnectorsResponseTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from apideck_unify.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConnectorConnectorsAllGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class ConnectorConnectorsAllGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class ConnectorConnectorsAllRequestTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    cursor: NotRequired[Nullable[str]]
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""
    limit: NotRequired[int]
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""
    filter_: NotRequired[ConnectorsFilterTypedDict]
    r"""Apply filters"""


class ConnectorConnectorsAllRequest(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""

    cursor: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""

    filter_: Annotated[
        Optional[ConnectorsFilter],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Apply filters"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["appId", "cursor", "limit", "filter"]
        nullable_fields = ["cursor"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class ConnectorConnectorsAllResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    get_connectors_response: NotRequired[GetConnectorsResponseTypedDict]
    r"""Connectors"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class ConnectorConnectorsAllResponse(BaseModel):
    next: Callable[[], Optional[ConnectorConnectorsAllResponse]]

    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    get_connectors_response: Optional[GetConnectorsResponse] = None
    r"""Connectors"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
