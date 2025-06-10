# CreditNotes
(*accounting.credit_notes*)

## Overview

### Available Operations

* [list](#list) - List Credit Notes
* [create](#create) - Create Credit Note
* [get](#get) - Get Credit Note
* [update](#update) - Update Credit Note
* [delete](#delete) - Delete Credit Note

## list

List Credit Notes

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

    res = apideck.accounting.credit_notes.list(raw=False, service_id="salesforce", limit=20, filter_={
        "updated_since": parse_datetime("2020-09-30T07:43:32.000Z"),
    }, sort={
        "by": apideck_unify.CreditNotesSortBy.UPDATED_AT,
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
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.CreditNotesFilter]](../../models/creditnotesfilter.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply filters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"updated_since": "2020-09-30T07:43:32.000Z"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.CreditNotesSort]](../../models/creditnotessort.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply sorting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"by": "updated_at",<br/>"direction": "desc"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pass_through`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {<br/>"search": "San Francisco"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.AccountingCreditNotesAllResponse](../../models/accountingcreditnotesallresponse.md)**

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

Create Credit Note

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

    res = apideck.accounting.credit_notes.create(total_amount=49.99, raw=False, service_id="salesforce", number="OIT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, company_id="12345", currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", balance=27500, remaining_credit=27500, status=apideck_unify.CreditNoteStatus.AUTHORISED, reference="123456", date_issued=parse_datetime("2021-05-01T12:00:00.000Z"), date_paid=parse_datetime("2021-05-01T12:00:00.000Z"), type_=apideck_unify.CreditNoteType.ACCOUNTS_RECEIVABLE_CREDIT, account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, line_items=[
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
                    "value": [
                        "<value 1>",
                        "<value 2>",
                    ],
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
                    "value": [
                        "<value 1>",
                        "<value 2>",
                    ],
                },
            ],
            "row_version": "1-12345",
        },
    ], allocations=[
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
    ], note="Some notes about this credit note", terms="Some terms about this credit note", billing_address={
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
        },
    ], custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": [
                "<value 1>",
                "<value 2>",
            ],
        },
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": [
                "<value 1>",
                "<value 2>",
            ],
        },
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": [
                "<value 1>",
                "<value 2>",
            ],
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
    ])

    assert res.create_credit_note_response is not None

    # Handle response
    print(res.create_credit_note_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `total_amount`                                                                                                                                          | *float*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                      | Amount of transaction                                                                                                                                   | 49.99                                                                                                                                                   |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Credit note number.                                                                                                                                     | OIT00546                                                                                                                                                |
| `customer`                                                                                                                                              | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The customer this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this invoice.                                                                                                               | 2500                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `balance`                                                                                                                                               | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | The balance reflecting any payments made against the transaction.                                                                                       | 27500                                                                                                                                                   |
| `remaining_credit`                                                                                                                                      | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Indicates the total credit amount still available to apply towards the payment.                                                                         | 27500                                                                                                                                                   |
| `status`                                                                                                                                                | [Optional[models.CreditNoteStatus]](../../models/creditnotestatus.md)                                                                                   | :heavy_minus_sign:                                                                                                                                      | Status of credit notes                                                                                                                                  | authorised                                                                                                                                              |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional reference message ie: Debit remittance detail.                                                                                                 | 123456                                                                                                                                                  |
| `date_issued`                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                     | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `date_paid`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                       | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `type`                                                                                                                                                  | [Optional[models.CreditNoteType]](../../models/creditnotetype.md)                                                                                       | :heavy_minus_sign:                                                                                                                                      | Type of payment                                                                                                                                         | accounts_receivable_credit                                                                                                                              |
| `account`                                                                                                                                               | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                           | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `line_items`                                                                                                                                            | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `allocations`                                                                                                                                           | List[[models.AllocationInput](../../models/allocationinput.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `note`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional note to be associated with the credit note.                                                                                                    | Some notes about this credit note                                                                                                                       |
| `terms`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional terms to be associated with the credit note.                                                                                                   | Some terms about this credit note                                                                                                                       |
| `billing_address`                                                                                                                                       | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingCreditNotesAddResponse](../../models/accountingcreditnotesaddresponse.md)**

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

Get Credit Note

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.credit_notes.get(id="<id>", service_id="salesforce", raw=False, fields="id,updated_at")

    assert res.get_credit_note_response is not None

    # Handle response
    print(res.get_credit_note_response)

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

**[models.AccountingCreditNotesOneResponse](../../models/accountingcreditnotesoneresponse.md)**

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

Update Credit Note

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

    res = apideck.accounting.credit_notes.update(id="<id>", total_amount=49.99, service_id="salesforce", raw=False, number="OIT00546", customer={
        "id": "12345",
        "display_name": "Windsurf Shop",
        "email": "boring@boring.com",
    }, company_id="12345", currency=apideck_unify.Currency.USD, currency_rate=0.69, tax_inclusive=True, sub_total=27500, total_tax=2500, tax_code="1234", balance=27500, remaining_credit=27500, status=apideck_unify.CreditNoteStatus.AUTHORISED, reference="123456", date_issued=parse_datetime("2021-05-01T12:00:00.000Z"), date_paid=parse_datetime("2021-05-01T12:00:00.000Z"), type_=apideck_unify.CreditNoteType.ACCOUNTS_RECEIVABLE_CREDIT, account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, line_items=[
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
    ], allocations=[
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
        {
            "id": "123456",
            "amount": 49.99,
            "allocation_id": "123456",
        },
    ], note="Some notes about this credit note", terms="Some terms about this credit note", billing_address={
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
        },
        {
            "id": "123456",
            "name": "New York",
        },
        {
            "id": "123456",
            "name": "New York",
        },
    ], custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": {},
        },
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
    ])

    assert res.update_credit_note_response is not None

    # Handle response
    print(res.update_credit_note_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `total_amount`                                                                                                                                          | *float*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                      | Amount of transaction                                                                                                                                   | 49.99                                                                                                                                                   |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Credit note number.                                                                                                                                     | OIT00546                                                                                                                                                |
| `customer`                                                                                                                                              | [OptionalNullable[models.LinkedCustomerInput]](../../models/linkedcustomerinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The customer this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this invoice.                                                                                                               | 2500                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `balance`                                                                                                                                               | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | The balance reflecting any payments made against the transaction.                                                                                       | 27500                                                                                                                                                   |
| `remaining_credit`                                                                                                                                      | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Indicates the total credit amount still available to apply towards the payment.                                                                         | 27500                                                                                                                                                   |
| `status`                                                                                                                                                | [Optional[models.CreditNoteStatus]](../../models/creditnotestatus.md)                                                                                   | :heavy_minus_sign:                                                                                                                                      | Status of credit notes                                                                                                                                  | authorised                                                                                                                                              |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional reference message ie: Debit remittance detail.                                                                                                 | 123456                                                                                                                                                  |
| `date_issued`                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                     | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `date_paid`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                       | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `type`                                                                                                                                                  | [Optional[models.CreditNoteType]](../../models/creditnotetype.md)                                                                                       | :heavy_minus_sign:                                                                                                                                      | Type of payment                                                                                                                                         | accounts_receivable_credit                                                                                                                              |
| `account`                                                                                                                                               | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                           | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `line_items`                                                                                                                                            | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `allocations`                                                                                                                                           | List[[models.AllocationInput](../../models/allocationinput.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `note`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional note to be associated with the credit note.                                                                                                    | Some notes about this credit note                                                                                                                       |
| `terms`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional terms to be associated with the credit note.                                                                                                   | Some terms about this credit note                                                                                                                       |
| `billing_address`                                                                                                                                       | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingCreditNotesUpdateResponse](../../models/accountingcreditnotesupdateresponse.md)**

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

Delete Credit Note

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.credit_notes.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_credit_note_response is not None

    # Handle response
    print(res.delete_credit_note_response)

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

**[models.AccountingCreditNotesDeleteResponse](../../models/accountingcreditnotesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |