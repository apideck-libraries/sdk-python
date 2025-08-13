# Quotes
(*accounting.quotes*)

## Overview

### Available Operations

* [list](#list) - List Quotes
* [create](#create) - Create Quote
* [get](#get) - Get Quote
* [update](#update) - Update Quote
* [delete](#delete) - Delete Quote

## list

List Quotes

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.quotesAll" method="get" path="/accounting/quotes" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.quotes.list(raw=False, service_id="salesforce", limit=20)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `consumer_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | ID of the consumer which you want to get or push data from                                                                                    | test-consumer                                                                                                                                 |
| `app_id`                                                                                                                                      | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of your Unify application                                                                                                              | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                       |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `cursor`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                            | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.                              |                                                                                                                                               |
| `limit`                                                                                                                                       | *Optional[int]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Number of results to return. Minimum 1, Maximum 200, Default 20                                                                               |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingQuotesAllResponse](../../models/accountingquotesallresponse.md)**

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

Create Quote

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.quotesAdd" method="post" path="/accounting/quotes" -->
```python
import apideck_unify
from apideck_unify import Apideck
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.quotes.create(raw=False, service_id="salesforce", number="QT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, sales_order_id="123456", company_id="12345", department_id="12345", project_id="12345", quote_date=date.fromisoformat("2020-09-30"), expiry_date=date.fromisoformat("2020-10-30"), terms="Valid for 30 days", reference="INV-2024-001", status=apideck_unify.QuoteStatus.DRAFT, currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", discount_percentage=5.5, discount_amount=25, total=27500, customer_memo="Thank you for considering our services!", line_items=[
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.QuoteLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
            "category_id": "12345",
            "location_id": "12345",
            "department_id": "12345",
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
                    "parent_id": "123456",
                    "parent_name": "New York",
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
    ], billing_address={
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
    }, shipping_address={
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
    }, tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
            "parent_id": "123456",
            "parent_name": "New York",
        },
    ], template_id="123456", source_document_url="https://www.quotesolution.com/quote/123456", custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": "Uses Salesforce and Marketo",
        },
    ], row_version="1-12345", pass_through=[
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
    ])

    assert res.create_quote_response is not None

    # Handle response
    print(res.create_quote_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Quote number.                                                                                                                                           | QT00546                                                                                                                                                 |
| `customer`                                                                                                                                              | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The customer this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `sales_order_id`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The unique identifier for the sales order.                                                                                                              | 123456                                                                                                                                                  |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company ID the transaction belongs to                                                                                                               | 12345                                                                                                                                                   |
| `department_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the department                                                                                                                                | 12345                                                                                                                                                   |
| `project_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The unique identifier for the linked project.                                                                                                           | 12345                                                                                                                                                   |
| `quote_date`                                                                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | Date quote was issued - YYYY-MM-DD.                                                                                                                     | 2020-09-30                                                                                                                                              |
| `expiry_date`                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date until which the quote is valid - YYYY-MM-DD.                                                                                                   | 2020-10-30                                                                                                                                              |
| `terms`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Terms of the quote.                                                                                                                                     | Valid for 30 days                                                                                                                                       |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional reference identifier for the transaction.                                                                                                      | INV-2024-001                                                                                                                                            |
| `status`                                                                                                                                                | [OptionalNullable[models.QuoteStatus]](../../models/quotestatus.md)                                                                                     | :heavy_minus_sign:                                                                                                                                      | Quote status                                                                                                                                            | draft                                                                                                                                                   |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this quote.                                                                                                                 | 2500                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `discount_percentage`                                                                                                                                   | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount percentage applied to this quote.                                                                                                              | 5.5                                                                                                                                                     |
| `discount_amount`                                                                                                                                       | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount amount applied to this quote.                                                                                                                  | 25                                                                                                                                                      |
| `total`                                                                                                                                                 | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total amount of quote, including tax.                                                                                                                   | 27500                                                                                                                                                   |
| `customer_memo`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Customer memo                                                                                                                                           | Thank you for considering our services!                                                                                                                 |
| `line_items`                                                                                                                                            | List[[models.QuoteLineItemInput](../../models/quotelineiteminput.md)]                                                                                   | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `billing_address`                                                                                                                                       | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `template_id`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional quote template                                                                                                                                 | 123456                                                                                                                                                  |
| `source_document_url`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | URL link to a source document - shown as 'Go to [appName]' in the downstream app.                                                                       | https://www.quotesolution.com/quote/123456                                                                                                              |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingQuotesAddResponse](../../models/accountingquotesaddresponse.md)**

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

Get Quote

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.quotesOne" method="get" path="/accounting/quotes/{id}" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.quotes.get(id="<id>", service_id="salesforce", raw=False)

    assert res.get_quote_response is not None

    # Handle response
    print(res.get_quote_response)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `consumer_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | ID of the consumer which you want to get or push data from                                                                                    | test-consumer                                                                                                                                 |
| `app_id`                                                                                                                                      | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of your Unify application                                                                                                              | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                       |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingQuotesOneResponse](../../models/accountingquotesoneresponse.md)**

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

Update Quote

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.quotesUpdate" method="patch" path="/accounting/quotes/{id}" -->
```python
import apideck_unify
from apideck_unify import Apideck
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.quotes.update(id="<id>", service_id="salesforce", raw=False, number="QT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, sales_order_id="123456", company_id="12345", department_id="12345", project_id="12345", quote_date=date.fromisoformat("2020-09-30"), expiry_date=date.fromisoformat("2020-10-30"), terms="Valid for 30 days", reference="INV-2024-001", status=apideck_unify.QuoteStatus.DRAFT, currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", discount_percentage=5.5, discount_amount=25, total=27500, customer_memo="Thank you for considering our services!", line_items=[
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.QuoteLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
            "category_id": "12345",
            "location_id": "12345",
            "department_id": "12345",
            "item": {
                "id": "12344",
                "code": "120-C",
                "name": "Model Y",
            },
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "tracking_categories": None,
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
    ], billing_address={
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
    }, shipping_address={
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
    }, tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
            "parent_id": "123456",
            "parent_name": "New York",
        },
    ], template_id="123456", source_document_url="https://www.quotesolution.com/quote/123456", custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": "Uses Salesforce and Marketo",
        },
    ], row_version="1-12345", pass_through=[
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
    ])

    assert res.update_quote_response is not None

    # Handle response
    print(res.update_quote_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Quote number.                                                                                                                                           | QT00546                                                                                                                                                 |
| `customer`                                                                                                                                              | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The customer this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `sales_order_id`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The unique identifier for the sales order.                                                                                                              | 123456                                                                                                                                                  |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company ID the transaction belongs to                                                                                                               | 12345                                                                                                                                                   |
| `department_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the department                                                                                                                                | 12345                                                                                                                                                   |
| `project_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The unique identifier for the linked project.                                                                                                           | 12345                                                                                                                                                   |
| `quote_date`                                                                                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | Date quote was issued - YYYY-MM-DD.                                                                                                                     | 2020-09-30                                                                                                                                              |
| `expiry_date`                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date until which the quote is valid - YYYY-MM-DD.                                                                                                   | 2020-10-30                                                                                                                                              |
| `terms`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Terms of the quote.                                                                                                                                     | Valid for 30 days                                                                                                                                       |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional reference identifier for the transaction.                                                                                                      | INV-2024-001                                                                                                                                            |
| `status`                                                                                                                                                | [OptionalNullable[models.QuoteStatus]](../../models/quotestatus.md)                                                                                     | :heavy_minus_sign:                                                                                                                                      | Quote status                                                                                                                                            | draft                                                                                                                                                   |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this quote.                                                                                                                 | 2500                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `discount_percentage`                                                                                                                                   | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount percentage applied to this quote.                                                                                                              | 5.5                                                                                                                                                     |
| `discount_amount`                                                                                                                                       | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount amount applied to this quote.                                                                                                                  | 25                                                                                                                                                      |
| `total`                                                                                                                                                 | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total amount of quote, including tax.                                                                                                                   | 27500                                                                                                                                                   |
| `customer_memo`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Customer memo                                                                                                                                           | Thank you for considering our services!                                                                                                                 |
| `line_items`                                                                                                                                            | List[[models.QuoteLineItemInput](../../models/quotelineiteminput.md)]                                                                                   | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `billing_address`                                                                                                                                       | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `template_id`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional quote template                                                                                                                                 | 123456                                                                                                                                                  |
| `source_document_url`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | URL link to a source document - shown as 'Go to [appName]' in the downstream app.                                                                       | https://www.quotesolution.com/quote/123456                                                                                                              |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingQuotesUpdateResponse](../../models/accountingquotesupdateresponse.md)**

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

Delete Quote

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.quotesDelete" method="delete" path="/accounting/quotes/{id}" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.quotes.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_quote_response is not None

    # Handle response
    print(res.delete_quote_response)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `consumer_id`                                                                                                                                 | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | ID of the consumer which you want to get or push data from                                                                                    | test-consumer                                                                                                                                 |
| `app_id`                                                                                                                                      | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The ID of your Unify application                                                                                                              | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                       |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AccountingQuotesDeleteResponse](../../models/accountingquotesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |