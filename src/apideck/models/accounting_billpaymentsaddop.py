"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .billpayment import BillPaymentInput, BillPaymentInputTypedDict
from .createbillpaymentresponse import (
    CreateBillPaymentResponse,
    CreateBillPaymentResponseTypedDict,
)
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingBillPaymentsAddGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingBillPaymentsAddGlobals(BaseModel):
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


class AccountingBillPaymentsAddRequestTypedDict(TypedDict):
    bill_payment: BillPaymentInputTypedDict
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


class AccountingBillPaymentsAddRequest(BaseModel):
    bill_payment: Annotated[
        BillPaymentInput,
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


class AccountingBillPaymentsAddResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    create_bill_payment_response: NotRequired[CreateBillPaymentResponseTypedDict]
    r"""Bill Payment created"""
    unexpected_error_response: NotRequired[UnexpectedErrorResponseTypedDict]
    r"""Unexpected error"""


class AccountingBillPaymentsAddResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    create_bill_payment_response: Optional[CreateBillPaymentResponse] = None
    r"""Bill Payment created"""

    unexpected_error_response: Optional[UnexpectedErrorResponse] = None
    r"""Unexpected error"""
