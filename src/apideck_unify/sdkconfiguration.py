"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from ._hooks import SDKHooks
from ._version import (
    __gen_version__,
    __openapi_doc_version__,
    __user_agent__,
    __version__,
)
from .httpclient import AsyncHttpClient, HttpClient
from .utils import Logger, RetryConfig, remove_suffix
from apideck_unify import models
from apideck_unify.models import internal
from apideck_unify.types import OptionalNullable, UNSET
from dataclasses import dataclass
from pydantic import Field
from typing import Callable, Dict, Optional, Tuple, Union


SERVERS = [
    "https://unify.apideck.com",
]
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: Union[HttpClient, None]
    client_supplied: bool
    async_client: Union[AsyncHttpClient, None]
    async_client_supplied: bool
    debug_logger: Logger
    globals: internal.Globals
    security: Optional[Union[models.Security, Callable[[], models.Security]]] = None
    server_url: Optional[str] = ""
    server_idx: Optional[int] = 0
    language: str = "python"
    openapi_doc_version: str = __openapi_doc_version__
    sdk_version: str = __version__
    gen_version: str = __gen_version__
    user_agent: str = __user_agent__
    retry_config: OptionalNullable[RetryConfig] = Field(default_factory=lambda: UNSET)
    timeout_ms: Optional[int] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}

    def get_hooks(self) -> SDKHooks:
        return self._hooks
