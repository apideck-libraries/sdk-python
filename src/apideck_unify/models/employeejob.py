"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .currency import Currency
from .paymentunit import PaymentUnit
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from datetime import date
from enum import Enum
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EmployeeJobStatus(str, Enum):
    r"""Indicates the status of the job."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"


class EmployeeJobTypedDict(TypedDict):
    id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    employee_id: NotRequired[Nullable[str]]
    r"""A unique identifier for an object."""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    role: NotRequired[Nullable[str]]
    r"""The position and responsibilities of the person within the organization."""
    start_date: NotRequired[Nullable[date]]
    r"""The date on which the employee starts working in their current job role."""
    end_date: NotRequired[Nullable[date]]
    r"""The date on which the employee leaves or is expected to leave their current job role."""
    compensation_rate: NotRequired[Nullable[float]]
    r"""The rate of pay for the employee in their current job role."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    payment_unit: NotRequired[Nullable[PaymentUnit]]
    r"""Unit of measurement for employee compensation."""
    hired_at: NotRequired[Nullable[date]]
    r"""The date on which the employee was hired by the organization"""
    is_primary: NotRequired[Nullable[bool]]
    r"""Indicates whether this the employee's primary job."""
    is_manager: NotRequired[Nullable[bool]]
    r"""Indicates whether this the employee has a manager role."""
    status: NotRequired[Nullable[EmployeeJobStatus]]
    r"""Indicates the status of the job."""
    location: NotRequired[AddressTypedDict]


class EmployeeJob(BaseModel):
    id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    employee_id: OptionalNullable[str] = UNSET
    r"""A unique identifier for an object."""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    role: OptionalNullable[str] = UNSET
    r"""The position and responsibilities of the person within the organization."""

    start_date: OptionalNullable[date] = UNSET
    r"""The date on which the employee starts working in their current job role."""

    end_date: OptionalNullable[date] = UNSET
    r"""The date on which the employee leaves or is expected to leave their current job role."""

    compensation_rate: OptionalNullable[float] = UNSET
    r"""The rate of pay for the employee in their current job role."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    payment_unit: OptionalNullable[PaymentUnit] = UNSET
    r"""Unit of measurement for employee compensation."""

    hired_at: OptionalNullable[date] = UNSET
    r"""The date on which the employee was hired by the organization"""

    is_primary: OptionalNullable[bool] = UNSET
    r"""Indicates whether this the employee's primary job."""

    is_manager: OptionalNullable[bool] = UNSET
    r"""Indicates whether this the employee has a manager role."""

    status: OptionalNullable[EmployeeJobStatus] = UNSET
    r"""Indicates the status of the job."""

    location: Optional[Address] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "employee_id",
            "title",
            "role",
            "start_date",
            "end_date",
            "compensation_rate",
            "currency",
            "payment_unit",
            "hired_at",
            "is_primary",
            "is_manager",
            "status",
            "location",
        ]
        nullable_fields = [
            "id",
            "employee_id",
            "title",
            "role",
            "start_date",
            "end_date",
            "compensation_rate",
            "currency",
            "payment_unit",
            "hired_at",
            "is_primary",
            "is_manager",
            "status",
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


class EmployeeJobInputTypedDict(TypedDict):
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    role: NotRequired[Nullable[str]]
    r"""The position and responsibilities of the person within the organization."""
    start_date: NotRequired[Nullable[date]]
    r"""The date on which the employee starts working in their current job role."""
    end_date: NotRequired[Nullable[date]]
    r"""The date on which the employee leaves or is expected to leave their current job role."""
    compensation_rate: NotRequired[Nullable[float]]
    r"""The rate of pay for the employee in their current job role."""
    currency: NotRequired[Nullable[Currency]]
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""
    payment_unit: NotRequired[Nullable[PaymentUnit]]
    r"""Unit of measurement for employee compensation."""
    hired_at: NotRequired[Nullable[date]]
    r"""The date on which the employee was hired by the organization"""
    is_primary: NotRequired[Nullable[bool]]
    r"""Indicates whether this the employee's primary job."""
    is_manager: NotRequired[Nullable[bool]]
    r"""Indicates whether this the employee has a manager role."""
    status: NotRequired[Nullable[EmployeeJobStatus]]
    r"""Indicates the status of the job."""
    location: NotRequired[AddressTypedDict]


class EmployeeJobInput(BaseModel):
    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    role: OptionalNullable[str] = UNSET
    r"""The position and responsibilities of the person within the organization."""

    start_date: OptionalNullable[date] = UNSET
    r"""The date on which the employee starts working in their current job role."""

    end_date: OptionalNullable[date] = UNSET
    r"""The date on which the employee leaves or is expected to leave their current job role."""

    compensation_rate: OptionalNullable[float] = UNSET
    r"""The rate of pay for the employee in their current job role."""

    currency: OptionalNullable[Currency] = UNSET
    r"""Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217)."""

    payment_unit: OptionalNullable[PaymentUnit] = UNSET
    r"""Unit of measurement for employee compensation."""

    hired_at: OptionalNullable[date] = UNSET
    r"""The date on which the employee was hired by the organization"""

    is_primary: OptionalNullable[bool] = UNSET
    r"""Indicates whether this the employee's primary job."""

    is_manager: OptionalNullable[bool] = UNSET
    r"""Indicates whether this the employee has a manager role."""

    status: OptionalNullable[EmployeeJobStatus] = UNSET
    r"""Indicates the status of the job."""

    location: Optional[Address] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "title",
            "role",
            "start_date",
            "end_date",
            "compensation_rate",
            "currency",
            "payment_unit",
            "hired_at",
            "is_primary",
            "is_manager",
            "status",
            "location",
        ]
        nullable_fields = [
            "title",
            "role",
            "start_date",
            "end_date",
            "compensation_rate",
            "currency",
            "payment_unit",
            "hired_at",
            "is_primary",
            "is_manager",
            "status",
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