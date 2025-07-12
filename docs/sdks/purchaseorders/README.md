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
import apideck_unify
from apideck_unify import Apideck
from apideck_unify.utils import parse_datetime
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.purchase_orders.list(raw=False, service_id="salesforce", pass_through={
        "search": "San Francisco",
    }, limit=20, filter_={
        "updated_since": parse_datetime("2020-09-30T07:43:32.000Z"),
        "supplier_id": "1234",
    }, sort={
        "by": apideck_unify.PurchaseOrdersSortBy.UPDATED_AT,
        "direction": apideck_unify.SortDirection.DESC,
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                             | *Optional[bool]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Include raw response. Mostly used for debugging purposes                                                                                          |                                                                                                                                                   |
| `consumer_id`                                                                                                                                     | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | ID of the consumer which you want to get or push data from                                                                                        | test-consumer                                                                                                                                     |
| `app_id`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The ID of your Unify application                                                                                                                  | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                           |
| `service_id`                                                                                                                                      | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.     | salesforce                                                                                                                                        |
| `cursor`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.                                  |                                                                                                                                                   |
| `pass_through`                                                                                                                                    | Dict[str, *Any*]                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads | {<br/>"search": "San Francisco"<br/>}                                                                                                             |
| `limit`                                                                                                                                           | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Number of results to return. Minimum 1, Maximum 200, Default 20                                                                                   |                                                                                                                                                   |
| `filter_`                                                                                                                                         | [Optional[models.PurchaseOrdersFilter]](../../models/purchaseordersfilter.md)                                                                     | :heavy_minus_sign:                                                                                                                                | Apply filters                                                                                                                                     | {<br/>"updated_since": "2020-09-30T07:43:32.000Z",<br/>"supplier_id": "1234"<br/>}                                                                |
| `sort`                                                                                                                                            | [Optional[models.PurchaseOrdersSort]](../../models/purchaseorderssort.md)                                                                         | :heavy_minus_sign:                                                                                                                                | Apply sorting                                                                                                                                     | {<br/>"by": "updated_at",<br/>"direction": "desc"<br/>}                                                                                           |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

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
import apideck_unify
from apideck_unify import Apideck
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.purchase_orders.create(raw=False, service_id="salesforce", po_number="90000117", reference="123456", supplier={
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
    }, subsidiary_id="12345", company_id="12345", status=apideck_unify.PurchaseOrderStatus.OPEN, issued_date=date.fromisoformat("2020-09-30"), delivery_date=date.fromisoformat("2020-09-30"), expected_arrival_date=date.fromisoformat("2020-09-30"), currency=apideck_unify.Currency.USD, currency_rate=0.69, sub_total=27500, total_tax=2500, total=27500, tax_inclusive=True, line_items=[
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
                    "value": 10,
                },
                {
                    "id": "2389328923893298",
                    "name": "employee_level",
                    "description": "Employee Level",
                    "value": 10,
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
    ], shipping_address={
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
    }, ledger_account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, template_id="123456", discount_percentage=5.5, bank_account={
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
    }, accounting_by_row=False, due_date=date.fromisoformat("2020-10-30"), payment_method="cash", tax_code="1234", channel="email", memo="Thank you for the partnership and have a great day!", tracking_categories=[
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
            "value": 10,
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

    assert res.create_purchase_order_response is not None

    # Handle response
    print(res.create_purchase_order_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `po_number`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A PO Number uniquely identifies a purchase order and is generally defined by the buyer.                                                                 | 90000117                                                                                                                                                |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional purchase order reference.                                                                                                                      | 123456                                                                                                                                                  |
| `supplier`                                                                                                                                              | [OptionalNullable[models.LinkedSupplierInput]](../../models/linkedsupplierinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The supplier this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `subsidiary_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the subsidiary                                                                                                                                | 12345                                                                                                                                                   |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `status`                                                                                                                                                | [OptionalNullable[models.PurchaseOrderStatus]](../../models/purchaseorderstatus.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | open                                                                                                                                                    |
| `issued_date`                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | Date purchase order was issued - YYYY-MM-DD.                                                                                                            | 2020-09-30                                                                                                                                              |
| `delivery_date`                                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date on which the purchase order is to be delivered - YYYY-MM-DD.                                                                                   | 2020-09-30                                                                                                                                              |
| `expected_arrival_date`                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date on which the order is expected to arrive - YYYY-MM-DD.                                                                                         | 2020-09-30                                                                                                                                              |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this invoice.                                                                                                               | 2500                                                                                                                                                    |
| `total`                                                                                                                                                 | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total amount of invoice, including tax.                                                                                                                 | 27500                                                                                                                                                   |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `line_items`                                                                                                                                            | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `ledger_account`                                                                                                                                        | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                           | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `template_id`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional purchase order template                                                                                                                        | 123456                                                                                                                                                  |
| `discount_percentage`                                                                                                                                   | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount percentage applied to this transaction.                                                                                                        | 5.5                                                                                                                                                     |
| `bank_account`                                                                                                                                          | [Optional[models.BankAccount]](../../models/bankaccount.md)                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `accounting_by_row`                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.       | false                                                                                                                                                   |
| `due_date`                                                                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD.                                                                   | 2020-10-30                                                                                                                                              |
| `payment_method`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                             | cash                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `channel`                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The channel through which the transaction is processed.                                                                                                 | email                                                                                                                                                   |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Message for the supplier. This text appears on the Purchase Order.                                                                                      | Thank you for the partnership and have a great day!                                                                                                     |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.purchase_orders.get(id="<id>", service_id="salesforce", raw=False)

    assert res.get_purchase_order_response is not None

    # Handle response
    print(res.get_purchase_order_response)

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
import apideck_unify
from apideck_unify import Apideck
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.purchase_orders.update(id="<id>", service_id="salesforce", raw=False, po_number="90000117", reference="123456", supplier={
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
    }, subsidiary_id="12345", company_id="12345", status=apideck_unify.PurchaseOrderStatus.OPEN, issued_date=date.fromisoformat("2020-09-30"), delivery_date=date.fromisoformat("2020-09-30"), expected_arrival_date=date.fromisoformat("2020-09-30"), currency=apideck_unify.Currency.USD, currency_rate=0.69, sub_total=27500, total_tax=2500, total=27500, tax_inclusive=True, line_items=[
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
                    "value": {

                    },
                },
            ],
            "row_version": "1-12345",
        },
    ], shipping_address={
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
    }, ledger_account={
        "id": "123456",
        "nominal_code": "N091",
        "code": "453",
    }, template_id="123456", discount_percentage=5.5, bank_account={
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
    }, accounting_by_row=False, due_date=date.fromisoformat("2020-10-30"), payment_method="cash", tax_code="1234", channel="email", memo="Thank you for the partnership and have a great day!", tracking_categories=[
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
            "value": {

            },
        },
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": {

            },
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

    assert res.update_purchase_order_response is not None

    # Handle response
    print(res.update_purchase_order_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `po_number`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A PO Number uniquely identifies a purchase order and is generally defined by the buyer.                                                                 | 90000117                                                                                                                                                |
| `reference`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional purchase order reference.                                                                                                                      | 123456                                                                                                                                                  |
| `supplier`                                                                                                                                              | [OptionalNullable[models.LinkedSupplierInput]](../../models/linkedsupplierinput.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | The supplier this entity is linked to.                                                                                                                  |                                                                                                                                                         |
| `subsidiary_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the subsidiary                                                                                                                                | 12345                                                                                                                                                   |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `status`                                                                                                                                                | [OptionalNullable[models.PurchaseOrderStatus]](../../models/purchaseorderstatus.md)                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | open                                                                                                                                                    |
| `issued_date`                                                                                                                                           | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | Date purchase order was issued - YYYY-MM-DD.                                                                                                            | 2020-09-30                                                                                                                                              |
| `delivery_date`                                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date on which the purchase order is to be delivered - YYYY-MM-DD.                                                                                   | 2020-09-30                                                                                                                                              |
| `expected_arrival_date`                                                                                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date on which the order is expected to arrive - YYYY-MM-DD.                                                                                         | 2020-09-30                                                                                                                                              |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `sub_total`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Sub-total amount, normally before tax.                                                                                                                  | 27500                                                                                                                                                   |
| `total_tax`                                                                                                                                             | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total tax amount applied to this invoice.                                                                                                               | 2500                                                                                                                                                    |
| `total`                                                                                                                                                 | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Total amount of invoice, including tax.                                                                                                                 | 27500                                                                                                                                                   |
| `tax_inclusive`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Amounts are including tax                                                                                                                               | true                                                                                                                                                    |
| `line_items`                                                                                                                                            | List[[models.InvoiceLineItemInput](../../models/invoicelineiteminput.md)]                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `shipping_address`                                                                                                                                      | [Optional[models.Address]](../../models/address.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `ledger_account`                                                                                                                                        | [OptionalNullable[models.LinkedLedgerAccountInput]](../../models/linkedledgeraccountinput.md)                                                           | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `template_id`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Optional purchase order template                                                                                                                        | 123456                                                                                                                                                  |
| `discount_percentage`                                                                                                                                   | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Discount percentage applied to this transaction.                                                                                                        | 5.5                                                                                                                                                     |
| `bank_account`                                                                                                                                          | [Optional[models.BankAccount]](../../models/bankaccount.md)                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `accounting_by_row`                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Indicates if accounting by row is used (true) or not (false). Accounting by row means that a separate ledger transaction is created for each row.       | false                                                                                                                                                   |
| `due_date`                                                                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The due date is the date on which a payment is scheduled to be received - YYYY-MM-DD.                                                                   | 2020-10-30                                                                                                                                              |
| `payment_method`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Payment method used for the transaction, such as cash, credit card, bank transfer, or check                                                             | cash                                                                                                                                                    |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `channel`                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The channel through which the transaction is processed.                                                                                                 | email                                                                                                                                                   |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Message for the supplier. This text appears on the Purchase Order.                                                                                      | Thank you for the partnership and have a great day!                                                                                                     |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.purchase_orders.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_purchase_order_response is not None

    # Handle response
    print(res.delete_purchase_order_response)

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