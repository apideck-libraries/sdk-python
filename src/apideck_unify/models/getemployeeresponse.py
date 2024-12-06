"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .employee import Employee, EmployeeTypedDict
from apideck_unify.types import BaseModel
from typing_extensions import TypedDict


class GetEmployeeResponseTypedDict(TypedDict):
    r"""Employees"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    service: str
    r"""Apideck ID of service provider"""
    resource: str
    r"""Unified API resource name"""
    operation: str
    r"""Operation performed"""
    data: EmployeeTypedDict


class GetEmployeeResponse(BaseModel):
    r"""Employees"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    service: str
    r"""Apideck ID of service provider"""

    resource: str
    r"""Unified API resource name"""

    operation: str
    r"""Operation performed"""

    data: Employee
