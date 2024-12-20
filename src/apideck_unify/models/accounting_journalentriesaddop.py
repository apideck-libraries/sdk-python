"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createjournalentryresponse import (
    CreateJournalEntryResponse,
    CreateJournalEntryResponseTypedDict,
)
from .journalentry_input import JournalEntryInput, JournalEntryInputTypedDict
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
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class AccountingJournalEntriesAddGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingJournalEntriesAddGlobals(BaseModel):
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


class AccountingJournalEntriesAddRequestTypedDict(TypedDict):
    journal_entry: JournalEntryInputTypedDict
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


class AccountingJournalEntriesAddRequest(BaseModel):
    journal_entry: Annotated[
        JournalEntryInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""

    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


AccountingJournalEntriesAddResponseTypedDict = TypeAliasType(
    "AccountingJournalEntriesAddResponseTypedDict",
    Union[CreateJournalEntryResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


AccountingJournalEntriesAddResponse = TypeAliasType(
    "AccountingJournalEntriesAddResponse",
    Union[CreateJournalEntryResponse, UnexpectedErrorResponse],
)
