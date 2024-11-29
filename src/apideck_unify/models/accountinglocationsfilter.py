"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck_unify.types import BaseModel
from apideck_unify.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingLocationsFilterTypedDict(TypedDict):
    subsidiary: NotRequired[str]
    r"""Id of the subsidiary to search for"""


class AccountingLocationsFilter(BaseModel):
    subsidiary: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Id of the subsidiary to search for"""