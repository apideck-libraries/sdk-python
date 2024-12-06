# Bills
(*accounting.bills*)

## Overview

### Available Operations

* [list](#list) - List Bills
* [create](#create) - Create Bill
* [get](#get) - Get Bill
* [update](#update) - Update Bill
* [delete](#delete) - Delete Bill

## list

List Bills

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
    res = s.accounting.bills.list(request={
        "service_id": "salesforce",
        "filter_": {
            "updated_since": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
        },
        "sort": {
            "by": apideck_unify.By.UPDATED_AT,
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

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.AccountingBillsAllRequest](../../models/accountingbillsallrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AccountingBillsAllResponse](../../models/accountingbillsallresponse.md)**

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

Create Bill

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
    res = s.accounting.bills.create(bill={
        "bill_number": "10001",
        "supplier": {
            "id": "12345",
            "display_name": "Windsurf Shop",
            "address": {
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
        },
        "company_id": "12345",
        "currency": apideck_unify.Currency.USD,
        "currency_rate": 0.69,
        "tax_inclusive": True,
        "bill_date": dateutil.parser.parse("2020-09-30").date(),
        "due_date": dateutil.parser.parse("2020-10-30").date(),
        "paid_date": dateutil.parser.parse("2020-10-30").date(),
        "po_number": "90000117",
        "reference": "123456",
        "line_items": [
            {
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
                "tax_amount": 27500,
                "total_amount": 27500,
                "quantity": 1,
                "unit_price": 27500.5,
                "unit_of_measure": "pc.",
                "discount_percentage": 0.01,
                "discount_amount": 19.99,
                "location_id": "1234",
                "department_id": "1234",
                "item": {
                    "id": "12344",
                    "code": "120-C",
                    "name": "Model Y",
                },
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
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
                "row_version": "1-12345",
            },
        ],
        "terms": "Net 30 days",
        "balance": 27500,
        "deposit": 0,
        "sub_total": 27500,
        "total_tax": 2500,
        "total": 27500,
        "tax_code": "1234",
        "notes": "Some notes about this bill.",
        "status": apideck_unify.BillStatus.DRAFT,
        "ledger_account": {
            "id": "123456",
            "nominal_code": "N091",
            "code": "453",
        },
        "payment_method": "cash",
        "channel": "email",
        "language": "EN",
        "accounting_by_row": False,
        "bank_account": {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck_unify.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck_unify.Currency.USD,
        },
        "discount_percentage": 5.5,
        "tracking_categories": [
            {
                "id": "123456",
                "name": "New York",
            },
        ],
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
        "accounting_period": "01-24",
    }, service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `bill`                                                                                                                                        | [models.BillInput](../../models/billinput.md)                                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingBillsAddResponse](../../models/accountingbillsaddresponse.md)**

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

Get Bill

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.bills.get(id="<id>", service_id="salesforce", fields="id,updated_at")

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

**[models.AccountingBillsOneResponse](../../models/accountingbillsoneresponse.md)**

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

Update Bill

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
    res = s.accounting.bills.update(id="<id>", bill={
        "bill_number": "10001",
        "supplier": {
            "id": "12345",
            "display_name": "Windsurf Shop",
            "address": {
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
        },
        "company_id": "12345",
        "currency": apideck_unify.Currency.USD,
        "currency_rate": 0.69,
        "tax_inclusive": True,
        "bill_date": dateutil.parser.parse("2020-09-30").date(),
        "due_date": dateutil.parser.parse("2020-10-30").date(),
        "paid_date": dateutil.parser.parse("2020-10-30").date(),
        "po_number": "90000117",
        "reference": "123456",
        "line_items": [
            {
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
                "tax_amount": 27500,
                "total_amount": 27500,
                "quantity": 1,
                "unit_price": 27500.5,
                "unit_of_measure": "pc.",
                "discount_percentage": 0.01,
                "discount_amount": 19.99,
                "location_id": "1234",
                "department_id": "1234",
                "item": {
                    "id": "12344",
                    "code": "120-C",
                    "name": "Model Y",
                },
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
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
                "row_version": "1-12345",
            },
            {
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
                "tax_amount": 27500,
                "total_amount": 27500,
                "quantity": 1,
                "unit_price": 27500.5,
                "unit_of_measure": "pc.",
                "discount_percentage": 0.01,
                "discount_amount": 19.99,
                "location_id": "1234",
                "department_id": "1234",
                "item": {
                    "id": "12344",
                    "code": "120-C",
                    "name": "Model Y",
                },
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "row_version": "1-12345",
            },
            {
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck_unify.BillLineItemType.EXPENSE_ACCOUNT,
                "tax_amount": 27500,
                "total_amount": 27500,
                "quantity": 1,
                "unit_price": 27500.5,
                "unit_of_measure": "pc.",
                "discount_percentage": 0.01,
                "discount_amount": 19.99,
                "location_id": "1234",
                "department_id": "1234",
                "item": {
                    "id": "12344",
                    "code": "120-C",
                    "name": "Model Y",
                },
                "tax_rate": {
                    "id": "123456",
                    "rate": 10,
                },
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
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
                "row_version": "1-12345",
            },
        ],
        "terms": "Net 30 days",
        "balance": 27500,
        "deposit": 0,
        "sub_total": 27500,
        "total_tax": 2500,
        "total": 27500,
        "tax_code": "1234",
        "notes": "Some notes about this bill.",
        "status": apideck_unify.BillStatus.DRAFT,
        "ledger_account": {
            "id": "123456",
            "nominal_code": "N091",
            "code": "453",
        },
        "payment_method": "cash",
        "channel": "email",
        "language": "EN",
        "accounting_by_row": False,
        "bank_account": {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck_unify.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck_unify.Currency.USD,
        },
        "discount_percentage": 5.5,
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
        "accounting_period": "01-24",
    }, service_id="salesforce")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `bill`                                                                                                                                        | [models.BillInput](../../models/billinput.md)                                                                                                 | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingBillsUpdateResponse](../../models/accountingbillsupdateresponse.md)**

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

Delete Bill

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.bills.delete(id="<id>", service_id="salesforce")

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

**[models.AccountingBillsDeleteResponse](../../models/accountingbillsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |