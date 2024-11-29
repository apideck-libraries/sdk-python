"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .linkedtaxrate import LinkedTaxRate, LinkedTaxRateTypedDict
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ExpenseLineItemTypedDict(TypedDict):
    total_amount: Nullable[float]
    r"""The total amount of the expense line item."""
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    account_id: NotRequired[str]
    r"""The unique identifier for the ledger account."""
    customer_id: NotRequired[str]
    r"""The ID of the customer this expense item is linked to."""
    department_id: NotRequired[str]
    r"""The ID of the department this expense item is linked to."""
    location_id: NotRequired[str]
    r"""The ID of the location this expense item is linked to."""
    tax_rate: NotRequired[LinkedTaxRateTypedDict]
    description: NotRequired[Nullable[str]]
    r"""The expense line item description"""
    billable: NotRequired[bool]
    r"""Boolean that indicates if the line item is billable or not."""


class ExpenseLineItem(BaseModel):
    total_amount: Nullable[float]
    r"""The total amount of the expense line item."""

    id: Optional[str] = None
    r"""A unique identifier for an object."""

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    account_id: Optional[str] = None
    r"""The unique identifier for the ledger account."""

    customer_id: Optional[str] = None
    r"""The ID of the customer this expense item is linked to."""

    department_id: Optional[str] = None
    r"""The ID of the department this expense item is linked to."""

    location_id: Optional[str] = None
    r"""The ID of the location this expense item is linked to."""

    tax_rate: Optional[LinkedTaxRate] = None

    description: OptionalNullable[str] = UNSET
    r"""The expense line item description"""

    billable: Optional[bool] = None
    r"""Boolean that indicates if the line item is billable or not."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "tracking_categories",
            "account_id",
            "customer_id",
            "department_id",
            "location_id",
            "tax_rate",
            "description",
            "billable",
        ]
        nullable_fields = ["total_amount", "tracking_categories", "description"]
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