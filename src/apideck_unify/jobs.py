"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from apideck_unify import models, utils
from apideck_unify._hooks import HookContext
from apideck_unify.types import OptionalNullable, UNSET
from apideck_unify.utils import get_security_from_env
from jsonpath import JSONPath
from typing import Any, Dict, Mapping, Optional


class Jobs(BaseSDK):
    def list(
        self,
        *,
        raw: Optional[bool] = False,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        cursor: OptionalNullable[str] = UNSET,
        limit: Optional[int] = 20,
        pass_through: Optional[Dict[str, Any]] = None,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.AtsJobsAllResponse]:
        r"""List Jobs

        List Jobs

        :param raw: Include raw response. Mostly used for debugging purposes
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
        :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
        :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
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

        request = models.AtsJobsAllRequest(
            raw=raw,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
        )

        req = self._build_request(
            method="GET",
            path="/ats/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AtsJobsAllGlobals(
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
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="ats.jobsAll",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.AtsJobsAllResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("$.meta.cursors.next").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                raw=raw,
                consumer_id=consumer_id,
                app_id=app_id,
                service_id=service_id,
                cursor=next_cursor,
                limit=limit,
                pass_through=pass_through,
                fields=fields,
                retries=retries,
            )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.AtsJobsAllResponse(
                get_jobs_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetJobsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
                next=next_func,
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
            return models.AtsJobsAllResponse(
                unexpected_error_response=utils.unmarshal_json(
                    http_res.text, Optional[models.UnexpectedErrorResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
                next=next_func,
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
        raw: Optional[bool] = False,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        cursor: OptionalNullable[str] = UNSET,
        limit: Optional[int] = 20,
        pass_through: Optional[Dict[str, Any]] = None,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.AtsJobsAllResponse]:
        r"""List Jobs

        List Jobs

        :param raw: Include raw response. Mostly used for debugging purposes
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
        :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
        :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
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

        request = models.AtsJobsAllRequest(
            raw=raw,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
        )

        req = self._build_request_async(
            method="GET",
            path="/ats/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AtsJobsAllGlobals(
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
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="ats.jobsAll",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "402", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.AtsJobsAllResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("$.meta.cursors.next").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                raw=raw,
                consumer_id=consumer_id,
                app_id=app_id,
                service_id=service_id,
                cursor=next_cursor,
                limit=limit,
                pass_through=pass_through,
                fields=fields,
                retries=retries,
            )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.AtsJobsAllResponse(
                get_jobs_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetJobsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
                next=next_func,
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
            return models.AtsJobsAllResponse(
                unexpected_error_response=utils.unmarshal_json(
                    http_res.text, Optional[models.UnexpectedErrorResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
                next=next_func,
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get(
        self,
        *,
        id: str,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        raw: Optional[bool] = False,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AtsJobsOneResponse:
        r"""Get Job

        Get Job

        :param id: ID of the record you are acting upon.
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param raw: Include raw response. Mostly used for debugging purposes
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

        request = models.AtsJobsOneRequest(
            id=id,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            raw=raw,
            fields=fields,
        )

        req = self._build_request(
            method="GET",
            path="/ats/jobs/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AtsJobsOneGlobals(
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
            retry_config = (retries, ["5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="ats.jobsOne",
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
            return models.AtsJobsOneResponse(
                get_job_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetJobResponse]
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
            return models.AtsJobsOneResponse(
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

    async def get_async(
        self,
        *,
        id: str,
        consumer_id: Optional[str] = None,
        app_id: Optional[str] = None,
        service_id: Optional[str] = None,
        raw: Optional[bool] = False,
        fields: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AtsJobsOneResponse:
        r"""Get Job

        Get Job

        :param id: ID of the record you are acting upon.
        :param consumer_id: ID of the consumer which you want to get or push data from
        :param app_id: The ID of your Unify application
        :param service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
        :param raw: Include raw response. Mostly used for debugging purposes
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

        request = models.AtsJobsOneRequest(
            id=id,
            consumer_id=consumer_id,
            app_id=app_id,
            service_id=service_id,
            raw=raw,
            fields=fields,
        )

        req = self._build_request_async(
            method="GET",
            path="/ats/jobs/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            _globals=models.AtsJobsOneGlobals(
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
            retry_config = (retries, ["5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="ats.jobsOne",
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
            return models.AtsJobsOneResponse(
                get_job_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetJobResponse]
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
            return models.AtsJobsOneResponse(
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
