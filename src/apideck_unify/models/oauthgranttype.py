"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class OAuthGrantType(str, Enum):
    r"""OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types"""

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"