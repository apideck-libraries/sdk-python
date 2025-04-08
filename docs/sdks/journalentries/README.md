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
import apideck_unify
from apideck_unify import Apideck
import dateutil.parser
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.journal_entries.list(consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", filter_={
        "updated_since": dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"),
    }, sort={
        "by": apideck_unify.JournalEntriesSortBy.UPDATED_AT,
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
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.JournalEntriesFilter]](../../models/journalentriesfilter.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply filters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"updated_since": "2020-09-30T07:43:32.000Z"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.JournalEntriesSort]](../../models/journalentriessort.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply sorting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"by": "updated_at",<br/>"direction": "desc"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pass_through`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {<br/>"search": "San Francisco"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

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
import apideck_unify
from apideck_unify import Apideck
import dateutil.parser
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.journal_entries.create(consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", title="Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry", currency_rate=0.69, currency=apideck_unify.Currency.USD, company_id="12345", line_items=[
        {
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "tax_amount": 27500,
            "sub_total": 27500,
            "total_amount": 27500,
            "type": apideck_unify.JournalEntryLineItemType.DEBIT,
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
            "department_id": "12345",
            "location_id": "12345",
            "line_number": 1,
        },
        {
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "tax_amount": 27500,
            "sub_total": 27500,
            "total_amount": 27500,
            "type": apideck_unify.JournalEntryLineItemType.DEBIT,
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
            "department_id": "12345",
            "location_id": "12345",
            "line_number": 1,
        },
    ], memo="Thank you for your business and have a great day!", posted_at=dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"), journal_symbol="IND", tax_type="sales", tax_code="1234", number="OIT00546", tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
        },
    ], accounting_period="01-24", row_version="1-12345", custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": [
                "<value>",
                "<value>",
                "<value>",
            ],
        },
    ], pass_through=[
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

    assert res.create_journal_entry_response is not None

    # Handle response
    print(res.create_journal_entry_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `title`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal entry title                                                                                                                                     | Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry                                                                                        |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `line_items`                                                                                                                                            | List[[models.JournalEntryLineItemInput](../../models/journalentrylineiteminput.md)]                                                                     | :heavy_minus_sign:                                                                                                                                      | Requires a minimum of 2 line items that sum to 0                                                                                                        |                                                                                                                                                         |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Reference for the journal entry.                                                                                                                        | Thank you for your business and have a great day!                                                                                                       |
| `posted_at`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.                          | 2020-09-30T07:43:32.000Z                                                                                                                                |
| `journal_symbol`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal symbol of the entry. For example IND for indirect costs                                                                                         | IND                                                                                                                                                     |
| `tax_type`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The specific category of tax associated with a transaction like sales or purchase                                                                       | sales                                                                                                                                                   |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal entry number.                                                                                                                                   | OIT00546                                                                                                                                                |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `accounting_period`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Accounting period                                                                                                                                       | 01-24                                                                                                                                                   |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.journal_entries.get(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", fields="id,updated_at")

    assert res.get_journal_entry_response is not None

    # Handle response
    print(res.get_journal_entry_response)

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
import apideck_unify
from apideck_unify import Apideck
import dateutil.parser
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.journal_entries.update(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", title="Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry", currency_rate=0.69, currency=apideck_unify.Currency.USD, company_id="12345", line_items=[
        {
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "tax_amount": 27500,
            "sub_total": 27500,
            "total_amount": 27500,
            "type": apideck_unify.JournalEntryLineItemType.DEBIT,
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
            "department_id": "12345",
            "location_id": "12345",
            "line_number": 1,
        },
        {
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "tax_amount": 27500,
            "sub_total": 27500,
            "total_amount": 27500,
            "type": apideck_unify.JournalEntryLineItemType.DEBIT,
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
            "department_id": "12345",
            "location_id": "12345",
            "line_number": 1,
        },
        {
            "description": "Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.",
            "tax_amount": 27500,
            "sub_total": 27500,
            "total_amount": 27500,
            "type": apideck_unify.JournalEntryLineItemType.DEBIT,
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
            "department_id": "12345",
            "location_id": "12345",
            "line_number": 1,
        },
    ], memo="Thank you for your business and have a great day!", posted_at=dateutil.parser.isoparse("2020-09-30T07:43:32.000Z"), journal_symbol="IND", tax_type="sales", tax_code="1234", number="OIT00546", tracking_categories=[
        {
            "id": "123456",
            "name": "New York",
        },
        {
            "id": "123456",
            "name": "New York",
        },
    ], accounting_period="01-24", row_version="1-12345", custom_fields=[
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
            "value": [
                {},
            ],
        },
    ], pass_through=[
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

    assert res.update_journal_entry_response is not None

    # Handle response
    print(res.update_journal_entry_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `title`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal entry title                                                                                                                                     | Purchase Invoice-Inventory (USD): 2019/02/01 Batch Summary Entry                                                                                        |
| `currency_rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                               | :heavy_minus_sign:                                                                                                                                      | Currency Exchange Rate at the time entity was recorded/generated.                                                                                       | 0.69                                                                                                                                                    |
| `currency`                                                                                                                                              | [OptionalNullable[models.Currency]](../../models/currency.md)                                                                                           | :heavy_minus_sign:                                                                                                                                      | Indicates the associated currency for an amount of money. Values correspond to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).                      | USD                                                                                                                                                     |
| `company_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The company or subsidiary id the transaction belongs to                                                                                                 | 12345                                                                                                                                                   |
| `line_items`                                                                                                                                            | List[[models.JournalEntryLineItemInput](../../models/journalentrylineiteminput.md)]                                                                     | :heavy_minus_sign:                                                                                                                                      | Requires a minimum of 2 line items that sum to 0                                                                                                        |                                                                                                                                                         |
| `memo`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Reference for the journal entry.                                                                                                                        | Thank you for your business and have a great day!                                                                                                       |
| `posted_at`                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                    | :heavy_minus_sign:                                                                                                                                      | This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.                          | 2020-09-30T07:43:32.000Z                                                                                                                                |
| `journal_symbol`                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal symbol of the entry. For example IND for indirect costs                                                                                         | IND                                                                                                                                                     |
| `tax_type`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The specific category of tax associated with a transaction like sales or purchase                                                                       | sales                                                                                                                                                   |
| `tax_code`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Applicable tax id/code override if tax is not supplied on a line item basis.                                                                            | 1234                                                                                                                                                    |
| `number`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Journal entry number.                                                                                                                                   | OIT00546                                                                                                                                                |
| `tracking_categories`                                                                                                                                   | List[[Nullable[models.LinkedTrackingCategory]](../../models/linkedtrackingcategory.md)]                                                                 | :heavy_minus_sign:                                                                                                                                      | A list of linked tracking categories.                                                                                                                   |                                                                                                                                                         |
| `accounting_period`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Accounting period                                                                                                                                       | 01-24                                                                                                                                                   |
| `row_version`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.              | 1-12345                                                                                                                                                 |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.journal_entries.delete(id="<id>", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce")

    assert res.delete_journal_entry_response is not None

    # Handle response
    print(res.delete_journal_entry_response)

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