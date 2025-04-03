"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .journalentrylineitem import (
    JournalEntryLineItemInput,
    JournalEntryLineItemInputTypedDict,
)
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import datetime
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class JournalEntryInputTypedDict(TypedDict):
    title: NotRequired[Nullable[str]]
    r"""Journal entry title"""
    currency_rate: NotRequired[Nullable[float]]
    r"""Currency Exchange Rate at the time entity was recorded/generated."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    company_id: NotRequired[Nullable[str]]
    r"""The company or subsidiary id the transaction belongs to"""
    line_items: NotRequired[List[JournalEntryLineItemInputTypedDict]]
    r"""Requires a minimum of 2 line items that sum to 0"""
    memo: NotRequired[Nullable[str]]
    r"""Reference for the journal entry."""
    posted_at: NotRequired[datetime]
    r"""This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated."""
    journal_symbol: NotRequired[Nullable[str]]
    r"""Journal symbol of the entry. For example IND for indirect costs"""
    tax_type: NotRequired[Nullable[str]]
    r"""The specific category of tax associated with a transaction like sales or purchase"""
    tax_code: NotRequired[Nullable[str]]
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""
    number: NotRequired[Nullable[str]]
    r"""Journal entry number."""
    tracking_categories: NotRequired[
        Nullable[List[Nullable[LinkedTrackingCategoryTypedDict]]]
    ]
    r"""A list of linked tracking categories."""
    accounting_period: NotRequired[Nullable[str]]
    r"""Accounting period"""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class JournalEntryInput(BaseModel):
    title: OptionalNullable[str] = UNSET
    r"""Journal entry title"""

    currency_rate: OptionalNullable[float] = UNSET
    r"""Currency Exchange Rate at the time entity was recorded/generated."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    company_id: OptionalNullable[str] = UNSET
    r"""The company or subsidiary id the transaction belongs to"""

    line_items: Optional[List[JournalEntryLineItemInput]] = None
    r"""Requires a minimum of 2 line items that sum to 0"""

    memo: OptionalNullable[str] = UNSET
    r"""Reference for the journal entry."""

    posted_at: Optional[datetime] = None
    r"""This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated."""

    journal_symbol: OptionalNullable[str] = UNSET
    r"""Journal symbol of the entry. For example IND for indirect costs"""

    tax_type: OptionalNullable[str] = UNSET
    r"""The specific category of tax associated with a transaction like sales or purchase"""

    tax_code: OptionalNullable[str] = UNSET
    r"""Applicable tax id/code override if tax is not supplied on a line item basis."""

    number: OptionalNullable[str] = UNSET
    r"""Journal entry number."""

    tracking_categories: OptionalNullable[List[Nullable[LinkedTrackingCategory]]] = (
        UNSET
    )
    r"""A list of linked tracking categories."""

    accounting_period: OptionalNullable[str] = UNSET
    r"""Accounting period"""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    custom_fields: Optional[List[CustomField]] = None

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "title",
            "currency_rate",
            "currency",
            "company_id",
            "line_items",
            "memo",
            "posted_at",
            "journal_symbol",
            "tax_type",
            "tax_code",
            "number",
            "tracking_categories",
            "accounting_period",
            "row_version",
            "custom_fields",
            "pass_through",
        ]
        nullable_fields = [
            "title",
            "currency_rate",
            "currency",
            "company_id",
            "memo",
            "journal_symbol",
            "tax_type",
            "tax_code",
            "number",
            "tracking_categories",
            "accounting_period",
            "row_version",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
