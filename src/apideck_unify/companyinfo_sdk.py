"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from apideck_unify import models, utils
from apideck_unify._hooks import HookContext
from apideck_unify.types import OptionalNullable, UNSET
from apideck_unify.utils import get_security_from_env
from apideck_unify.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Mapping, Optional


class CompanyInfoSDK(BaseSDK):
    def get(
        self,
        *,
        raw: Optional[bool] = False,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AccountingCompanyInfoOneResponse:
        r"""Get company info

        Get company info

        :param raw: Include raw response. Mostly used for debugging purposes
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param fields: The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
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

        request = models.AccountingCompanyInfoOneRequest(
            raw=raw,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            fields=fields,
        )

        req = self._build_request(
            method="GET",
            path="/accounting/company-info",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AccountingCompanyInfoOneGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="accounting.companyInfoOne",
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
            return models.AccountingCompanyInfoOneResponse(
                get_company_info_response=unmarshal_json_response(
                    Optional[models.GetCompanyInfoResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = unmarshal_json_response(
                models.BadRequestResponseData, http_res
            )
            raise models.BadRequestResponse(response_data, http_res)
        if utils.match_response(http_res, "401", "application/json"):
            response_data = unmarshal_json_response(
                models.UnauthorizedResponseData, http_res
            )
            raise models.UnauthorizedResponse(response_data, http_res)
        if utils.match_response(http_res, "402", "application/json"):
            response_data = unmarshal_json_response(
                models.PaymentRequiredResponseData, http_res
            )
            raise models.PaymentRequiredResponse(response_data, http_res)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = unmarshal_json_response(
                models.NotFoundResponseData, http_res
            )
            raise models.NotFoundResponse(response_data, http_res)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = unmarshal_json_response(
                models.UnprocessableResponseData, http_res
            )
            raise models.UnprocessableResponse(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "default", "application/json"):
            return models.AccountingCompanyInfoOneResponse(
                unexpected_error_response=unmarshal_json_response(
                    Optional[models.UnexpectedErrorResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )

        raise models.APIError("Unexpected response received", http_res)

    async def get_async(
        self,
        *,
        raw: Optional[bool] = False,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AccountingCompanyInfoOneResponse:
        r"""Get company info

        Get company info

        :param raw: Include raw response. Mostly used for debugging purposes
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param fields: The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
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

        request = models.AccountingCompanyInfoOneRequest(
            raw=raw,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            fields=fields,
        )

        req = self._build_request_async(
            method="GET",
            path="/accounting/company-info",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AccountingCompanyInfoOneGlobals(
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="accounting.companyInfoOne",
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
            return models.AccountingCompanyInfoOneResponse(
                get_company_info_response=unmarshal_json_response(
                    Optional[models.GetCompanyInfoResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )
        if utils.match_response(http_res, "400", "application/json"):
            response_data = unmarshal_json_response(
                models.BadRequestResponseData, http_res
            )
            raise models.BadRequestResponse(response_data, http_res)
        if utils.match_response(http_res, "401", "application/json"):
            response_data = unmarshal_json_response(
                models.UnauthorizedResponseData, http_res
            )
            raise models.UnauthorizedResponse(response_data, http_res)
        if utils.match_response(http_res, "402", "application/json"):
            response_data = unmarshal_json_response(
                models.PaymentRequiredResponseData, http_res
            )
            raise models.PaymentRequiredResponse(response_data, http_res)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = unmarshal_json_response(
                models.NotFoundResponseData, http_res
            )
            raise models.NotFoundResponse(response_data, http_res)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = unmarshal_json_response(
                models.UnprocessableResponseData, http_res
            )
            raise models.UnprocessableResponse(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "default", "application/json"):
            return models.AccountingCompanyInfoOneResponse(
                unexpected_error_response=unmarshal_json_response(
                    Optional[models.UnexpectedErrorResponse], http_res
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
            )

        raise models.APIError("Unexpected response received", http_res)
