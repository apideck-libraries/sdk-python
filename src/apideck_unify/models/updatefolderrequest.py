"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck_unify.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class UpdateFolderRequestTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the folder."""
    description: NotRequired[str]
    r"""Optional description of the folder."""
    parent_folder_id: NotRequired[str]
    r"""The parent folder to create the new file within. This can be an ID or a path depending on the downstream folder. Please see the connector section below to see downstream specific gotchas."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class UpdateFolderRequest(BaseModel):
    name: Optional[str] = None
    r"""The name of the folder."""

    description: Optional[str] = None
    r"""Optional description of the folder."""

    parent_folder_id: Optional[str] = None
    r"""The parent folder to create the new file within. This can be an ID or a path depending on the downstream folder. Please see the connector section below to see downstream specific gotchas."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""
