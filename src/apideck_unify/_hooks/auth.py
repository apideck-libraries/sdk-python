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
        api_key = request.headers.get("Authorization")
        request.headers["Authorization"] = f"Bearer {api_key}"
        return request
