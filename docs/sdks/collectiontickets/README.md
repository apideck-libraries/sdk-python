# CollectionTickets
(*issue_tracking.collection_tickets*)

## Overview

### Available Operations

* [list](#list) - List Tickets
* [create](#create) - Create Ticket
* [get](#get) - Get Ticket
* [update](#update) - Update Ticket
* [delete](#delete) - Delete Ticket

## list

List Tickets

### Example Usage

```python
import apideck
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_tickets.list(request={
        "collection_id": "apideck-io",
        "service_id": "salesforce",
        "sort": {
            "by": apideck.TicketsSortBy.CREATED_AT,
            "direction": apideck.SortDirection.DESC,
        },
        "filter_": {
            "status": [
                "open",
            ],
        },
        "pass_through": {
            "search": "San Francisco",
        },
        "fields": "id,updated_at",
    })

    if res.get_tickets_response is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.IssueTrackingCollectionTicketsAllRequest](../../models/issuetrackingcollectionticketsallrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.IssueTrackingCollectionTicketsAllResponse](../../models/issuetrackingcollectionticketsallresponse.md)**

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

Create Ticket

### Example Usage

```python
import apideck
from apideck import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_tickets.create(collection_id="apideck-io", ticket={
        "parent_id": "12345",
        "type": "Technical",
        "subject": "Technical Support Request",
        "description": "I am facing issues with my internet connection",
        "status": "open",
        "priority": apideck.Priority.HIGH,
        "assignees": [
            {
                "id": "12345",
            },
        ],
        "due_date": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        "tags": [
            {
                "id": "12345",
            },
            {
                "id": "12345",
            },
        ],
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
                ],
            },
        ],
    }, service_id="salesforce")

    if res.create_ticket_response is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_id`                                                                                                                               | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The collection ID                                                                                                                             | apideck-io                                                                                                                                    |
| `ticket`                                                                                                                                      | [models.TicketInput](../../models/ticketinput.md)                                                                                             | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.IssueTrackingCollectionTicketsAddResponse](../../models/issuetrackingcollectionticketsaddresponse.md)**

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

Get Ticket

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_tickets.get(request={
        "ticket_id": "<id>",
        "collection_id": "apideck-io",
        "service_id": "salesforce",
        "fields": "id,updated_at",
    })

    if res.get_ticket_response is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.IssueTrackingCollectionTicketsOneRequest](../../models/issuetrackingcollectionticketsonerequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.IssueTrackingCollectionTicketsOneResponse](../../models/issuetrackingcollectionticketsoneresponse.md)**

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

Update Ticket

### Example Usage

```python
import apideck
from apideck import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_tickets.update(request={
        "ticket_id": "<id>",
        "collection_id": "apideck-io",
        "ticket": {
            "parent_id": "12345",
            "type": "Technical",
            "subject": "Technical Support Request",
            "description": "I am facing issues with my internet connection",
            "status": "open",
            "priority": apideck.Priority.HIGH,
            "assignees": [
                {
                    "id": "12345",
                },
                {
                    "id": "12345",
                },
                {
                    "id": "12345",
                },
            ],
            "due_date": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
            "tags": [
                {
                    "id": "12345",
                },
                {
                    "id": "12345",
                },
            ],
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

    if res.update_ticket_response is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.IssueTrackingCollectionTicketsUpdateRequest](../../models/issuetrackingcollectionticketsupdaterequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.IssueTrackingCollectionTicketsUpdateResponse](../../models/issuetrackingcollectionticketsupdateresponse.md)**

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

Delete Ticket

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.issue_tracking.collection_tickets.delete(ticket_id="<id>", collection_id="apideck-io", service_id="salesforce")

    if res.delete_ticket_response is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `ticket_id`                                                                                                                                   | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the ticket you are acting upon.                                                                                                         |                                                                                                                                               |
| `collection_id`                                                                                                                               | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The collection ID                                                                                                                             | apideck-io                                                                                                                                    |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.IssueTrackingCollectionTicketsDeleteResponse](../../models/issuetrackingcollectionticketsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |