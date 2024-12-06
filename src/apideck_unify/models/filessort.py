"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sortdirection import SortDirection
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FilesSortBy(str, Enum):
    r"""The field on which to sort the Files"""

    UPDATED_AT = "updated_at"
    NAME = "name"


class FilesSortTypedDict(TypedDict):
    by: NotRequired[FilesSortBy]
    r"""The field on which to sort the Files"""
    direction: NotRequired[SortDirection]
    r"""The direction in which to sort the results"""


class FilesSort(BaseModel):
    by: Annotated[Optional[FilesSortBy], FieldMetadata(query=True)] = None
    r"""The field on which to sort the Files"""

    direction: Annotated[Optional[SortDirection], FieldMetadata(query=True)] = (
        SortDirection.ASC
    )
    r"""The direction in which to sort the results"""
