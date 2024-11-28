"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from apideck import models, utils
from apideck._hooks import HookContext
from apideck.types import BaseModel, OptionalNullable, UNSET
from apideck.utils import get_security_from_env
from typing import Any, Optional, Union, cast


class CollectionTags(BaseSDK):
    def list(
        self,
        *,
        request: Union[
            models.IssueTrackingCollectionTagsAllRequest,
            models.IssueTrackingCollectionTagsAllRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.IssueTrackingCollectionTagsAllResponse:
        r"""List Tags

        List Tags

        :param request: The request object to send.
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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.IssueTrackingCollectionTagsAllRequest
            )
        request = cast(models.IssueTrackingCollectionTagsAllRequest, request)

        req = self.build_request(
            method="GET",
            path="/issue-tracking/collections/{collection_id}/tags",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=models.IssueTrackingCollectionTagsAllGlobals(
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
                operation_id="issueTracking.collectionTagsAll",
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
            return models.IssueTrackingCollectionTagsAllResponse(
                get_collection_tags_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetCollectionTagsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
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
            return models.IssueTrackingCollectionTagsAllResponse(
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
        request: Union[
            models.IssueTrackingCollectionTagsAllRequest,
            models.IssueTrackingCollectionTagsAllRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.IssueTrackingCollectionTagsAllResponse:
        r"""List Tags

        List Tags

        :param request: The request object to send.
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

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, models.IssueTrackingCollectionTagsAllRequest
            )
        request = cast(models.IssueTrackingCollectionTagsAllRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/issue-tracking/collections/{collection_id}/tags",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=models.IssueTrackingCollectionTagsAllGlobals(
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
                operation_id="issueTracking.collectionTagsAll",
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
            return models.IssueTrackingCollectionTagsAllResponse(
                get_collection_tags_response=utils.unmarshal_json(
                    http_res.text, Optional[models.GetCollectionTagsResponse]
                ),
                http_meta=models.HTTPMetadata(request=req, response=http_res),
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
            return models.IssueTrackingCollectionTagsAllResponse(
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
