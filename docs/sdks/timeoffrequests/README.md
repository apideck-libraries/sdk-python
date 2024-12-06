# TimeOffRequests
(*hris.time_off_requests*)

## Overview

### Available Operations

* [list](#list) - List Time Off Requests
* [create](#create) - Create Time Off Request
* [get](#get) - Get Time Off Request
* [update](#update) - Update Time Off Request
* [delete](#delete) - Delete Time Off Request

## list

List Time Off Requests

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
    res = s.hris.time_off_requests.list(request={
        "service_id": "salesforce",
        "filter_": {
            "start_date": "2022-04-08",
            "end_date": "2022-04-21",
            "updated_since": "2020-09-30T07:43:32.000Z",
            "employee_id": "1234",
            "time_off_request_status": apideck_unify.TimeOffRequestStatus.APPROVED,
            "company_id": "1234",
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

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.HrisTimeOffRequestsAllRequest](../../models/hristimeoffrequestsallrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.HrisTimeOffRequestsAllResponse](../../models/hristimeoffrequestsallresponse.md)**

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

Create Time Off Request

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
    res = s.hris.time_off_requests.create(time_off_request={
        "employee_id": "12345",
        "policy_id": "12345",
        "status": apideck_unify.TimeOffRequestStatusStatus.APPROVED,
        "description": "Enjoying some sun.",
        "start_date": "2022-04-01",
        "end_date": "2022-04-01",
        "request_date": "2022-03-21",
        "request_type": apideck_unify.RequestType.VACATION,
        "approval_date": "2022-03-21",
        "units": apideck_unify.Units.HOURS,
        "amount": 3.5,
        "day_part": "morning",
        "notes": {
            "employee": "Relaxing on the beach for a few hours.",
            "manager": "Enjoy!",
        },
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
        "policy_type": "sick",
    }, service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_off_request`                                                                                                                            | [models.TimeOffRequestInput](../../models/timeoffrequestinput.md)                                                                             | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.HrisTimeOffRequestsAddResponse](../../models/hristimeoffrequestsaddresponse.md)**

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

Get Time Off Request

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.hris.time_off_requests.get(request={
        "id": "<id>",
        "employee_id": "<id>",
        "service_id": "salesforce",
        "fields": "id,updated_at",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.HrisTimeOffRequestsOneRequest](../../models/hristimeoffrequestsonerequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.HrisTimeOffRequestsOneResponse](../../models/hristimeoffrequestsoneresponse.md)**

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

Update Time Off Request

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
    res = s.hris.time_off_requests.update(request={
        "id": "<id>",
        "employee_id": "<id>",
        "time_off_request": {
            "employee_id": "12345",
            "policy_id": "12345",
            "status": apideck_unify.TimeOffRequestStatusStatus.APPROVED,
            "description": "Enjoying some sun.",
            "start_date": "2022-04-01",
            "end_date": "2022-04-01",
            "request_date": "2022-03-21",
            "request_type": apideck_unify.RequestType.VACATION,
            "approval_date": "2022-03-21",
            "units": apideck_unify.Units.HOURS,
            "amount": 3.5,
            "day_part": "morning",
            "notes": {
                "employee": "Relaxing on the beach for a few hours.",
                "manager": "Enjoy!",
            },
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
            "policy_type": "sick",
        },
        "service_id": "salesforce",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.HrisTimeOffRequestsUpdateRequest](../../models/hristimeoffrequestsupdaterequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.HrisTimeOffRequestsUpdateResponse](../../models/hristimeoffrequestsupdateresponse.md)**

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

Delete Time Off Request

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.hris.time_off_requests.delete(id="<id>", employee_id="<id>", service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `employee_id`                                                                                                                                 | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the employee you are acting upon.                                                                                                       |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.HrisTimeOffRequestsDeleteResponse](../../models/hristimeoffrequestsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |