# Expenses
(*accounting.expenses*)

## Overview

### Available Operations

* [list](#list) - List Expenses
* [create](#create) - Create Expense
* [get](#get) - Get Expense
* [update](#update) - Update Expense
* [delete](#delete) - Delete Expense

## list

List Expenses

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.expenses.list(consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

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

**[models.AccountingExpensesAllResponse](../../models/accountingexpensesallresponse.md)**

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

Create Expense

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
) as apideck:

    res = apideck.accounting.expenses.create(transaction_date=dateutil.parser.isoparse("2021-05-01T12:00:00.000Z"), account_id="123456", line_items=[
        {
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
            "account_id": "123456",
            "customer_id": "12345",
            "department_id": "12345",
            "location_id": "12345",
            "subsidiary_id": "12345",
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "description": "Travel US.",
            "total_amount": 275,
            "billable": True,
        },
    ], consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", number="OIT00546", customer_id="12345", supplier_id="12345", company_id="12345", department_id="12345", payment_type=apideck_unify.ExpensePaymentType.CASH, currency=apideck_unify.Currency.USD, currency_rate=0.69, type_=apideck_unify.ExpenseType.EXPENSE, memo="For travel expenses incurred on 2024-05-15", tax_rate={
        "id": "123456",
        "rate": 10,
    }, total_amount=275, custom_fields=[
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
    ])

    assert res.create_expense_response is not None

    # Handle response
    print(res.create_expense_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transaction_date`                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_check_mark:                                                                                                                                      | The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                 | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `account_id`                                                                                                                                            | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | The unique identifier for the ledger account that this expense should be credited to.                                                                   | 123456                                                                                                                                                  |
| `line_items`                                                                                                                                            | List[[models.ExpenseLineItemInput](../../models/expenselineiteminput.md)]                                                                               | :heavy_check_mark:                                                                                                                                      | Expense line items linked to this expense.                                                                                                              |                                                                                                                                                         |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Number.                                                                                                                                                 | OIT00546                                                                                                                                                |
| `customer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of the customer this entity is linked to. Used for expenses that should be marked as billable to customers.                                      | 12345                                                                                                                                                   |
| `supplier_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of the supplier this entity is linked to.                                                                                                        | 12345                                                                                                                                                   |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `department_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the department                                                                                                                                | 12345                                                                                                                                                   |
| `payment_type`                                                                                                                                          | [OptionalNullable[models.ExpensePaymentType]](../../models/expensepaymenttype.md)                                                                       | :heavy_minus_sign:                                                                                                                                      | The type of payment for the expense.                                                                                                                    | cash                                                                                                                                                    |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `type`                                                                                                                                                  | [OptionalNullable[models.ExpenseType]](../../models/expensetype.md)                                                                                     | :heavy_minus_sign:                                                                                                                                      | The type of expense.                                                                                                                                    | expense                                                                                                                                                 |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The memo of the expense.                                                                                                                                | For travel expenses incurred on 2024-05-15                                                                                                              |
| `tax_rate`                                                                                                                                              | [Optional[models.LinkedTaxRateInput]](../../models/linkedtaxrateinput.md)                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `total_amount`                                                                                                                                          | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | The total amount of the expense line item.                                                                                                              | 275                                                                                                                                                     |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingExpensesAddResponse](../../models/accountingexpensesaddresponse.md)**

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

Get Expense

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.expenses.get(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

    assert res.get_expense_response is not None

    # Handle response
    print(res.get_expense_response)

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

**[models.AccountingExpensesOneResponse](../../models/accountingexpensesoneresponse.md)**

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

Update Expense

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
) as apideck:

    res = apideck.accounting.expenses.update(id="<id>", transaction_date=dateutil.parser.isoparse("2021-05-01T12:00:00.000Z"), account_id="123456", line_items=[
        {
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
            "account_id": "123456",
            "customer_id": "12345",
            "department_id": "12345",
            "location_id": "12345",
            "subsidiary_id": "12345",
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "description": "Travel US.",
            "total_amount": 275,
            "billable": True,
        },
        {
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
            "account_id": "123456",
            "customer_id": "12345",
            "department_id": "12345",
            "location_id": "12345",
            "subsidiary_id": "12345",
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "description": "Travel US.",
            "total_amount": 275,
            "billable": True,
        },
        {
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
            "account_id": "123456",
            "customer_id": "12345",
            "department_id": "12345",
            "location_id": "12345",
            "subsidiary_id": "12345",
            "tax_rate": {
                "id": "123456",
                "rate": 10,
            },
            "description": "Travel US.",
            "total_amount": 275,
            "billable": True,
        },
    ], consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", number="OIT00546", customer_id="12345", supplier_id="12345", company_id="12345", department_id="12345", payment_type=apideck_unify.ExpensePaymentType.CASH, currency=apideck_unify.Currency.USD, currency_rate=0.69, type_=apideck_unify.ExpenseType.EXPENSE, memo="For travel expenses incurred on 2024-05-15", tax_rate={
        "id": "123456",
        "rate": 10,
    }, total_amount=275, custom_fields=[
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

    assert res.update_expense_response is not None

    # Handle response
    print(res.update_expense_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `transaction_date`                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_check_mark:                                                                                                                                      | The date of the transaction - YYYY:MM::DDThh:mm:ss.sTZD                                                                                                 | 2021-05-01T12:00:00.000Z                                                                                                                                |
| `account_id`                                                                                                                                            | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | The unique identifier for the ledger account that this expense should be credited to.                                                                   | 123456                                                                                                                                                  |
| `line_items`                                                                                                                                            | List[[models.ExpenseLineItemInput](../../models/expenselineiteminput.md)]                                                                               | :heavy_check_mark:                                                                                                                                      | Expense line items linked to this expense.                                                                                                              |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Number.                                                                                                                                                 | OIT00546                                                                                                                                                |
| `customer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of the customer this entity is linked to. Used for expenses that should be marked as billable to customers.                                      | 12345                                                                                                                                                   |
| `supplier_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of the supplier this entity is linked to.                                                                                                        | 12345                                                                                                                                                   |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `department_id`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The ID of the department                                                                                                                                | 12345                                                                                                                                                   |
| `payment_type`                                                                                                                                          | [OptionalNullable[models.ExpensePaymentType]](../../models/expensepaymenttype.md)                                                                       | :heavy_minus_sign:                                                                                                                                      | The type of payment for the expense.                                                                                                                    | cash                                                                                                                                                    |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `type`                                                                                                                                                  | [OptionalNullable[models.ExpenseType]](../../models/expensetype.md)                                                                                     | :heavy_minus_sign:                                                                                                                                      | The type of expense.                                                                                                                                    | expense                                                                                                                                                 |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The memo of the expense.                                                                                                                                | For travel expenses incurred on 2024-05-15                                                                                                              |
| `tax_rate`                                                                                                                                              | [Optional[models.LinkedTaxRateInput]](../../models/linkedtaxrateinput.md)                                                                               | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `total_amount`                                                                                                                                          | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | The total amount of the expense line item.                                                                                                              | 275                                                                                                                                                     |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.AccountingExpensesUpdateResponse](../../models/accountingexpensesupdateresponse.md)**

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

Delete Expense

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.expenses.delete(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

    assert res.delete_expense_response is not None

    # Handle response
    print(res.delete_expense_response)

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

**[models.AccountingExpensesDeleteResponse](../../models/accountingexpensesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |