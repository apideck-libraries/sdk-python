"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from apideck_unify import models, utils
from apideck_unify._hooks import HookContext
from apideck_unify.types import OptionalNullable, UNSET
from apideck_unify.utils import get_security_from_env
from typing import Any, Optional, Union


class CreateCallback(BaseSDK):
    def state(
        self,
        *,
        service_id: str,
        unified_api: str,
        create_callback_state: Union[
            models.CreateCallbackState, models.CreateCallbackStateTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.VaultCreateCallbackStateResponse:
        r"""Create Callback State

        This endpoint creates a callback state that can be used to issue requests to the callback endpoint.


        :param service_id: Service ID of the resource to return
        :param unified_api: Unified API
        :param create_callback_state: Callback state data
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.VaultCreateCallbackStateRequest(
            service_id=service_id,
            unified_api=unified_api,
            create_callback_state=utils.get_pydantic_model(
                create_callback_state, models.CreateCallbackState
            ),
        )

        req = self.build_request(
            method="POST",
            path="/vault/connections/{unified_api}/{service_id}/callback-state",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=models.VaultCreateCallbackStateGlobals(
                consumer_id=self.sdk_configuration.globals.consumer_id,
                app_id=self.sdk_configuration.globals.app_id,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.create_callback_state,
                False,
                False,
                "json",
                models.CreateCallbackState,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="vault.createCallbackState",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.CreateCallbackStateResponse
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.BadRequestResponseData)
            raise models.BadRequestResponse(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedResponseData)
            raise models.UnauthorizedResponse(data=data)
        if utils.match_response(http_res, "402", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.PaymentRequiredResponseData
            )
            raise models.PaymentRequiredResponse(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotFoundResponseData)
            raise models.NotFoundResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnprocessableResponseData)
            raise models.UnprocessableResponse(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, models.UnexpectedErrorResponse)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def state_async(
        self,
        *,
        service_id: str,
        unified_api: str,
        create_callback_state: Union[
            models.CreateCallbackState, models.CreateCallbackStateTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.VaultCreateCallbackStateResponse:
        r"""Create Callback State

        This endpoint creates a callback state that can be used to issue requests to the callback endpoint.


        :param service_id: Service ID of the resource to return
        :param unified_api: Unified API
        :param create_callback_state: Callback state data
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.VaultCreateCallbackStateRequest(
            service_id=service_id,
            unified_api=unified_api,
            create_callback_state=utils.get_pydantic_model(
                create_callback_state, models.CreateCallbackState
            ),
        )

        req = self.build_request_async(
            method="POST",
            path="/vault/connections/{unified_api}/{service_id}/callback-state",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=models.VaultCreateCallbackStateGlobals(
                consumer_id=self.sdk_configuration.globals.consumer_id,
                app_id=self.sdk_configuration.globals.app_id,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.create_callback_state,
                False,
                False,
                "json",
                models.CreateCallbackState,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="vault.createCallbackState",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.CreateCallbackStateResponse
            )
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.BadRequestResponseData)
            raise models.BadRequestResponse(data=data)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedResponseData)
            raise models.UnauthorizedResponse(data=data)
        if utils.match_response(http_res, "402", "application/json"):
            data = utils.unmarshal_json(
                http_res.text, models.PaymentRequiredResponseData
            )
            raise models.PaymentRequiredResponse(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotFoundResponseData)
            raise models.NotFoundResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnprocessableResponseData)
            raise models.UnprocessableResponse(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, models.UnexpectedErrorResponse)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
