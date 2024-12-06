# CollectionTicketComments
(*issue_tracking.collection_ticket_comments*)

## Overview

### Available Operations

* [list](#list) - List Comments
* [create](#create) - Create Comment
* [get](#get) - Get Comment
* [update](#update) - Update Comment
* [delete](#delete) - Delete Comment

## list

List Comments

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_ticket_comments.list(request={
        "collection_id": "apideck-io",
        "ticket_id": "<id>",
        "service_id": "salesforce",
        "sort": {
            "by": apideck_unify.CommentsSortBy.CREATED_AT,
            "direction": apideck_unify.SortDirection.DESC,
        },
        "pass_through": {
            "search": "San Francisco",
        },
        "fields": "id,updated_at",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                 | [models.IssueTrackingCollectionTicketCommentsAllRequest](../../models/issuetrackingcollectionticketcommentsallrequest.md) | :heavy_check_mark:                                                                                                        | The request object to use for the request.                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.IssueTrackingCollectionTicketCommentsAllResponse](../../models/issuetrackingcollectionticketcommentsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## create

Create Comment

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_ticket_comments.create(request={
        "collection_id": "apideck-io",
        "ticket_id": "<id>",
        "collection_ticket_comment": {
            "body": "What internet provider do you use?",
            "pass_through": [
                {
                    "service_id": "<id>",
                    "extend_paths": [
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                    ],
                },
            ],
        },
        "service_id": "salesforce",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                 | [models.IssueTrackingCollectionTicketCommentsAddRequest](../../models/issuetrackingcollectionticketcommentsaddrequest.md) | :heavy_check_mark:                                                                                                        | The request object to use for the request.                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.IssueTrackingCollectionTicketCommentsAddResponse](../../models/issuetrackingcollectionticketcommentsaddresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## get

Get Comment

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_ticket_comments.get(request={
        "id": "<id>",
        "collection_id": "apideck-io",
        "ticket_id": "<id>",
        "service_id": "salesforce",
        "fields": "id,updated_at",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                 | [models.IssueTrackingCollectionTicketCommentsOneRequest](../../models/issuetrackingcollectionticketcommentsonerequest.md) | :heavy_check_mark:                                                                                                        | The request object to use for the request.                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.IssueTrackingCollectionTicketCommentsOneResponse](../../models/issuetrackingcollectionticketcommentsoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## update

Update Comment

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_ticket_comments.update(request={
        "id": "<id>",
        "collection_id": "apideck-io",
        "ticket_id": "<id>",
        "collection_ticket_comment": {
            "body": "What internet provider do you use?",
            "pass_through": [
                {
                    "service_id": "<id>",
                    "extend_paths": [
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                    ],
                },
                {
                    "service_id": "<id>",
                    "extend_paths": [
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                    ],
                },
                {
                    "service_id": "<id>",
                    "extend_paths": [
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                        {
                            "path": "$.nested.property",
                            "value": {
                                "TaxClassificationRef": {
                                    "value": "EUC-99990201-V1-00020000",
                                },
                            },
                        },
                    ],
                },
            ],
        },
        "service_id": "salesforce",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                       | [models.IssueTrackingCollectionTicketCommentsUpdateRequest](../../models/issuetrackingcollectionticketcommentsupdaterequest.md) | :heavy_check_mark:                                                                                                              | The request object to use for the request.                                                                                      |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.IssueTrackingCollectionTicketCommentsUpdateResponse](../../models/issuetrackingcollectionticketcommentsupdateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## delete

Delete Comment

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_ticket_comments.delete(request={
        "id": "<id>",
        "collection_id": "apideck-io",
        "ticket_id": "<id>",
        "service_id": "salesforce",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                       | [models.IssueTrackingCollectionTicketCommentsDeleteRequest](../../models/issuetrackingcollectionticketcommentsdeleterequest.md) | :heavy_check_mark:                                                                                                              | The request object to use for the request.                                                                                      |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.IssueTrackingCollectionTicketCommentsDeleteResponse](../../models/issuetrackingcollectionticketcommentsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |