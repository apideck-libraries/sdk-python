"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .authtype import AuthType
from .connectionstate import ConnectionState
from .custommapping import CustomMapping, CustomMappingTypedDict
from .custommapping_input import CustomMappingInput, CustomMappingInputTypedDict
from .formfield import FormField, FormFieldTypedDict
from .formfieldoption import FormFieldOption, FormFieldOptionTypedDict
from .integrationstate import IntegrationState
from .oauthgranttype import OAuthGrantType
from .webhooksubscription import WebhookSubscription, WebhookSubscriptionTypedDict
from apideck_unify.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class ConnectionStatus(str, Enum):
    r"""Status of the connection."""

    LIVE = "live"
    UPCOMING = "upcoming"
    REQUESTED = "requested"


class Target(str, Enum):
    CUSTOM_FIELDS = "custom_fields"
    RESOURCE = "resource"


ConnectionValue5TypedDict = TypeAliasType(
    "ConnectionValue5TypedDict", Union[str, int, float]
)


ConnectionValue5 = TypeAliasType("ConnectionValue5", Union[str, int, float])


ConnectionValueTypedDict = TypeAliasType(
    "ConnectionValueTypedDict",
    Union[str, int, float, bool, List[ConnectionValue5TypedDict]],
)


ConnectionValue = TypeAliasType(
    "ConnectionValue", Union[str, int, float, bool, List[ConnectionValue5]]
)


class DefaultsTypedDict(TypedDict):
    target: NotRequired[Target]
    id: NotRequired[str]
    options: NotRequired[List[FormFieldOptionTypedDict]]
    value: NotRequired[ConnectionValueTypedDict]


class Defaults(BaseModel):
    target: Optional[Target] = None

    id: Optional[str] = None

    options: Optional[List[FormFieldOption]] = None

    value: Optional[ConnectionValue] = None


class ConfigurationTypedDict(TypedDict):
    resource: NotRequired[str]
    defaults: NotRequired[List[DefaultsTypedDict]]


class Configuration(BaseModel):
    resource: Optional[str] = None

    defaults: Optional[List[Defaults]] = None


class ConnectionTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The unique identifier of the connection."""
    service_id: NotRequired[str]
    r"""The ID of the service this connection belongs to."""
    name: NotRequired[str]
    r"""The name of the connection"""
    tag_line: NotRequired[str]
    unified_api: NotRequired[str]
    r"""The unified API category where the connection belongs to."""
    state: NotRequired[ConnectionState]
    r"""[Connection state flow](#section/Connection-state)"""
    integration_state: NotRequired[IntegrationState]
    r"""The current state of the Integration."""
    auth_type: NotRequired[AuthType]
    r"""Type of authorization used by the connector"""
    oauth_grant_type: NotRequired[OAuthGrantType]
    r"""OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types"""
    status: NotRequired[ConnectionStatus]
    r"""Status of the connection."""
    enabled: NotRequired[bool]
    r"""Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API."""
    website: NotRequired[str]
    r"""The website URL of the connection"""
    icon: NotRequired[str]
    r"""A visual icon of the connection, that will be shown in the Vault"""
    logo: NotRequired[str]
    r"""The logo of the connection, that will be shown in the Vault"""
    authorize_url: NotRequired[Nullable[str]]
    r"""The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter to the `authorize_url`. Be sure to URL encode the `redirect_uri` part. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI."""
    revoke_url: NotRequired[Nullable[str]]
    r"""The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI."""
    settings: NotRequired[Nullable[Dict[str, Any]]]
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Attach your own consumer specific metadata"""
    form_fields: NotRequired[List[FormFieldTypedDict]]
    r"""The settings that are wanted to create a connection."""
    configuration: NotRequired[List[ConfigurationTypedDict]]
    configurable_resources: NotRequired[List[str]]
    resource_schema_support: NotRequired[List[str]]
    resource_settings_support: NotRequired[List[str]]
    validation_support: NotRequired[bool]
    schema_support: NotRequired[bool]
    settings_required_for_authorization: NotRequired[List[str]]
    r"""List of settings that are required to be configured on integration before authorization can occur"""
    subscriptions: NotRequired[List[WebhookSubscriptionTypedDict]]
    has_guide: NotRequired[bool]
    r"""Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection)."""
    created_at: NotRequired[float]
    custom_mappings: NotRequired[List[CustomMappingTypedDict]]
    r"""List of custom mappings configured for this connection"""
    updated_at: NotRequired[Nullable[float]]


class Connection(BaseModel):
    id: Optional[str] = None
    r"""The unique identifier of the connection."""

    service_id: Optional[str] = None
    r"""The ID of the service this connection belongs to."""

    name: Optional[str] = None
    r"""The name of the connection"""

    tag_line: Optional[str] = None

    unified_api: Optional[str] = None
    r"""The unified API category where the connection belongs to."""

    state: Optional[ConnectionState] = None
    r"""[Connection state flow](#section/Connection-state)"""

    integration_state: Optional[IntegrationState] = None
    r"""The current state of the Integration."""

    auth_type: Optional[AuthType] = None
    r"""Type of authorization used by the connector"""

    oauth_grant_type: Optional[OAuthGrantType] = None
    r"""OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types"""

    status: Optional[ConnectionStatus] = None
    r"""Status of the connection."""

    enabled: Optional[bool] = None
    r"""Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API."""

    website: Optional[str] = None
    r"""The website URL of the connection"""

    icon: Optional[str] = None
    r"""A visual icon of the connection, that will be shown in the Vault"""

    logo: Optional[str] = None
    r"""The logo of the connection, that will be shown in the Vault"""

    authorize_url: OptionalNullable[str] = UNSET
    r"""The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter to the `authorize_url`. Be sure to URL encode the `redirect_uri` part. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI."""

    revoke_url: OptionalNullable[str] = UNSET
    r"""The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI."""

    settings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""

    metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Attach your own consumer specific metadata"""

    form_fields: Optional[List[FormField]] = None
    r"""The settings that are wanted to create a connection."""

    configuration: Optional[List[Configuration]] = None

    configurable_resources: Optional[List[str]] = None

    resource_schema_support: Optional[List[str]] = None

    resource_settings_support: Optional[List[str]] = None

    validation_support: Optional[bool] = None

    schema_support: Optional[bool] = None

    settings_required_for_authorization: Optional[List[str]] = None
    r"""List of settings that are required to be configured on integration before authorization can occur"""

    subscriptions: Optional[List[WebhookSubscription]] = None

    has_guide: Optional[bool] = None
    r"""Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection)."""

    created_at: Optional[float] = None

    custom_mappings: Optional[List[CustomMapping]] = None
    r"""List of custom mappings configured for this connection"""

    updated_at: OptionalNullable[float] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "service_id",
            "name",
            "tag_line",
            "unified_api",
            "state",
            "integration_state",
            "auth_type",
            "oauth_grant_type",
            "status",
            "enabled",
            "website",
            "icon",
            "logo",
            "authorize_url",
            "revoke_url",
            "settings",
            "metadata",
            "form_fields",
            "configuration",
            "configurable_resources",
            "resource_schema_support",
            "resource_settings_support",
            "validation_support",
            "schema_support",
            "settings_required_for_authorization",
            "subscriptions",
            "has_guide",
            "created_at",
            "custom_mappings",
            "updated_at",
        ]
        nullable_fields = [
            "authorize_url",
            "revoke_url",
            "settings",
            "metadata",
            "updated_at",
        ]
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


class ConnectionDefaultsTypedDict(TypedDict):
    id: NotRequired[str]
    options: NotRequired[List[FormFieldOptionTypedDict]]
    value: NotRequired[ConnectionValueTypedDict]


class ConnectionDefaults(BaseModel):
    id: Optional[str] = None

    options: Optional[List[FormFieldOption]] = None

    value: Optional[ConnectionValue] = None


class ConnectionConfigurationTypedDict(TypedDict):
    resource: NotRequired[str]
    defaults: NotRequired[List[ConnectionDefaultsTypedDict]]


class ConnectionConfiguration(BaseModel):
    resource: Optional[str] = None

    defaults: Optional[List[ConnectionDefaults]] = None


class ConnectionInputTypedDict(TypedDict):
    enabled: NotRequired[bool]
    r"""Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API."""
    settings: NotRequired[Nullable[Dict[str, Any]]]
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""
    metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Attach your own consumer specific metadata"""
    configuration: NotRequired[List[ConnectionConfigurationTypedDict]]
    custom_mappings: NotRequired[List[CustomMappingInputTypedDict]]
    r"""List of custom mappings configured for this connection"""


class ConnectionInput(BaseModel):
    enabled: Optional[bool] = None
    r"""Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API."""

    settings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Connection settings. Values will persist to `form_fields` with corresponding id"""

    metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Attach your own consumer specific metadata"""

    configuration: Optional[List[ConnectionConfiguration]] = None

    custom_mappings: Optional[List[CustomMappingInput]] = None
    r"""List of custom mappings configured for this connection"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "enabled",
            "settings",
            "metadata",
            "configuration",
            "custom_mappings",
        ]
        nullable_fields = ["settings", "metadata"]
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
