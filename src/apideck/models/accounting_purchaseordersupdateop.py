"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .purchaseorder import PurchaseOrderInput, PurchaseOrderInputTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from .updatepurchaseorderresponse import (
    UpdatePurchaseOrderResponse,
    UpdatePurchaseOrderResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class AccountingPurchaseOrdersUpdateGlobalsTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingPurchaseOrdersUpdateGlobals(BaseModel):
    customer_id: Annotated[
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


class AccountingPurchaseOrdersUpdateRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""
    purchase_order: PurchaseOrderInputTypedDict
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""


class AccountingPurchaseOrdersUpdateRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""

    purchase_order: Annotated[
        PurchaseOrderInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

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


AccountingPurchaseOrdersUpdateResponseTypedDict = TypeAliasType(
    "AccountingPurchaseOrdersUpdateResponseTypedDict",
    Union[UpdatePurchaseOrderResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


AccountingPurchaseOrdersUpdateResponse = TypeAliasType(
    "AccountingPurchaseOrdersUpdateResponse",
    Union[UpdatePurchaseOrderResponse, UnexpectedErrorResponse],
)