# JournalEntries
(*accounting.journal_entries*)

## Overview

### Available Operations

* [list](#list) - List Journal Entries
* [create](#create) - Create Journal Entry
* [get](#get) - Get Journal Entry
* [update](#update) - Update Journal Entry
* [delete](#delete) - Delete Journal Entry

## list

List Journal Entries

### Example Usage

```python
import apideck_sdk
from apideck_sdk import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.journal_entries.list(request={
        "service_id": "salesforce",
        "filter_": {
            "updated_since": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        },
        "sort": {
            "by": apideck_sdk.JournalEntriesSortBy.UPDATED_AT,
            "direction": apideck_sdk.SortDirection.DESC,
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

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.AccountingJournalEntriesAllRequest](../../models/accountingjournalentriesallrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AccountingJournalEntriesAllResponse](../../models/accountingjournalentriesallresponse.md)**

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

Create Journal Entry

### Example Usage

```python
import apideck_sdk
from apideck_sdk import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.journal_entries.create(journal_entry={
        "title": "Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry",
        "currency_rate": 0.69,
        "currency": apideck_sdk.Currency.USD,
        "company_id": "12345",
        "line_items": [
            {
                "type": apideck_sdk.JournalEntryLineItemType.DEBIT,
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "tax_amount": 27500,
                "sub_total": 27500,
                "total_amount": 27500,
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "customer": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "email": "boring@boring.com",
                },
                "supplier": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "address": {
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
                },
                "line_number": 1,
            },
        ],
        "memo": "Thank you for your business and have a great day!",
        "posted_at": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        "journal_symbol": "IND",
        "tax_type": "sales",
        "tax_code": "1234",
        "number": "OIT00546",
        "tracking_categories": [
            {
                "id": "123456",
                "name": "New York",
            },
        ],
        "accounting_period": "01-24",
        "row_version": "1-12345",
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
| `journal_entry`                                                                                                                               | [models.JournalEntryInput](../../models/journalentryinput.md)                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingJournalEntriesAddResponse](../../models/accountingjournalentriesaddresponse.md)**

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

Get Journal Entry

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.journal_entries.get(id="<id>", service_id="salesforce", fields="id,updated_at")

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

**[models.AccountingJournalEntriesOneResponse](../../models/accountingjournalentriesoneresponse.md)**

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

Update Journal Entry

### Example Usage

```python
import apideck_sdk
from apideck_sdk import Apideck
import dateutil.parser
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.journal_entries.update(id="<id>", journal_entry={
        "title": "Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry",
        "currency_rate": 0.69,
        "currency": apideck_sdk.Currency.USD,
        "company_id": "12345",
        "line_items": [
            {
                "type": apideck_sdk.JournalEntryLineItemType.DEBIT,
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "tax_amount": 27500,
                "sub_total": 27500,
                "total_amount": 27500,
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "customer": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "email": "boring@boring.com",
                },
                "supplier": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "address": {
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
                },
                "line_number": 1,
            },
            {
                "type": apideck_sdk.JournalEntryLineItemType.DEBIT,
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "tax_amount": 27500,
                "sub_total": 27500,
                "total_amount": 27500,
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "customer": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "email": "boring@boring.com",
                },
                "supplier": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "address": {
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
                },
                "line_number": 1,
            },
            {
                "type": apideck_sdk.JournalEntryLineItemType.DEBIT,
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "tax_amount": 27500,
                "sub_total": 27500,
                "total_amount": 27500,
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "customer": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "email": "boring@boring.com",
                },
                "supplier": {
                    "id": "12345",
                    "display_name": "Windsurf Shop",
                    "address": {
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
                },
                "line_number": 1,
            },
        ],
        "memo": "Thank you for your business and have a great day!",
        "posted_at": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        "journal_symbol": "IND",
        "tax_type": "sales",
        "tax_code": "1234",
        "number": "OIT00546",
        "tracking_categories": [
            {
                "id": "123456",
                "name": "New York",
            },
            {
                "id": "123456",
                "name": "New York",
            },
        ],
        "accounting_period": "01-24",
        "row_version": "1-12345",
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
    }, service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `journal_entry`                                                                                                                               | [models.JournalEntryInput](../../models/journalentryinput.md)                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingJournalEntriesUpdateResponse](../../models/accountingjournalentriesupdateresponse.md)**

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

Delete Journal Entry

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.journal_entries.delete(id="<id>", service_id="salesforce")

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

**[models.AccountingJournalEntriesDeleteResponse](../../models/accountingjournalentriesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |