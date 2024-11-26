"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ConnectorSettingType(str, Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"
    TEL = "tel"
    EMAIL = "email"
    URL = "url"
    TEXTAREA = "textarea"
    SELECT = "select"
    FILTERED_SELECT = "filtered-select"
    MULTI_SELECT = "multi-select"
    DATETIME = "datetime"
    DATE = "date"
    TIME = "time"
    NUMBER = "number"
    PASSWORD = "password"


class ConnectorSettingTypedDict(TypedDict):
    id: NotRequired[str]
    label: NotRequired[str]
    type: NotRequired[ConnectorSettingType]


class ConnectorSetting(BaseModel):
    id: Optional[str] = None

    label: Optional[str] = None

    type: Optional[ConnectorSettingType] = None