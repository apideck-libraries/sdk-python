"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from apideck_unify import models, utils
from apideck_unify._hooks import HookContext
from apideck_unify.types import OptionalNullable, UNSET
from apideck_unify.utils import get_security_from_env
from typing import Any, Mapping, Optional


class ConnectionCustomMappings(BaseSDK):
    def list(
        self,
        *,
        unified_api: str,
        service_id: str,
        resource: str,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VaultConnectionCustomMappingsAllResponse:
        r"""List connection custom mappings

        This endpoint returns a list of custom mappings for a connection.

        :param unified_api: Unified API
        :param service_id: Service ID of the resource to return
        :param resource: Name of the resource (plural)
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param resource_id: This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.VaultConnectionCustomMappingsAllRequest(
            consumer_id=consumer_id,
            app_id=app_id,
            unified_api=unified_api,
            service_id=service_id,
            resource=resource,
            resource_id=resource_id,
        )

        req = self._build_request(
            method="GET",
            path="/vault/connections/{unified_api}/{service_id}/{resource}/custom-mappings",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.VaultConnectionCustomMappingsAllGlobals(
                consumer_id=self.sdk_configuration.globals.consumer_id,
                app_id=self.sdk_configuration.globals.app_id,
            ),
            security=self.sdk_configuration.security,
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
            retry_config = (retries, ["408", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="vault.connectionCustomMappingsAll",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.VaultConnectionCustomMappingsAllResponse(
                get_custom_mappings_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetCustomMappingsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.BadRequestResponseData
            )
            raise models.BadRequestResponse(data=response_data)
        if utils.match_response(http_res, "401", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnauthorizedResponseData
            )
            raise models.UnauthorizedResponse(data=response_data)
        if utils.match_response(http_res, "402", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.PaymentRequiredResponseData
            )
            raise models.PaymentRequiredResponse(data=response_data)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.NotFoundResponseData
            )
            raise models.NotFoundResponse(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableResponseData
            )
            raise models.UnprocessableResponse(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return models.VaultConnectionCustomMappingsAllResponse(
                unexpected_error_response=utils.unmarshal_json(
                    http_res.text, Optional[models.UnexpectedErrorResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_async(
        self,
        *,
        unified_api: str,
        service_id: str,
        resource: str,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.VaultConnectionCustomMappingsAllResponse:
        r"""List connection custom mappings

        This endpoint returns a list of custom mappings for a connection.

        :param unified_api: Unified API
        :param service_id: Service ID of the resource to return
        :param resource: Name of the resource (plural)
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param resource_id: This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.VaultConnectionCustomMappingsAllRequest(
            consumer_id=consumer_id,
            app_id=app_id,
            unified_api=unified_api,
            service_id=service_id,
            resource=resource,
            resource_id=resource_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/vault/connections/{unified_api}/{service_id}/{resource}/custom-mappings",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.VaultConnectionCustomMappingsAllGlobals(
                consumer_id=self.sdk_configuration.globals.consumer_id,
                app_id=self.sdk_configuration.globals.app_id,
            ),
            security=self.sdk_configuration.security,
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
            retry_config = (retries, ["408", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="vault.connectionCustomMappingsAll",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.VaultConnectionCustomMappingsAllResponse(
                get_custom_mappings_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetCustomMappingsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.BadRequestResponseData
            )
            raise models.BadRequestResponse(data=response_data)
        if utils.match_response(http_res, "401", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnauthorizedResponseData
            )
            raise models.UnauthorizedResponse(data=response_data)
        if utils.match_response(http_res, "402", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.PaymentRequiredResponseData
            )
            raise models.PaymentRequiredResponse(data=response_data)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.NotFoundResponseData
            )
            raise models.NotFoundResponse(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableResponseData
            )
            raise models.UnprocessableResponse(data=response_data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return models.VaultConnectionCustomMappingsAllResponse(
                unexpected_error_response=utils.unmarshal_json(
                    http_res.text, Optional[models.UnexpectedErrorResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
