"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .consumermetadata import ConsumerMetadata, ConsumerMetadataTypedDict
from .unifiedapiid import UnifiedAPIID
from apideck_unify.types import BaseModel
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class AllowActions(str, Enum):
    DELETE = "delete"
    DISCONNECT = "disconnect"
    REAUTHORIZE = "reauthorize"
    DISABLE = "disable"


class SettingsTypedDict(TypedDict):
    r"""Settings to change the way the Vault is displayed."""

    unified_apis: NotRequired[List[UnifiedAPIID]]
    r"""Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs."""
    hide_resource_settings: NotRequired[bool]
    r"""A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user."""
    sandbox_mode: NotRequired[bool]
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment."""
    isolation_mode: NotRequired[bool]
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items."""
    session_length: NotRequired[str]
    r"""The duration of time the session is valid for (maximum 1 week)."""
    show_logs: NotRequired[bool]
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`."""
    show_suggestions: NotRequired[bool]
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`."""
    show_sidebar: NotRequired[bool]
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`."""
    auto_redirect: NotRequired[bool]
    r"""Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`."""
    hide_guides: NotRequired[bool]
    r"""Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`."""
    allow_actions: NotRequired[List[AllowActions]]
    r"""Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault.
    Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`.
    Empty array will hide all actions. By default all actions are visible.
    """


class Settings(BaseModel):
    r"""Settings to change the way the Vault is displayed."""

    unified_apis: Optional[List[UnifiedAPIID]] = None
    r"""Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs."""

    hide_resource_settings: Optional[bool] = False
    r"""A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user."""

    sandbox_mode: Optional[bool] = False
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment."""

    isolation_mode: Optional[bool] = False
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items."""

    session_length: Optional[str] = "1h"
    r"""The duration of time the session is valid for (maximum 1 week)."""

    show_logs: Optional[bool] = True
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`."""

    show_suggestions: Optional[bool] = False
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`."""

    show_sidebar: Optional[bool] = True
    r"""Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`."""

    auto_redirect: Optional[bool] = False
    r"""Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`."""

    hide_guides: Optional[bool] = False
    r"""Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`."""

    allow_actions: Optional[List[AllowActions]] = None
    r"""Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault.
    Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`.
    Empty array will hide all actions. By default all actions are visible.
    """


class ThemeTypedDict(TypedDict):
    r"""Theming options to change the look and feel of Vault."""

    favicon: NotRequired[str]
    r"""The URL to the favicon to use for Vault."""
    logo: NotRequired[str]
    r"""The URL to the logo to use for Vault."""
    primary_color: NotRequired[str]
    r"""The primary color to use for Vault."""
    sidepanel_background_color: NotRequired[str]
    r"""The background color to use for the sidebar."""
    sidepanel_text_color: NotRequired[str]
    r"""The text color to use for the sidebar."""
    vault_name: NotRequired[str]
    r"""The name that will be shown in the sidebar."""
    privacy_url: NotRequired[str]
    r"""The URL to the privacy policy that will be shown in the sidebar."""
    terms_url: NotRequired[str]
    r"""The URL to the terms and conditions that will be shown in the sidebar."""


class Theme(BaseModel):
    r"""Theming options to change the look and feel of Vault."""

    favicon: Optional[str] = None
    r"""The URL to the favicon to use for Vault."""

    logo: Optional[str] = None
    r"""The URL to the logo to use for Vault."""

    primary_color: Optional[str] = None
    r"""The primary color to use for Vault."""

    sidepanel_background_color: Optional[str] = None
    r"""The background color to use for the sidebar."""

    sidepanel_text_color: Optional[str] = None
    r"""The text color to use for the sidebar."""

    vault_name: Optional[str] = None
    r"""The name that will be shown in the sidebar."""

    privacy_url: Optional[str] = None
    r"""The URL to the privacy policy that will be shown in the sidebar."""

    terms_url: Optional[str] = None
    r"""The URL to the terms and conditions that will be shown in the sidebar."""


class SessionTypedDict(TypedDict):
    consumer_metadata: NotRequired[ConsumerMetadataTypedDict]
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""
    redirect_uri: NotRequired[str]
    r"""The URL to redirect the user to after the session has been configured."""
    settings: NotRequired[SettingsTypedDict]
    r"""Settings to change the way the Vault is displayed."""
    theme: NotRequired[ThemeTypedDict]
    r"""Theming options to change the look and feel of Vault."""
    custom_consumer_settings: NotRequired[Dict[str, Any]]
    r"""Custom consumer settings that are passed as part of the session."""


class Session(BaseModel):
    consumer_metadata: Optional[ConsumerMetadata] = None
    r"""The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended."""

    redirect_uri: Optional[str] = None
    r"""The URL to redirect the user to after the session has been configured."""

    settings: Optional[Settings] = None
    r"""Settings to change the way the Vault is displayed."""

    theme: Optional[Theme] = None
    r"""Theming options to change the look and feel of Vault."""

    custom_consumer_settings: Optional[Dict[str, Any]] = None
    r"""Custom consumer settings that are passed as part of the session."""
