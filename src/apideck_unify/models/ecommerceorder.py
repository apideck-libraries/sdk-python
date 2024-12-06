"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .ecommerceaddress import EcommerceAddress, EcommerceAddressTypedDict
from .ecommercediscount import EcommerceDiscount, EcommerceDiscountTypedDict
from .ecommerceorderlineitem import (
    EcommerceOrderLineItem,
    EcommerceOrderLineItemTypedDict,
)
from .ecommerceorderstatus import EcommerceOrderStatus
from .linkedecommercecustomer import (
    LinkedEcommerceCustomer,
    LinkedEcommerceCustomerTypedDict,
)
from .trackingitem import TrackingItem, TrackingItemTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class EcommerceOrderPaymentStatus(str, Enum):
    r"""Current payment status of the order."""

    PENDING = "pending"
    AUTHORIZED = "authorized"
    PAID = "paid"
    PARTIAL = "partial"
    REFUNDED = "refunded"
    VOIDED = "voided"
    UNKNOWN = "unknown"


class FulfillmentStatus(str, Enum):
    r"""Current fulfillment status of the order."""

    PENDING = "pending"
    SHIPPED = "shipped"
    PARTIAL = "partial"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"
    UNKNOWN = "unknown"


class EcommerceOrderTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    order_number: NotRequired[Nullable[str]]
    r"""Order number, if any."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    discounts: NotRequired[List[EcommerceDiscountTypedDict]]
    sub_total: NotRequired[Nullable[str]]
    r"""Sub-total amount, normally before tax."""
    shipping_cost: NotRequired[Nullable[str]]
    r"""Shipping cost, if any."""
    coupon_discount: NotRequired[Nullable[str]]
    r"""Coupon discount, if any."""
    total_discount: NotRequired[Nullable[str]]
    r"""Total discount, if any."""
    total_tax: NotRequired[Nullable[str]]
    r"""Total tax, if any."""
    total_amount: NotRequired[Nullable[str]]
    r"""Total amount due."""
    refunded_amount: NotRequired[Nullable[str]]
    r"""Refunded amount, if any."""
    status: NotRequired[Nullable[EcommerceOrderStatus]]
    r"""Current status of the order."""
    payment_status: NotRequired[Nullable[EcommerceOrderPaymentStatus]]
    r"""Current payment status of the order."""
    fulfillment_status: NotRequired[Nullable[FulfillmentStatus]]
    r"""Current fulfillment status of the order."""
    payment_method: NotRequired[Nullable[str]]
    r"""Payment method used for this order."""
    customer: NotRequired[LinkedEcommerceCustomerTypedDict]
    r"""The customer this entity is linked to."""
    billing_address: NotRequired[EcommerceAddressTypedDict]
    r"""An object representing a shipping or billing address."""
    shipping_address: NotRequired[EcommerceAddressTypedDict]
    r"""An object representing a shipping or billing address."""
    tracking: NotRequired[List[TrackingItemTypedDict]]
    line_items: NotRequired[List[EcommerceOrderLineItemTypedDict]]
    note: NotRequired[Nullable[str]]
    r"""Note for the order."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""


class EcommerceOrder(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    order_number: OptionalNullable[str] = UNSET
    r"""Order number, if any."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    discounts: Optional[List[EcommerceDiscount]] = None

    sub_total: OptionalNullable[str] = UNSET
    r"""Sub-total amount, normally before tax."""

    shipping_cost: OptionalNullable[str] = UNSET
    r"""Shipping cost, if any."""

    coupon_discount: OptionalNullable[str] = UNSET
    r"""Coupon discount, if any."""

    total_discount: OptionalNullable[str] = UNSET
    r"""Total discount, if any."""

    total_tax: OptionalNullable[str] = UNSET
    r"""Total tax, if any."""

    total_amount: OptionalNullable[str] = UNSET
    r"""Total amount due."""

    refunded_amount: OptionalNullable[str] = UNSET
    r"""Refunded amount, if any."""

    status: OptionalNullable[EcommerceOrderStatus] = UNSET
    r"""Current status of the order."""

    payment_status: OptionalNullable[EcommerceOrderPaymentStatus] = UNSET
    r"""Current payment status of the order."""

    fulfillment_status: OptionalNullable[FulfillmentStatus] = UNSET
    r"""Current fulfillment status of the order."""

    payment_method: OptionalNullable[str] = UNSET
    r"""Payment method used for this order."""

    customer: Optional[LinkedEcommerceCustomer] = None
    r"""The customer this entity is linked to."""

    billing_address: Optional[EcommerceAddress] = None
    r"""An object representing a shipping or billing address."""

    shipping_address: Optional[EcommerceAddress] = None
    r"""An object representing a shipping or billing address."""

    tracking: Optional[List[TrackingItem]] = None

    line_items: Optional[List[EcommerceOrderLineItem]] = None

    note: OptionalNullable[str] = UNSET
    r"""Note for the order."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "order_number",
            "currency",
            "discounts",
            "sub_total",
            "shipping_cost",
            "coupon_discount",
            "total_discount",
            "total_tax",
            "total_amount",
            "refunded_amount",
            "status",
            "payment_status",
            "fulfillment_status",
            "payment_method",
            "customer",
            "billing_address",
            "shipping_address",
            "tracking",
            "line_items",
            "note",
            "custom_mappings",
            "created_at",
            "updated_at",
        ]
        nullable_fields = [
            "order_number",
            "currency",
            "sub_total",
            "shipping_cost",
            "coupon_discount",
            "total_discount",
            "total_tax",
            "total_amount",
            "refunded_amount",
            "status",
            "payment_status",
            "fulfillment_status",
            "payment_method",
            "note",
            "custom_mappings",
            "created_at",
            "updated_at",
        ]
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
