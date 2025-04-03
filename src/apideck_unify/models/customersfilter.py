"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from apideck_unify.utils import FieldMetadata
from datetime import datetime
from enum import Enum
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomersFilterStatus(str, Enum):
    r"""Status of customer to filter on"""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
    ALL = "all"


class CustomersFilterTypedDict(TypedDict):
    company_name: NotRequired[str]
    r"""Company Name of customer to search for"""
    display_name: NotRequired[str]
    r"""Display Name of customer to search for"""
    first_name: NotRequired[str]
    r"""First name of customer to search for"""
    last_name: NotRequired[str]
    r"""Last name of customer to search for"""
    email: NotRequired[str]
    r"""Email of customer to search for"""
    status: NotRequired[Nullable[CustomersFilterStatus]]
    r"""Status of customer to filter on"""
    updated_since: NotRequired[datetime]
    supplier_id: NotRequired[str]
    r"""Supplier ID of customer to search for"""


class CustomersFilter(BaseModel):
    company_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Company Name of customer to search for"""

    display_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Display Name of customer to search for"""

    first_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""First name of customer to search for"""

    last_name: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Last name of customer to search for"""

    email: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Email of customer to search for"""

    status: Annotated[
        OptionalNullable[CustomersFilterStatus], FieldMetadata(query=True)
    ] = UNSET
    r"""Status of customer to filter on"""

    updated_since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None

    supplier_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Supplier ID of customer to search for"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "company_name",
            "display_name",
            "first_name",
            "last_name",
            "email",
            "status",
            "updated_since",
            "supplier_id",
        ]
        nullable_fields = ["status"]
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
