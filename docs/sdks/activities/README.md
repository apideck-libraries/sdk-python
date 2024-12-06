# Activities
(*crm.activities*)

## Overview

### Available Operations

* [list](#list) - List activities
* [create](#create) - Create activity
* [get](#get) - Get activity
* [update](#update) - Update activity
* [delete](#delete) - Delete activity

## list

List activities

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.activities.list(request={
        "service_id": "salesforce",
        "filter_": {
            "updated_since": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        },
        "sort": {
            "by": apideck_unify.ActivitiesSortBy.CREATED_AT,
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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CrmActivitiesAllRequest](../../models/crmactivitiesallrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CrmActivitiesAllResponse](../../models/crmactivitiesallresponse.md)**

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

Create activity

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
    res = s.crm.activities.create(activity={
        "type": apideck_unify.ActivityType.MEETING,
        "activity_datetime": "2021-05-01T12:00:00.000Z",
        "duration_seconds": 1800,
        "user_id": "12345",
        "account_id": "12345",
        "contact_id": "12345",
        "company_id": "12345",
        "opportunity_id": "12345",
        "lead_id": "12345",
        "owner_id": "12345",
        "campaign_id": "12345",
        "case_id": "12345",
        "asset_id": "12345",
        "contract_id": "12345",
        "product_id": "12345",
        "solution_id": "12345",
        "custom_object_id": "12345",
        "title": "Meeting",
        "description": "More info about the meeting",
        "note": "An internal note about the meeting",
        "location": "Space",
        "location_address": {
            "id": "123",
            "type": apideck_unify.Type.PRIMARY,
            "string": "25 Spring Street, Blackburn, VIC 3130",
            "name": "HQ US",
            "line1": "Main street",
            "line2": "apt #",
            "line3": "Suite #",
            "line4": "delivery instructions",
            "street_number": "25",
            "city": "San Francisco",
            "state": "CA",
            "postal_code": "94104",
            "country": "US",
            "latitude": "40.759211",
            "longitude": "-73.984638",
            "county": "Santa Clara",
            "contact_name": "Elon Musk",
            "salutation": "Mr",
            "phone_number": "111-111-1111",
            "fax": "122-111-1111",
            "email": "elon@musk.com",
            "website": "https://elonmusk.com",
            "notes": "Address notes or delivery instructions.",
            "row_version": "1-12345",
        },
        "all_day_event": False,
        "private": True,
        "group_event": True,
        "event_sub_type": "debrief",
        "group_event_type": "Proposed",
        "child": False,
        "archived": False,
        "deleted": False,
        "show_as": apideck_unify.ShowAs.BUSY,
        "done": False,
        "start_datetime": "2021-05-01T12:00:00.000Z",
        "end_datetime": "2021-05-01T12:30:00.000Z",
        "activity_date": "2021-05-01",
        "end_date": "2021-05-01",
        "recurrent": False,
        "reminder_datetime": "2021-05-01T17:00:00.000Z",
        "reminder_set": False,
        "video_conference_url": "https://us02web.zoom.us/j/88120759396",
        "video_conference_id": "zoom:88120759396",
        "custom_fields": [
            {
                "id": "2389328923893298",
                "name": "employee_level",
                "description": "Employee Level",
            },
        ],
        "attendees": [
            {
                "name": "Elon Musk",
                "first_name": "Elon",
                "middle_name": "D.",
                "last_name": "Musk",
                "prefix": "Mr.",
                "suffix": "PhD",
                "email_address": "elon@musk.com",
                "is_organizer": True,
                "status": apideck_unify.ActivityAttendeeStatus.ACCEPTED,
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

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `activity`                                                                                                                                    | [models.ActivityInput](../../models/activityinput.md)                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.CrmActivitiesAddResponse](../../models/crmactivitiesaddresponse.md)**

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

Get activity

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.activities.get(id="<id>", service_id="salesforce", fields="id,updated_at")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the record you are acting upon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `service_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | salesforce                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `raw`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Include raw response. Mostly used for debugging purposes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.CrmActivitiesOneResponse](../../models/crmactivitiesoneresponse.md)**

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

Update activity

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
    res = s.crm.activities.update(id="<id>", activity={
        "type": apideck_unify.ActivityType.MEETING,
        "activity_datetime": "2021-05-01T12:00:00.000Z",
        "duration_seconds": 1800,
        "user_id": "12345",
        "account_id": "12345",
        "contact_id": "12345",
        "company_id": "12345",
        "opportunity_id": "12345",
        "lead_id": "12345",
        "owner_id": "12345",
        "campaign_id": "12345",
        "case_id": "12345",
        "asset_id": "12345",
        "contract_id": "12345",
        "product_id": "12345",
        "solution_id": "12345",
        "custom_object_id": "12345",
        "title": "Meeting",
        "description": "More info about the meeting",
        "note": "An internal note about the meeting",
        "location": "Space",
        "location_address": {
            "id": "123",
            "type": apideck_unify.Type.PRIMARY,
            "string": "25 Spring Street, Blackburn, VIC 3130",
            "name": "HQ US",
            "line1": "Main street",
            "line2": "apt #",
            "line3": "Suite #",
            "line4": "delivery instructions",
            "street_number": "25",
            "city": "San Francisco",
            "state": "CA",
            "postal_code": "94104",
            "country": "US",
            "latitude": "40.759211",
            "longitude": "-73.984638",
            "county": "Santa Clara",
            "contact_name": "Elon Musk",
            "salutation": "Mr",
            "phone_number": "111-111-1111",
            "fax": "122-111-1111",
            "email": "elon@musk.com",
            "website": "https://elonmusk.com",
            "notes": "Address notes or delivery instructions.",
            "row_version": "1-12345",
        },
        "all_day_event": False,
        "private": True,
        "group_event": True,
        "event_sub_type": "debrief",
        "group_event_type": "Proposed",
        "child": False,
        "archived": False,
        "deleted": False,
        "show_as": apideck_unify.ShowAs.BUSY,
        "done": False,
        "start_datetime": "2021-05-01T12:00:00.000Z",
        "end_datetime": "2021-05-01T12:30:00.000Z",
        "activity_date": "2021-05-01",
        "end_date": "2021-05-01",
        "recurrent": False,
        "reminder_datetime": "2021-05-01T17:00:00.000Z",
        "reminder_set": False,
        "video_conference_url": "https://us02web.zoom.us/j/88120759396",
        "video_conference_id": "zoom:88120759396",
        "custom_fields": [
            {
                "id": "2389328923893298",
                "name": "employee_level",
                "description": "Employee Level",
            },
            {
                "id": "2389328923893298",
                "name": "employee_level",
                "description": "Employee Level",
                "value": True,
            },
            {
                "id": "2389328923893298",
                "name": "employee_level",
                "description": "Employee Level",
            },
        ],
        "attendees": [
            {
                "name": "Elon Musk",
                "first_name": "Elon",
                "middle_name": "D.",
                "last_name": "Musk",
                "prefix": "Mr.",
                "suffix": "PhD",
                "email_address": "elon@musk.com",
                "is_organizer": True,
                "status": apideck_unify.ActivityAttendeeStatus.ACCEPTED,
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

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `activity`                                                                                                                                    | [models.ActivityInput](../../models/activityinput.md)                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.CrmActivitiesUpdateResponse](../../models/crmactivitiesupdateresponse.md)**

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

Delete activity

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.activities.delete(id="<id>", service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.CrmActivitiesDeleteResponse](../../models/crmactivitiesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |