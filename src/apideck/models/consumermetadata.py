"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ConsumerMetadataTypedDict(TypedDict):
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""

    account_name: NotRequired[str]
    r"""The name of the account as shown in the sidebar."""
    user_name: NotRequired[str]
    r"""The name of the user as shown in the sidebar."""
    email: NotRequired[str]
    r"""The email of the user as shown in the sidebar."""
    image: NotRequired[str]
    r"""The avatar of the user in the sidebar. Must be a valid URL"""


class ConsumerMetadata(BaseModel):
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""

    account_name: Optional[str] = None
    r"""The name of the account as shown in the sidebar."""

    user_name: Optional[str] = None
    r"""The name of the user as shown in the sidebar."""

    email: Optional[str] = None
    r"""The email of the user as shown in the sidebar."""

    image: Optional[str] = None
    r"""The avatar of the user in the sidebar. Must be a valid URL"""