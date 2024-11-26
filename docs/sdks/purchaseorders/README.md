# PurchaseOrders
(*accounting.purchase_orders*)

## Overview

### Available Operations

* [list](#list) - List Purchase Orders
* [create](#create) - Create Purchase Order
* [get](#get) - Get Purchase Order
* [update](#update) - Update Purchase Order
* [delete](#delete) - Delete Purchase Order

## list

List Purchase Orders

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
    res = s.accounting.purchase_orders.list(request={
        "service_id": "salesforce",
        "pass_through": {
            "search": "San Francisco",
        },
        "filter_": {
            "updated_since": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
            "supplier_id": "1234",
        },
        "sort": {
            "by": apideck.PurchaseOrdersSortBy.UPDATED_AT,
            "direction": apideck.SortDirection.DESC,
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.AccountingPurchaseOrdersAllRequest](../../models/accountingpurchaseordersallrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AccountingPurchaseOrdersAllResponse](../../models/accountingpurchaseordersallresponse.md)**

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

Create Purchase Order

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
    res = s.accounting.purchase_orders.create(purchase_order={
        "po_number": "90000117",
        "reference": "123456",
        "supplier": {
            "id": "12345",
            "display_name": "Windsurf Shop",
            "address": {
                "id": "123",
                "type": apideck.Type.PRIMARY,
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
        "status": apideck.PurchaseOrderStatus.OPEN,
        "issued_date": dateutil.parser.parse("2020-09-30").date(),
        "delivery_date": dateutil.parser.parse("2020-09-30").date(),
        "expected_arrival_date": dateutil.parser.parse("2020-09-30").date(),
        "currency": apideck.Currency.USD,
        "currency_rate": 0.69,
        "sub_total": 27500,
        "total_tax": 2500,
        "total": 27500,
        "tax_inclusive": True,
        "line_items": [
            {
                "id": "12345",
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck.InvoiceLineItemType.SALES_ITEM,
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
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "custom_fields": [
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                        "value": "Uses Salesforce and Marketo",
                    },
                ],
                "row_version": "1-12345",
            },
        ],
        "shipping_address": {
            "id": "123",
            "type": apideck.Type.PRIMARY,
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
        "ledger_account": {
            "id": "123456",
            "nominal_code": "N091",
            "code": "453",
        },
        "template_id": "123456",
        "discount_percentage": 5.5,
        "bank_account": {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck.Currency.USD,
        },
        "accounting_by_row": False,
        "due_date": dateutil.parser.parse("2020-10-30").date(),
        "payment_method": "cash",
        "tax_code": "1234",
        "channel": "email",
        "memo": "Thank you for the partnership and have a great day!",
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
| `purchase_order`                                                                                                                              | [models.PurchaseOrderInput](../../models/purchaseorderinput.md)                                                                               | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingPurchaseOrdersAddResponse](../../models/accountingpurchaseordersaddresponse.md)**

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

Get Purchase Order

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.purchase_orders.get(id="<id>", service_id="salesforce")

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

**[models.AccountingPurchaseOrdersOneResponse](../../models/accountingpurchaseordersoneresponse.md)**

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

Update Purchase Order

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
    res = s.accounting.purchase_orders.update(id="<id>", purchase_order={
        "po_number": "90000117",
        "reference": "123456",
        "supplier": {
            "id": "12345",
            "display_name": "Windsurf Shop",
            "address": {
                "id": "123",
                "type": apideck.Type.PRIMARY,
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
        "status": apideck.PurchaseOrderStatus.OPEN,
        "issued_date": dateutil.parser.parse("2020-09-30").date(),
        "delivery_date": dateutil.parser.parse("2020-09-30").date(),
        "expected_arrival_date": dateutil.parser.parse("2020-09-30").date(),
        "currency": apideck.Currency.USD,
        "currency_rate": 0.69,
        "sub_total": 27500,
        "total_tax": 2500,
        "total": 27500,
        "tax_inclusive": True,
        "line_items": [
            {
                "id": "12345",
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck.InvoiceLineItemType.SALES_ITEM,
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
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "custom_fields": [
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                    },
                ],
                "row_version": "1-12345",
            },
            {
                "id": "12345",
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck.InvoiceLineItemType.SALES_ITEM,
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
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "custom_fields": [
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                        "value": "Uses Salesforce and Marketo",
                    },
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                    },
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                        "value": 10,
                    },
                ],
                "row_version": "1-12345",
            },
            {
                "id": "12345",
                "row_id": "12345",
                "code": "120-C",
                "line_number": 1,
                "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
                "type": apideck.InvoiceLineItemType.SALES_ITEM,
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
                "tracking_categories": [
                    {
                        "id": "123456",
                        "name": "New York",
                    },
                ],
                "ledger_account": {
                    "id": "123456",
                    "nominal_code": "N091",
                    "code": "453",
                },
                "custom_fields": [
                    {
                        "id": "2389328923893298",
                        "name": "employee_level",
                        "description": "Employee Level",
                        "value": [
                            {},
                        ],
                    },
                ],
                "row_version": "1-12345",
            },
        ],
        "shipping_address": {
            "id": "123",
            "type": apideck.Type.PRIMARY,
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
        "ledger_account": {
            "id": "123456",
            "nominal_code": "N091",
            "code": "453",
        },
        "template_id": "123456",
        "discount_percentage": 5.5,
        "bank_account": {
            "bank_name": "Monzo",
            "account_number": "123465",
            "account_name": "SPACEX LLC",
            "account_type": apideck.AccountType.CREDIT_CARD,
            "iban": "CH2989144532982975332",
            "bic": "AUDSCHGGXXX",
            "routing_number": "012345678",
            "bsb_number": "062-001",
            "branch_identifier": "001",
            "bank_code": "BNH",
            "currency": apideck.Currency.USD,
        },
        "accounting_by_row": False,
        "due_date": dateutil.parser.parse("2020-10-30").date(),
        "payment_method": "cash",
        "tax_code": "1234",
        "channel": "email",
        "memo": "Thank you for the partnership and have a great day!",
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
| `purchase_order`                                                                                                                              | [models.PurchaseOrderInput](../../models/purchaseorderinput.md)                                                                               | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingPurchaseOrdersUpdateResponse](../../models/accountingpurchaseordersupdateresponse.md)**

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

Delete Purchase Order

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.purchase_orders.delete(id="<id>", service_id="salesforce")

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

**[models.AccountingPurchaseOrdersDeleteResponse](../../models/accountingpurchaseordersdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |