"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .gettimeoffrequestresponse import (
    GetTimeOffRequestResponse,
    GetTimeOffRequestResponseTypedDict,
)
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class HrisTimeOffRequestsOneGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class HrisTimeOffRequestsOneGlobals(BaseModel):
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


class HrisTimeOffRequestsOneRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    employee_id: str
    r"""ID of the employee you are acting upon."""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    fields: NotRequired[Nullable[str]]
    r"""The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded."""


class HrisTimeOffRequestsOneRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the employee you are acting upon."""

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

    fields: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["serviceId", "raw", "fields"]
        nullable_fields = ["fields"]
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


class HrisTimeOffRequestsOneResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    get_time_off_request_response: NotRequired[GetTimeOffRequestResponseTypedDict]
    r"""TimeOffRequests"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class HrisTimeOffRequestsOneResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    get_time_off_request_response: Optional[GetTimeOffRequestResponse] = None
    r"""TimeOffRequests"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
