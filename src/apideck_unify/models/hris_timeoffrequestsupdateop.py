"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .timeoffrequest import TimeOffRequestInput, TimeOffRequestInputTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updatetimeoffrequestresponse import (
    UpdateTimeOffRequestResponse,
    UpdateTimeOffRequestResponseTypedDict,
)
from apideck_unify.types import BaseModel
from apideck_unify.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class HrisTimeOffRequestsUpdateGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class HrisTimeOffRequestsUpdateGlobals(BaseModel):
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


class HrisTimeOffRequestsUpdateRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    employee_id_param: str
    r"""ID of the employee you are acting upon."""
    time_off_request: TimeOffRequestInputTypedDict
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class HrisTimeOffRequestsUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    employee_id_param: Annotated[
        str,
        pydantic.Field(alias="employee_id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of the employee you are acting upon."""

    time_off_request: Annotated[
        TimeOffRequestInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

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

    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""


class HrisTimeOffRequestsUpdateResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    update_time_off_request_response: NotRequired[UpdateTimeOffRequestResponseTypedDict]
    r"""TimeOffRequests"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class HrisTimeOffRequestsUpdateResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    update_time_off_request_response: Optional[UpdateTimeOffRequestResponse] = None
    r"""TimeOffRequests"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
