"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EmployeesFilterEmploymentStatus(str, Enum):
    r"""Employment status to filter on"""

    ACTIVE = "active"
    INACTIVE = "inactive"
    TERMINATED = "terminated"
    OTHER = "other"


class EmployeesFilterTypedDict(TypedDict):
    company_id: NotRequired[str]
    r"""Company ID to filter on"""
    email: NotRequired[str]
    r"""Email to filter on"""
    first_name: NotRequired[str]
    r"""First Name to filter on"""
    title: NotRequired[str]
    r"""Job title to filter on"""
    last_name: NotRequired[str]
    r"""Last Name to filter on"""
    manager_id: NotRequired[str]
    r"""Manager id to filter on"""
    employment_status: NotRequired[EmployeesFilterEmploymentStatus]
    r"""Employment status to filter on"""
    employee_number: NotRequired[str]
    r"""Employee number to filter on"""
    department_id: NotRequired[str]
    r"""ID of the department to filter on"""
    city: NotRequired[str]
    r"""City to filter on"""
    country: NotRequired[str]
    r"""Country to filter on"""


class EmployeesFilter(BaseModel):
    company_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Company ID to filter on"""

    email: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Email to filter on"""

    first_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""First Name to filter on"""

    title: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Job title to filter on"""

    last_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Last Name to filter on"""

    manager_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Manager id to filter on"""

    employment_status: Annotated[
        Optional[EmployeesFilterEmploymentStatus], FieldMetadata(query=True)
    ] = None
    r"""Employment status to filter on"""

    employee_number: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Employee number to filter on"""

    department_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""ID of the department to filter on"""

    city: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""City to filter on"""

    country: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Country to filter on"""
