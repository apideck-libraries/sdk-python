"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ConnectorConnectorDocsOneGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class ConnectorConnectorDocsOneGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class ConnectorConnectorDocsOneRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    doc_id: str
    r"""ID of the Doc"""


class ConnectorConnectorDocsOneRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    doc_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Doc"""


ConnectorConnectorDocsOneResponseTypedDict = TypeAliasType(
    "ConnectorConnectorDocsOneResponseTypedDict",
    Union[UnexpectedErrorResponseTypedDict, str],
)


ConnectorConnectorDocsOneResponse = TypeAliasType(
    "ConnectorConnectorDocsOneResponse", Union[UnexpectedErrorResponse, str]
)
