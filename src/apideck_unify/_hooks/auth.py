from typing import Union
import requests
from .types import (
    BeforeRequestHook,
    BeforeRequestContext,
)

class AuthHook(BeforeRequestHook):

    def before_request(
        self, 
        _: BeforeRequestContext, 
        request: requests.PreparedRequest
    ) -> Union[requests.PreparedRequest, Exception]:
        api_key: str | None = request.headers.get("Authorization")
        if api_key is not None:
            request.headers["Authorization"] = f"Bearer {api_key}"
        return request
