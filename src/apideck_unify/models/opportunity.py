"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currency import Currency
from .customfield import CustomField, CustomFieldTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import date, datetime
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OpportunityTypedDict(TypedDict):
    title: str
    r"""The title or name of the opportunity."""
    primary_contact_id: Nullable[str]
    r"""The unique identifier of the primary contact associated with the opportunity."""
    id: NotRequired[str]
    r"""A unique identifier for the opportunity."""
    description: NotRequired[Nullable[str]]
    r"""A description of the opportunity."""
    type: NotRequired[Nullable[str]]
    r"""The type of the opportunity"""
    monetary_amount: NotRequired[Nullable[float]]
    r"""The monetary value associated with the opportunity"""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    win_probability: NotRequired[Nullable[float]]
    r"""The probability of winning the opportunity, expressed as a percentage."""
    expected_revenue: NotRequired[Nullable[float]]
    r"""The expected revenue from the opportunity"""
    close_date: NotRequired[Nullable[date]]
    r"""The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet."""
    loss_reason_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the reason why the opportunity was lost."""
    loss_reason: NotRequired[Nullable[str]]
    r"""The reason why the opportunity was lost."""
    won_reason_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the reason why the opportunity was won."""
    won_reason: NotRequired[Nullable[str]]
    r"""The reason why the opportunity was won."""
    pipeline_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the pipeline associated with the opportunity"""
    pipeline_stage_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the stage in the pipeline associated with the opportunity."""
    source_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the source of the opportunity."""
    lead_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the lead associated with the opportunity."""
    lead_source: NotRequired[Nullable[str]]
    r"""The source of the lead associated with the opportunity."""
    contact_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the contact associated with the opportunity."""
    contact_ids: NotRequired[List[str]]
    r"""An array of unique identifiers of all contacts associated with the opportunity."""
    company_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the company associated with the opportunity."""
    company_name: NotRequired[Nullable[str]]
    r"""The name of the company associated with the opportunity."""
    owner_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the user who owns the opportunity."""
    priority: NotRequired[Nullable[str]]
    r"""The priority level of the opportunity."""
    status: NotRequired[Nullable[str]]
    r"""The current status of the opportunity."""
    status_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the current status of the opportunity."""
    tags: NotRequired[Nullable[List[str]]]
    interaction_count: NotRequired[Nullable[float]]
    r"""The number of interactions with the opportunity."""
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    stage_last_changed_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the stage of the opportunity was last changed."""
    last_activity_at: NotRequired[Nullable[str]]
    r"""The date and time of the last activity associated with the opportunity."""
    deleted: NotRequired[bool]
    r"""Indicates whether the opportunity has been deleted."""
    date_stage_changed: NotRequired[Nullable[datetime]]
    r"""The date and time when the stage of the opportunity was last changed."""
    date_last_contacted: NotRequired[Nullable[datetime]]
    r"""The date and time when the opportunity was last contacted."""
    date_lead_created: NotRequired[Nullable[datetime]]
    r"""The date and time when the lead associated with the opportunity was created."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    updated_by: NotRequired[Nullable[str]]
    r"""The unique identifier of the user who last updated the opportunity."""
    created_by: NotRequired[Nullable[str]]
    r"""The unique identifier of the user who created the opportunity."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the opportunity was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the opportunity was created."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class Opportunity(BaseModel):
    title: str
    r"""The title or name of the opportunity."""

    primary_contact_id: Nullable[str]
    r"""The unique identifier of the primary contact associated with the opportunity."""

    id: Optional[str] = None
    r"""A unique identifier for the opportunity."""

    description: OptionalNullable[str] = UNSET
    r"""A description of the opportunity."""

    type: OptionalNullable[str] = UNSET
    r"""The type of the opportunity"""

    monetary_amount: OptionalNullable[float] = UNSET
    r"""The monetary value associated with the opportunity"""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    win_probability: OptionalNullable[float] = UNSET
    r"""The probability of winning the opportunity, expressed as a percentage."""

    expected_revenue: OptionalNullable[float] = UNSET
    r"""The expected revenue from the opportunity"""

    close_date: OptionalNullable[date] = UNSET
    r"""The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet."""

    loss_reason_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the reason why the opportunity was lost."""

    loss_reason: OptionalNullable[str] = UNSET
    r"""The reason why the opportunity was lost."""

    won_reason_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the reason why the opportunity was won."""

    won_reason: OptionalNullable[str] = UNSET
    r"""The reason why the opportunity was won."""

    pipeline_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the pipeline associated with the opportunity"""

    pipeline_stage_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the stage in the pipeline associated with the opportunity."""

    source_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the source of the opportunity."""

    lead_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the lead associated with the opportunity."""

    lead_source: OptionalNullable[str] = UNSET
    r"""The source of the lead associated with the opportunity."""

    contact_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the contact associated with the opportunity."""

    contact_ids: Optional[List[str]] = None
    r"""An array of unique identifiers of all contacts associated with the opportunity."""

    company_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the company associated with the opportunity."""

    company_name: OptionalNullable[str] = UNSET
    r"""The name of the company associated with the opportunity."""

    owner_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the user who owns the opportunity."""

    priority: OptionalNullable[str] = UNSET
    r"""The priority level of the opportunity."""

    status: OptionalNullable[str] = UNSET
    r"""The current status of the opportunity."""

    status_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the current status of the opportunity."""

    tags: OptionalNullable[List[str]] = UNSET

    interaction_count: OptionalNullable[float] = UNSET
    r"""The number of interactions with the opportunity."""

    custom_fields: Optional[List[CustomField]] = None

    stage_last_changed_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the stage of the opportunity was last changed."""

    last_activity_at: OptionalNullable[str] = UNSET
    r"""The date and time of the last activity associated with the opportunity."""

    deleted: Optional[bool] = None
    r"""Indicates whether the opportunity has been deleted."""

    date_stage_changed: OptionalNullable[datetime] = UNSET
    r"""The date and time when the stage of the opportunity was last changed."""

    date_last_contacted: OptionalNullable[datetime] = UNSET
    r"""The date and time when the opportunity was last contacted."""

    date_lead_created: OptionalNullable[datetime] = UNSET
    r"""The date and time when the lead associated with the opportunity was created."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The unique identifier of the user who last updated the opportunity."""

    created_by: OptionalNullable[str] = UNSET
    r"""The unique identifier of the user who created the opportunity."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the opportunity was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the opportunity was created."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "description",
            "type",
            "monetary_amount",
            "currency",
            "win_probability",
            "expected_revenue",
            "close_date",
            "loss_reason_id",
            "loss_reason",
            "won_reason_id",
            "won_reason",
            "pipeline_id",
            "pipeline_stage_id",
            "source_id",
            "lead_id",
            "lead_source",
            "contact_id",
            "contact_ids",
            "company_id",
            "company_name",
            "owner_id",
            "priority",
            "status",
            "status_id",
            "tags",
            "interaction_count",
            "custom_fields",
            "stage_last_changed_at",
            "last_activity_at",
            "deleted",
            "date_stage_changed",
            "date_last_contacted",
            "date_lead_created",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "primary_contact_id",
            "description",
            "type",
            "monetary_amount",
            "currency",
            "win_probability",
            "expected_revenue",
            "close_date",
            "loss_reason_id",
            "loss_reason",
            "won_reason_id",
            "won_reason",
            "pipeline_id",
            "pipeline_stage_id",
            "source_id",
            "lead_id",
            "lead_source",
            "contact_id",
            "company_id",
            "company_name",
            "owner_id",
            "priority",
            "status",
            "status_id",
            "tags",
            "interaction_count",
            "stage_last_changed_at",
            "last_activity_at",
            "date_stage_changed",
            "date_last_contacted",
            "date_lead_created",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
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