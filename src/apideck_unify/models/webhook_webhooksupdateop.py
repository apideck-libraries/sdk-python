"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updatewebhookrequest import UpdateWebhookRequest, UpdateWebhookRequestTypedDict
from .updatewebhookresponse import UpdateWebhookResponse, UpdateWebhookResponseTypedDict
from apideck_unify.types import BaseModel
from apideck_unify.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WebhookWebhooksUpdateGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class WebhookWebhooksUpdateGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class WebhookWebhooksUpdateRequestTypedDict(TypedDict):
    id: str
    r"""JWT Webhook token that represents the unifiedApi and applicationId associated to the event source."""
    update_webhook_request: UpdateWebhookRequestTypedDict
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class WebhookWebhooksUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""JWT Webhook token that represents the unifiedApi and applicationId associated to the event source."""

    update_webhook_request: Annotated[
        UpdateWebhookRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class WebhookWebhooksUpdateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    update_webhook_response: NotRequired[UpdateWebhookResponseTypedDict]
    r"""Webhooks"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class WebhookWebhooksUpdateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    update_webhook_response: Optional[UpdateWebhookResponse] = None
    r"""Webhooks"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
