"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconsumersresponse import GetConsumersResponse, GetConsumersResponseTypedDict
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
from typing import Callable, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConsumersAllGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConsumersAllGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class VaultConsumersAllRequestTypedDict(TypedDict):
    cursor: NotRequired[Nullable[str]]
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""
    limit: NotRequired[int]
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""


class VaultConsumersAllRequest(BaseModel):
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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cursor", "limit"]
        nullable_fields = ["cursor"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


VaultConsumersAllResponseResultTypedDict = TypeAliasType(
    "VaultConsumersAllResponseResultTypedDict",
    Union[GetConsumersResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConsumersAllResponseResult = TypeAliasType(
    "VaultConsumersAllResponseResult",
    Union[GetConsumersResponse, UnexpectedErrorResponse],
)


class VaultConsumersAllResponseTypedDict(TypedDict):
    result: VaultConsumersAllResponseResultTypedDict


class VaultConsumersAllResponse(BaseModel):
    next: Callable[[], Optional[VaultConsumersAllResponse]]

    result: VaultConsumersAllResponseResult
