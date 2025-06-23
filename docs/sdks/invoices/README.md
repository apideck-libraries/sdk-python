# Invoices
(*accounting.invoices*)

## Overview

### Available Operations

* [list](#list) - List Invoices
* [create](#create) - Create Invoice
* [get](#get) - Get Invoice
* [update](#update) - Update Invoice
* [delete](#delete) - Delete Invoice

## list

List Invoices

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
from apideck_unify.utils import parse_datetime
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.invoices.list(raw=False, service_id="salesforce", limit=20, filter_={
        "updated_since": parse_datetime("2020-09-30T07:43:32.000Z"),
        "created_since": parse_datetime("2020-09-30T07:43:32.000Z"),
        "number": "OIT00546",
    }, sort={
        "by": apideck_unify.InvoicesSortBy.UPDATED_AT,
        "direction": apideck_unify.SortDirection.DESC,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Include raw response. Mostly used for debugging purposes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `consumer_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the consumer which you want to get or push data from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | test-consumer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `app_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The ID of your Unify application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `service_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | salesforce                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `cursor`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Number of results to return. Minimum 1, Maximum 200, Default 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.InvoicesFilter]](../../models/invoicesfilter.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply filters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"updated_since": "2020-09-30T07:43:32.000Z",<br/>"created_since": "2020-09-30T07:43:32.000Z",<br/>"number": "OIT00546"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.InvoicesSort]](../../models/invoicessort.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply sorting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"by": "updated_at",<br/>"direction": "desc"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pass_through`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {<br/>"search": "San Francisco"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.AccountingInvoicesAllResponse](../../models/accountinginvoicesallresponse.md)**

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

Create Invoice

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
from apideck_unify.utils import parse_datetime
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.invoices.create(raw=False, service_id="salesforce", type_=apideck_unify.InvoiceType.SERVICE, number="OIT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, company_id="12345", invoice_date=date.fromisoformat("2020-09-30"), due_date=date.fromisoformat("2020-09-30"), terms="Net 30 days", po_number="90000117", reference="123456", status=apideck_unify.InvoiceStatus.DRAFT, invoice_sent=True, currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", discount_percentage=5.5, discount_amount=25, total=27500, balance=27500, deposit=0, customer_memo="Thank you for your business and have a great day!", tracking_categories=[
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
    ], line_items=[
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.InvoiceLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
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
                    "value": {},
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
            "type": apideck_unify.InvoiceLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
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
                    "value": {},
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
    }, template_id="123456", source_document_url="https://www.invoicesolution.com/invoice/123456", payment_allocations=[
        {
            "id": "123456",
            "allocated_amount": 1000,
            "date_": parse_datetime("2020-09-30T07:43:32.000Z"),
        },
    ], payment_method="cash", channel="email", language="EN", accounting_by_row=False, bank_account={
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
    }, ledger_account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": {},
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
            ],
        },
    ])

    assert res.create_invoice_response is not None

    # Handle response
    print(res.create_invoice_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                            | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Include raw response. Mostly used for debugging purposes                                                                                                         |                                                                                                                                                                  |
| `consumer_id`                                                                                                                                                    | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | ID of the consumer which you want to get or push data from                                                                                                       | test-consumer                                                                                                                                                    |
| `app_id`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The ID of your Unify application                                                                                                                                 | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                          |
| `service_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                    | salesforce                                                                                                                                                       |
| `type`                                                                                                                                                           | [OptionalNullable[models.InvoiceType]](../../models/invoicetype.md)                                                                                              | :heavy_minus_sign:                                                                                                                                               | Invoice type                                                                                                                                                     | service                                                                                                                                                          |
| `number`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Invoice number.                                                                                                                                                  | OIT00546                                                                                                                                                         |
| `customer`                                                                                                                                                       | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                              | :heavy_minus_sign:                                                                                                                                               | The customer this entity is linked to.                                                                                                                           |                                                                                                                                                                  |
| `company_id`                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The company or subsidiary id the transaction belongs to                                                                                                          | 12345                                                                                                                                                            |
| `invoice_date`                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | Date invoice was issued - YYYY-MM-DD.                                                                                                                            | 2020-09-30                                                                                                                                                       |
| `due_date`                                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.                                           | 2020-09-30                                                                                                                                                       |
| `terms`                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Terms of payment.                                                                                                                                                | Net 30 days                                                                                                                                                      |
| `po_number`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | 90000117                                                                                                                                                         |
| `reference`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Optional reference identifier for the transaction.                                                                                                               | INV-2024-001                                                                                                                                                     |
| `status`                                                                                                                                                         | [OptionalNullable[models.InvoiceStatus]](../../models/invoicestatus.md)                                                                                          | :heavy_minus_sign:                                                                                                                                               | Invoice status                                                                                                                                                   | draft                                                                                                                                                            |
| `invoice_sent`                                                                                                                                                   | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Invoice sent to contact/customer.                                                                                                                                | true                                                                                                                                                             |
| `currency`                                                                                                                                                       | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                               | USD                                                                                                                                                              |
| `currency_rate`                                                                                                                                                  | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Currency Exchange Rate at the time entity was recorded/generated.                                                                                                | 0.69                                                                                                                                                             |
| `tax_inclusive`                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Amounts are including tax                                                                                                                                        | true                                                                                                                                                             |
| `sub_total`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Sub-total amount, normally before tax.                                                                                                                           | 27500                                                                                                                                                            |
| `total_tax`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total tax amount applied to this invoice.                                                                                                                        | 2500                                                                                                                                                             |
| `tax_code`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                                     | 1234                                                                                                                                                             |
| `discount_percentage`                                                                                                                                            | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Discount percentage applied to this invoice.                                                                                                                     | 5.5                                                                                                                                                              |
| `discount_amount`                                                                                                                                                | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Discount amount applied to this invoice.                                                                                                                         | 25                                                                                                                                                               |
| `total`                                                                                                                                                          | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total amount of invoice, including tax.                                                                                                                          | 27500                                                                                                                                                            |
| `balance`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Balance of invoice due.                                                                                                                                          | 27500                                                                                                                                                            |
| `deposit`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Amount of deposit made to this invoice.                                                                                                                          | 0                                                                                                                                                                |
| `customer_memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Customer memo                                                                                                                                                    | Thank you for your business and have a great day!                                                                                                                |
| `tracking_category`                                                                                                                                              | [OptionalNullable[models.DeprecatedLinkedTrackingCategory]](../../models/deprecatedlinkedtrackingcategory.md)                                                    | :heavy_minus_sign:                                                                                                                                               | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.                                          |                                                                                                                                                                  |
| `tracking_categories`                                                                                                                                            | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                          | :heavy_minus_sign:                                                                                                                                               | A list of linked tracking categories.                                                                                                                            |                                                                                                                                                                  |
| `line_items`                                                                                                                                                     | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                                        | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `billing_address`                                                                                                                                                | [Optional[models.Address]](../../models/address.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `shipping_address`                                                                                                                                               | [Optional[models.Address]](../../models/address.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `template_id`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Optional invoice template                                                                                                                                        | 123456                                                                                                                                                           |
| `source_document_url`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.                                             | https://www.invoicesolution.com/invoice/123456                                                                                                                   |
| `payment_allocations`                                                                                                                                            | List[[models.PaymentAllocations](../../models/paymentallocations.md)]                                                                                            | :heavy_minus_sign:                                                                                                                                               | IDs of payments made on the invoice                                                                                                                              |                                                                                                                                                                  |
| `payment_method`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                                      | cash                                                                                                                                                             |
| `channel`                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The channel through which the transaction is processed.                                                                                                          | email                                                                                                                                                            |
| `language`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | language code according to ISO 639-1. For the United States - EN                                                                                                 | EN                                                                                                                                                               |
| `accounting_by_row`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.                | false                                                                                                                                                            |
| `bank_account`                                                                                                                                                   | [Optional[models.BankAccount]](../../models/bankaccount.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `ledger_account`                                                                                                                                                 | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                                    | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `custom_fields`                                                                                                                                                  | List[[models.CustomField](../../models/customfield.md)]                                                                                                          | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `row_version`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.                       | 1-12345                                                                                                                                                          |
| `pass_through`                                                                                                                                                   | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources.          |                                                                                                                                                                  |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.AccountingInvoicesAddResponse](../../models/accountinginvoicesaddresponse.md)**

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

Get Invoice

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.invoices.get(id="<id>", service_id="salesforce", raw=False, fields="id,updated_at")

    assert res.get_invoice_response is not None

    # Handle response
    print(res.get_invoice_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the record you are acting upon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `consumer_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ID of the consumer which you want to get or push data from                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | test-consumer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `app_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The ID of your Unify application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `service_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | salesforce                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `raw`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Include raw response. Mostly used for debugging purposes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.AccountingInvoicesOneResponse](../../models/accountinginvoicesoneresponse.md)**

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

Update Invoice

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
from apideck_unify.utils import parse_datetime
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.invoices.update(id="<id>", service_id="salesforce", raw=False, type_=apideck_unify.InvoiceType.SERVICE, number="OIT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, company_id="12345", invoice_date=date.fromisoformat("2020-09-30"), due_date=date.fromisoformat("2020-09-30"), terms="Net 30 days", po_number="90000117", reference="123456", status=apideck_unify.InvoiceStatus.DRAFT, invoice_sent=True, currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", discount_percentage=5.5, discount_amount=25, total=27500, balance=27500, deposit=0, customer_memo="Thank you for your business and have a great day!", tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
        },
        {
            "id": "123456",
            "name": "New York",
        },
    ], line_items=[
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.InvoiceLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
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
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.InvoiceLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
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
        {
            "id": "12345",
            "row_id": "12345",
            "code": "120-C",
            "line_number": 1,
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "type": apideck_unify.InvoiceLineItemType.SALES_ITEM,
            "tax_amount": 27500,
            "total_amount": 27500,
            "quantity": 1,
            "unit_price": 27500.5,
            "unit_of_measure": "pc.",
            "discount_percentage": 0.01,
            "discount_amount": 19.99,
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
    }, template_id="123456", source_document_url="https://www.invoicesolution.com/invoice/123456", payment_allocations=[
        {
            "id": "123456",
            "allocated_amount": 1000,
            "date_": parse_datetime("2020-09-30T07:43:32.000Z"),
        },
        {
            "id": "123456",
            "allocated_amount": 1000,
            "date_": parse_datetime("2020-09-30T07:43:32.000Z"),
        },
        {
            "id": "123456",
            "allocated_amount": 1000,
            "date_": parse_datetime("2020-09-30T07:43:32.000Z"),
        },
    ], payment_method="cash", channel="email", language="EN", accounting_by_row=False, bank_account={
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
    }, ledger_account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, custom_fields=[
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
    ])

    assert res.update_invoice_response is not None

    # Handle response
    print(res.update_invoice_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | ID of the record you are acting upon.                                                                                                                            |                                                                                                                                                                  |
| `consumer_id`                                                                                                                                                    | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | ID of the consumer which you want to get or push data from                                                                                                       | test-consumer                                                                                                                                                    |
| `app_id`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The ID of your Unify application                                                                                                                                 | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                          |
| `service_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                    | salesforce                                                                                                                                                       |
| `raw`                                                                                                                                                            | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Include raw response. Mostly used for debugging purposes                                                                                                         |                                                                                                                                                                  |
| `type`                                                                                                                                                           | [OptionalNullable[models.InvoiceType]](../../models/invoicetype.md)                                                                                              | :heavy_minus_sign:                                                                                                                                               | Invoice type                                                                                                                                                     | service                                                                                                                                                          |
| `number`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Invoice number.                                                                                                                                                  | OIT00546                                                                                                                                                         |
| `customer`                                                                                                                                                       | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                              | :heavy_minus_sign:                                                                                                                                               | The customer this entity is linked to.                                                                                                                           |                                                                                                                                                                  |
| `company_id`                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The company or subsidiary id the transaction belongs to                                                                                                          | 12345                                                                                                                                                            |
| `invoice_date`                                                                                                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | Date invoice was issued - YYYY-MM-DD.                                                                                                                            | 2020-09-30                                                                                                                                                       |
| `due_date`                                                                                                                                                       | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                     | :heavy_minus_sign:                                                                                                                                               | The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.                                           | 2020-09-30                                                                                                                                                       |
| `terms`                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Terms of payment.                                                                                                                                                | Net 30 days                                                                                                                                                      |
| `po_number`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order. | 90000117                                                                                                                                                         |
| `reference`                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Optional reference identifier for the transaction.                                                                                                               | INV-2024-001                                                                                                                                                     |
| `status`                                                                                                                                                         | [OptionalNullable[models.InvoiceStatus]](../../models/invoicestatus.md)                                                                                          | :heavy_minus_sign:                                                                                                                                               | Invoice status                                                                                                                                                   | draft                                                                                                                                                            |
| `invoice_sent`                                                                                                                                                   | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Invoice sent to contact/customer.                                                                                                                                | true                                                                                                                                                             |
| `currency`                                                                                                                                                       | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                               | USD                                                                                                                                                              |
| `currency_rate`                                                                                                                                                  | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Currency Exchange Rate at the time entity was recorded/generated.                                                                                                | 0.69                                                                                                                                                             |
| `tax_inclusive`                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Amounts are including tax                                                                                                                                        | true                                                                                                                                                             |
| `sub_total`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Sub-total amount, normally before tax.                                                                                                                           | 27500                                                                                                                                                            |
| `total_tax`                                                                                                                                                      | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total tax amount applied to this invoice.                                                                                                                        | 2500                                                                                                                                                             |
| `tax_code`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                                     | 1234                                                                                                                                                             |
| `discount_percentage`                                                                                                                                            | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Discount percentage applied to this invoice.                                                                                                                     | 5.5                                                                                                                                                              |
| `discount_amount`                                                                                                                                                | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Discount amount applied to this invoice.                                                                                                                         | 25                                                                                                                                                               |
| `total`                                                                                                                                                          | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Total amount of invoice, including tax.                                                                                                                          | 27500                                                                                                                                                            |
| `balance`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Balance of invoice due.                                                                                                                                          | 27500                                                                                                                                                            |
| `deposit`                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                               | Amount of deposit made to this invoice.                                                                                                                          | 0                                                                                                                                                                |
| `customer_memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Customer memo                                                                                                                                                    | Thank you for your business and have a great day!                                                                                                                |
| `tracking_category`                                                                                                                                              | [OptionalNullable[models.DeprecatedLinkedTrackingCategory]](../../models/deprecatedlinkedtrackingcategory.md)                                                    | :heavy_minus_sign:                                                                                                                                               | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.                                          |                                                                                                                                                                  |
| `tracking_categories`                                                                                                                                            | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                          | :heavy_minus_sign:                                                                                                                                               | A list of linked tracking categories.                                                                                                                            |                                                                                                                                                                  |
| `line_items`                                                                                                                                                     | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                                        | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `billing_address`                                                                                                                                                | [Optional[models.Address]](../../models/address.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `shipping_address`                                                                                                                                               | [Optional[models.Address]](../../models/address.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `template_id`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Optional invoice template                                                                                                                                        | 123456                                                                                                                                                           |
| `source_document_url`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.                                             | https://www.invoicesolution.com/invoice/123456                                                                                                                   |
| `payment_allocations`                                                                                                                                            | List[[models.PaymentAllocations](../../models/paymentallocations.md)]                                                                                            | :heavy_minus_sign:                                                                                                                                               | IDs of payments made on the invoice                                                                                                                              |                                                                                                                                                                  |
| `payment_method`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                                      | cash                                                                                                                                                             |
| `channel`                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | The channel through which the transaction is processed.                                                                                                          | email                                                                                                                                                            |
| `language`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | language code according to ISO 639-1. For the United States - EN                                                                                                 | EN                                                                                                                                                               |
| `accounting_by_row`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                               | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.                | false                                                                                                                                                            |
| `bank_account`                                                                                                                                                   | [Optional[models.BankAccount]](../../models/bankaccount.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `ledger_account`                                                                                                                                                 | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                                    | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `custom_fields`                                                                                                                                                  | List[[models.CustomField](../../models/customfield.md)]                                                                                                          | :heavy_minus_sign:                                                                                                                                               | N/A                                                                                                                                                              |                                                                                                                                                                  |
| `row_version`                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                          | :heavy_minus_sign:                                                                                                                                               | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.                       | 1-12345                                                                                                                                                          |
| `pass_through`                                                                                                                                                   | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                                  | :heavy_minus_sign:                                                                                                                                               | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources.          |                                                                                                                                                                  |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.AccountingInvoicesUpdateResponse](../../models/accountinginvoicesupdateresponse.md)**

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

Delete Invoice

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.invoices.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_invoice_response is not None

    # Handle response
    print(res.delete_invoice_response)

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

**[models.AccountingInvoicesDeleteResponse](../../models/accountinginvoicesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |