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
        # modify the request object before it is sent, such as adding headers
        api_key = request.headers.get("Authorization")
        request.headers["Authorization"] = f"Bearer {api_key}"
        return request