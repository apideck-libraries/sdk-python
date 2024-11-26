# Users
(*crm.users*)

## Overview

### Available Operations

* [list](#list) - List users
* [create](#create) - Create user
* [get](#get) - Get user
* [update](#update) - Update user
* [delete](#delete) - Delete user

## list

List users

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.users.list(request={
        "service_id": "salesforce",
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CrmUsersAllRequest](../../models/crmusersallrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CrmUsersAllResponse](../../models/crmusersallresponse.md)**

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

Create user

### Example Usage

```python
import apideck_sdk
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.users.create(user={
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_sdk.EmailType.PRIMARY,
            },
        ],
        "parent_id": "54321",
        "username": "masterofcoin",
        "first_name": "Elon",
        "last_name": "Musk",
        "title": "CEO",
        "division": "Europe",
        "company_name": "SpaceX",
        "employee_number": "123456-AB",
        "description": "A description",
        "image": "https://logo.clearbit.com/spacex.com?s=128",
        "language": "EN",
        "status": "active",
        "password": "supersecretpassword",
        "addresses": [
            {
                "id": "123",
                "type": apideck_sdk.Type.PRIMARY,
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
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_sdk.PhoneNumberType.PRIMARY,
            },
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_sdk.PhoneNumberType.PRIMARY,
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
| `user`                                                                                                                                        | [models.UserInput](../../models/userinput.md)                                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.CrmUsersAddResponse](../../models/crmusersaddresponse.md)**

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

Get user

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.users.get(id="<id>", service_id="salesforce", fields="id,updated_at")

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

**[models.CrmUsersOneResponse](../../models/crmusersoneresponse.md)**

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

Update user

### Example Usage

```python
import apideck_sdk
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.users.update(id="<id>", user={
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_sdk.EmailType.PRIMARY,
            },
        ],
        "parent_id": "54321",
        "username": "masterofcoin",
        "first_name": "Elon",
        "last_name": "Musk",
        "title": "CEO",
        "division": "Europe",
        "company_name": "SpaceX",
        "employee_number": "123456-AB",
        "description": "A description",
        "image": "https://logo.clearbit.com/spacex.com?s=128",
        "language": "EN",
        "status": "active",
        "password": "supersecretpassword",
        "addresses": [
            {
                "id": "123",
                "type": apideck_sdk.Type.PRIMARY,
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
            {
                "id": "123",
                "type": apideck_sdk.Type.PRIMARY,
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
            {
                "id": "123",
                "type": apideck_sdk.Type.PRIMARY,
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
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_sdk.PhoneNumberType.PRIMARY,
            },
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_sdk.PhoneNumberType.PRIMARY,
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
    }, service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `user`                                                                                                                                        | [models.UserInput](../../models/userinput.md)                                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.CrmUsersUpdateResponse](../../models/crmusersupdateresponse.md)**

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

Delete user

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.crm.users.delete(id="<id>", service_id="salesforce")

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

**[models.CrmUsersDeleteResponse](../../models/crmusersdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |