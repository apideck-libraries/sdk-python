# apideck-unify

Developer-friendly & type-safe Python SDK specifically catered to leverage *apideck-unify* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=apideck-unify&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<!-- Start Summary [summary] -->
## Summary

Apideck: The Apideck OpenAPI Spec: SDK Optimized

For more information about the API: [Apideck Developer Docs](https://developers.apideck.com)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [apideck-unify](#apideck-unify)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install apideck-unify
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add apideck-unify
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from apideck-unify python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "apideck-unify",
# ]
# ///

from apideck_unify import Apideck

sdk = Apideck(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from apideck_unify import Apideck
import asyncio
import os

async def main():

    async with Apideck(
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        api_key=os.getenv("APIDECK_API_KEY", ""),
    ) as apideck:

        res = await apideck.accounting.tax_rates.list_async(raw=False, service_id="salesforce", limit=20, filter_={
            "assets": True,
            "equity": True,
            "expenses": True,
            "liabilities": True,
            "revenue": True,
        }, pass_through={
            "search": "San Francisco",
        }, fields="id,updated_at")

        while res is not None:
            # Handle items

            res = res.next()

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      | Environment Variable |
| --------- | ---- | ----------- | -------------------- |
| `api_key` | http | HTTP Bearer | `APIDECK_API_KEY`    |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [accounting](docs/sdks/accounting/README.md)


#### [accounting.aged_creditors](docs/sdks/agedcreditorssdk/README.md)

* [get](docs/sdks/agedcreditorssdk/README.md#get) - Get Aged Creditors

#### [accounting.aged_debtors](docs/sdks/ageddebtorssdk/README.md)

* [get](docs/sdks/ageddebtorssdk/README.md#get) - Get Aged Debtors

#### [accounting.attachments](docs/sdks/attachments/README.md)

* [list](docs/sdks/attachments/README.md#list) - List Attachments
* [upload](docs/sdks/attachments/README.md#upload) - Upload attachment
* [get](docs/sdks/attachments/README.md#get) - Get Attachment
* [delete](docs/sdks/attachments/README.md#delete) - Delete Attachment
* [download](docs/sdks/attachments/README.md#download) - Download Attachment

#### [accounting.balance_sheet](docs/sdks/balancesheetsdk/README.md)

* [get](docs/sdks/balancesheetsdk/README.md#get) - Get BalanceSheet

#### [accounting.bank_feed_accounts](docs/sdks/bankfeedaccounts/README.md)

* [list](docs/sdks/bankfeedaccounts/README.md#list) - List Bank Feed Accounts
* [create](docs/sdks/bankfeedaccounts/README.md#create) - Create Bank Feed Account
* [get](docs/sdks/bankfeedaccounts/README.md#get) - Get Bank Feed Account
* [update](docs/sdks/bankfeedaccounts/README.md#update) - Update Bank Feed Account
* [delete](docs/sdks/bankfeedaccounts/README.md#delete) - Delete Bank Feed Account

#### [accounting.bank_feed_statements](docs/sdks/bankfeedstatements/README.md)

* [list](docs/sdks/bankfeedstatements/README.md#list) - List Bank Feed Statements
* [create](docs/sdks/bankfeedstatements/README.md#create) - Create Bank Feed Statement
* [get](docs/sdks/bankfeedstatements/README.md#get) - Get Bank Feed Statement
* [update](docs/sdks/bankfeedstatements/README.md#update) - Update Bank Feed Statement
* [delete](docs/sdks/bankfeedstatements/README.md#delete) - Delete Bank Feed Statement

#### [accounting.bill_payments](docs/sdks/billpayments/README.md)

* [list](docs/sdks/billpayments/README.md#list) - List Bill Payments
* [create](docs/sdks/billpayments/README.md#create) - Create Bill Payment
* [get](docs/sdks/billpayments/README.md#get) - Get Bill Payment
* [update](docs/sdks/billpayments/README.md#update) - Update Bill Payment
* [delete](docs/sdks/billpayments/README.md#delete) - Delete Bill Payment

#### [accounting.bills](docs/sdks/bills/README.md)

* [list](docs/sdks/bills/README.md#list) - List Bills
* [create](docs/sdks/bills/README.md#create) - Create Bill
* [get](docs/sdks/bills/README.md#get) - Get Bill
* [update](docs/sdks/bills/README.md#update) - Update Bill
* [delete](docs/sdks/bills/README.md#delete) - Delete Bill

#### [accounting.categories](docs/sdks/categories/README.md)

* [list](docs/sdks/categories/README.md#list) - List Categories
* [get](docs/sdks/categories/README.md#get) - Get Category

#### [accounting.company_info](docs/sdks/companyinfosdk/README.md)

* [get](docs/sdks/companyinfosdk/README.md#get) - Get company info

#### [accounting.credit_notes](docs/sdks/creditnotes/README.md)

* [list](docs/sdks/creditnotes/README.md#list) - List Credit Notes
* [create](docs/sdks/creditnotes/README.md#create) - Create Credit Note
* [get](docs/sdks/creditnotes/README.md#get) - Get Credit Note
* [update](docs/sdks/creditnotes/README.md#update) - Update Credit Note
* [delete](docs/sdks/creditnotes/README.md#delete) - Delete Credit Note

#### [accounting.customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - List Customers
* [create](docs/sdks/customers/README.md#create) - Create Customer
* [get](docs/sdks/customers/README.md#get) - Get Customer
* [update](docs/sdks/customers/README.md#update) - Update Customer
* [delete](docs/sdks/customers/README.md#delete) - Delete Customer

#### [accounting.departments](docs/sdks/departments/README.md)

* [list](docs/sdks/departments/README.md#list) - List Departments
* [create](docs/sdks/departments/README.md#create) - Create Department
* [get](docs/sdks/departments/README.md#get) - Get Department
* [update](docs/sdks/departments/README.md#update) - Update Department
* [delete](docs/sdks/departments/README.md#delete) - Delete Department

#### [accounting.expenses](docs/sdks/expenses/README.md)

* [list](docs/sdks/expenses/README.md#list) - List Expenses
* [create](docs/sdks/expenses/README.md#create) - Create Expense
* [get](docs/sdks/expenses/README.md#get) - Get Expense
* [update](docs/sdks/expenses/README.md#update) - Update Expense
* [delete](docs/sdks/expenses/README.md#delete) - Delete Expense

#### [accounting.invoice_items](docs/sdks/invoiceitems/README.md)

* [list](docs/sdks/invoiceitems/README.md#list) - List Invoice Items
* [create](docs/sdks/invoiceitems/README.md#create) - Create Invoice Item
* [get](docs/sdks/invoiceitems/README.md#get) - Get Invoice Item
* [update](docs/sdks/invoiceitems/README.md#update) - Update Invoice Item
* [delete](docs/sdks/invoiceitems/README.md#delete) - Delete Invoice Item

#### [accounting.invoices](docs/sdks/invoices/README.md)

* [list](docs/sdks/invoices/README.md#list) - List Invoices
* [create](docs/sdks/invoices/README.md#create) - Create Invoice
* [get](docs/sdks/invoices/README.md#get) - Get Invoice
* [update](docs/sdks/invoices/README.md#update) - Update Invoice
* [delete](docs/sdks/invoices/README.md#delete) - Delete Invoice

#### [accounting.journal_entries](docs/sdks/journalentries/README.md)

* [list](docs/sdks/journalentries/README.md#list) - List Journal Entries
* [create](docs/sdks/journalentries/README.md#create) - Create Journal Entry
* [get](docs/sdks/journalentries/README.md#get) - Get Journal Entry
* [update](docs/sdks/journalentries/README.md#update) - Update Journal Entry
* [delete](docs/sdks/journalentries/README.md#delete) - Delete Journal Entry

#### [accounting.ledger_accounts](docs/sdks/ledgeraccounts/README.md)

* [list](docs/sdks/ledgeraccounts/README.md#list) - List Ledger Accounts
* [create](docs/sdks/ledgeraccounts/README.md#create) - Create Ledger Account
* [get](docs/sdks/ledgeraccounts/README.md#get) - Get Ledger Account
* [update](docs/sdks/ledgeraccounts/README.md#update) - Update Ledger Account
* [delete](docs/sdks/ledgeraccounts/README.md#delete) - Delete Ledger Account

#### [accounting.locations](docs/sdks/locations/README.md)

* [list](docs/sdks/locations/README.md#list) - List Locations
* [create](docs/sdks/locations/README.md#create) - Create Location
* [get](docs/sdks/locations/README.md#get) - Get Location
* [update](docs/sdks/locations/README.md#update) - Update Location
* [delete](docs/sdks/locations/README.md#delete) - Delete Location

#### [accounting.payments](docs/sdks/payments/README.md)

* [list](docs/sdks/payments/README.md#list) - List Payments
* [create](docs/sdks/payments/README.md#create) - Create Payment
* [get](docs/sdks/payments/README.md#get) - Get Payment
* [update](docs/sdks/payments/README.md#update) - Update Payment
* [delete](docs/sdks/payments/README.md#delete) - Delete Payment

#### [accounting.profit_and_loss](docs/sdks/profitandlosssdk/README.md)

* [get](docs/sdks/profitandlosssdk/README.md#get) - Get Profit and Loss

#### [accounting.purchase_orders](docs/sdks/purchaseorders/README.md)

* [list](docs/sdks/purchaseorders/README.md#list) - List Purchase Orders
* [create](docs/sdks/purchaseorders/README.md#create) - Create Purchase Order
* [get](docs/sdks/purchaseorders/README.md#get) - Get Purchase Order
* [update](docs/sdks/purchaseorders/README.md#update) - Update Purchase Order
* [delete](docs/sdks/purchaseorders/README.md#delete) - Delete Purchase Order

#### [accounting.subsidiaries](docs/sdks/subsidiaries/README.md)

* [list](docs/sdks/subsidiaries/README.md#list) - List Subsidiaries
* [create](docs/sdks/subsidiaries/README.md#create) - Create Subsidiary
* [get](docs/sdks/subsidiaries/README.md#get) - Get Subsidiary
* [update](docs/sdks/subsidiaries/README.md#update) - Update Subsidiary
* [delete](docs/sdks/subsidiaries/README.md#delete) - Delete Subsidiary

#### [accounting.suppliers](docs/sdks/suppliers/README.md)

* [list](docs/sdks/suppliers/README.md#list) - List Suppliers
* [create](docs/sdks/suppliers/README.md#create) - Create Supplier
* [get](docs/sdks/suppliers/README.md#get) - Get Supplier
* [update](docs/sdks/suppliers/README.md#update) - Update Supplier
* [delete](docs/sdks/suppliers/README.md#delete) - Delete Supplier

#### [accounting.tax_rates](docs/sdks/taxrates/README.md)

* [list](docs/sdks/taxrates/README.md#list) - List Tax Rates
* [create](docs/sdks/taxrates/README.md#create) - Create Tax Rate
* [get](docs/sdks/taxrates/README.md#get) - Get Tax Rate
* [update](docs/sdks/taxrates/README.md#update) - Update Tax Rate
* [delete](docs/sdks/taxrates/README.md#delete) - Delete Tax Rate

#### [accounting.tracking_categories](docs/sdks/trackingcategories/README.md)

* [list](docs/sdks/trackingcategories/README.md#list) - List Tracking Categories
* [create](docs/sdks/trackingcategories/README.md#create) - Create Tracking Category
* [get](docs/sdks/trackingcategories/README.md#get) - Get Tracking Category
* [update](docs/sdks/trackingcategories/README.md#update) - Update Tracking Category
* [delete](docs/sdks/trackingcategories/README.md#delete) - Delete Tracking Category


### [ats](docs/sdks/ats/README.md)


#### [ats.applicants](docs/sdks/applicants/README.md)

* [list](docs/sdks/applicants/README.md#list) - List Applicants
* [create](docs/sdks/applicants/README.md#create) - Create Applicant
* [get](docs/sdks/applicants/README.md#get) - Get Applicant
* [update](docs/sdks/applicants/README.md#update) - Update Applicant
* [delete](docs/sdks/applicants/README.md#delete) - Delete Applicant

#### [ats.applications](docs/sdks/applications/README.md)

* [list](docs/sdks/applications/README.md#list) - List Applications
* [create](docs/sdks/applications/README.md#create) - Create Application
* [get](docs/sdks/applications/README.md#get) - Get Application
* [update](docs/sdks/applications/README.md#update) - Update Application
* [delete](docs/sdks/applications/README.md#delete) - Delete Application

#### [ats.jobs](docs/sdks/jobs/README.md)

* [list](docs/sdks/jobs/README.md#list) - List Jobs
* [get](docs/sdks/jobs/README.md#get) - Get Job

### [connector](docs/sdks/connectorsdk/README.md)


#### [connector.api_resource_coverage](docs/sdks/apiresourcecoveragesdk/README.md)

* [get](docs/sdks/apiresourcecoveragesdk/README.md#get) - Get API Resource Coverage

#### [connector.api_resources](docs/sdks/apiresources/README.md)

* [get](docs/sdks/apiresources/README.md#get) - Get API Resource

#### [connector.apis](docs/sdks/apis/README.md)

* [list](docs/sdks/apis/README.md#list) - List APIs
* [get](docs/sdks/apis/README.md#get) - Get API

#### [connector.connector_docs](docs/sdks/connectordocs/README.md)

* [get](docs/sdks/connectordocs/README.md#get) - Get Connector Doc content

#### [connector.connector_resources](docs/sdks/connectorresources/README.md)

* [get](docs/sdks/connectorresources/README.md#get) - Get Connector Resource

#### [connector.connectors](docs/sdks/connectors/README.md)

* [list](docs/sdks/connectors/README.md#list) - List Connectors
* [get](docs/sdks/connectors/README.md#get) - Get Connector

### [crm](docs/sdks/crm/README.md)


#### [crm.activities](docs/sdks/activities/README.md)

* [list](docs/sdks/activities/README.md#list) - List activities
* [create](docs/sdks/activities/README.md#create) - Create activity
* [get](docs/sdks/activities/README.md#get) - Get activity
* [update](docs/sdks/activities/README.md#update) - Update activity
* [delete](docs/sdks/activities/README.md#delete) - Delete activity

#### [crm.companies](docs/sdks/companies/README.md)

* [list](docs/sdks/companies/README.md#list) - List companies
* [create](docs/sdks/companies/README.md#create) - Create company
* [get](docs/sdks/companies/README.md#get) - Get company
* [update](docs/sdks/companies/README.md#update) - Update company
* [delete](docs/sdks/companies/README.md#delete) - Delete company

#### [crm.contacts](docs/sdks/contacts/README.md)

* [list](docs/sdks/contacts/README.md#list) - List contacts
* [create](docs/sdks/contacts/README.md#create) - Create contact
* [get](docs/sdks/contacts/README.md#get) - Get contact
* [update](docs/sdks/contacts/README.md#update) - Update contact
* [delete](docs/sdks/contacts/README.md#delete) - Delete contact

#### [crm.custom_object_schemas](docs/sdks/customobjectschemas/README.md)

* [list](docs/sdks/customobjectschemas/README.md#list) - List custom object schemas
* [create](docs/sdks/customobjectschemas/README.md#create) - Create custom object schema
* [get](docs/sdks/customobjectschemas/README.md#get) - Get custom object schema
* [update](docs/sdks/customobjectschemas/README.md#update) - Update custom object schema
* [delete](docs/sdks/customobjectschemas/README.md#delete) - Delete custom object schema

#### [crm.custom_objects](docs/sdks/customobjects/README.md)

* [list](docs/sdks/customobjects/README.md#list) - List custom objects
* [create](docs/sdks/customobjects/README.md#create) - Create custom object
* [get](docs/sdks/customobjects/README.md#get) - Get custom object
* [update](docs/sdks/customobjects/README.md#update) - Update custom object
* [delete](docs/sdks/customobjects/README.md#delete) - Delete custom object

#### [crm.leads](docs/sdks/leads/README.md)

* [list](docs/sdks/leads/README.md#list) - List leads
* [create](docs/sdks/leads/README.md#create) - Create lead
* [get](docs/sdks/leads/README.md#get) - Get lead
* [update](docs/sdks/leads/README.md#update) - Update lead
* [delete](docs/sdks/leads/README.md#delete) - Delete lead

#### [crm.notes](docs/sdks/notes/README.md)

* [list](docs/sdks/notes/README.md#list) - List notes
* [create](docs/sdks/notes/README.md#create) - Create note
* [get](docs/sdks/notes/README.md#get) - Get note
* [update](docs/sdks/notes/README.md#update) - Update note
* [delete](docs/sdks/notes/README.md#delete) - Delete note

#### [crm.opportunities](docs/sdks/opportunities/README.md)

* [list](docs/sdks/opportunities/README.md#list) - List opportunities
* [create](docs/sdks/opportunities/README.md#create) - Create opportunity
* [get](docs/sdks/opportunities/README.md#get) - Get opportunity
* [update](docs/sdks/opportunities/README.md#update) - Update opportunity
* [delete](docs/sdks/opportunities/README.md#delete) - Delete opportunity

#### [crm.pipelines](docs/sdks/pipelines/README.md)

* [list](docs/sdks/pipelines/README.md#list) - List pipelines
* [create](docs/sdks/pipelines/README.md#create) - Create pipeline
* [get](docs/sdks/pipelines/README.md#get) - Get pipeline
* [update](docs/sdks/pipelines/README.md#update) - Update pipeline
* [delete](docs/sdks/pipelines/README.md#delete) - Delete pipeline

#### [crm.users](docs/sdks/users/README.md)

* [list](docs/sdks/users/README.md#list) - List users
* [create](docs/sdks/users/README.md#create) - Create user
* [get](docs/sdks/users/README.md#get) - Get user
* [update](docs/sdks/users/README.md#update) - Update user
* [delete](docs/sdks/users/README.md#delete) - Delete user

### [ecommerce](docs/sdks/ecommerce/README.md)


#### [ecommerce.customers](docs/sdks/apideckcustomers/README.md)

* [list](docs/sdks/apideckcustomers/README.md#list) - List Customers
* [get](docs/sdks/apideckcustomers/README.md#get) - Get Customer

#### [ecommerce.orders](docs/sdks/orders/README.md)

* [list](docs/sdks/orders/README.md#list) - List Orders
* [get](docs/sdks/orders/README.md#get) - Get Order

#### [ecommerce.products](docs/sdks/products/README.md)

* [list](docs/sdks/products/README.md#list) - List Products
* [get](docs/sdks/products/README.md#get) - Get Product

#### [ecommerce.stores](docs/sdks/stores/README.md)

* [get](docs/sdks/stores/README.md#get) - Get Store

### [file_storage](docs/sdks/filestorage/README.md)


#### [file_storage.drive_groups](docs/sdks/drivegroups/README.md)

* [list](docs/sdks/drivegroups/README.md#list) - List DriveGroups
* [create](docs/sdks/drivegroups/README.md#create) - Create DriveGroup
* [get](docs/sdks/drivegroups/README.md#get) - Get DriveGroup
* [update](docs/sdks/drivegroups/README.md#update) - Update DriveGroup
* [delete](docs/sdks/drivegroups/README.md#delete) - Delete DriveGroup

#### [file_storage.drives](docs/sdks/drives/README.md)

* [list](docs/sdks/drives/README.md#list) - List Drives
* [create](docs/sdks/drives/README.md#create) - Create Drive
* [get](docs/sdks/drives/README.md#get) - Get Drive
* [update](docs/sdks/drives/README.md#update) - Update Drive
* [delete](docs/sdks/drives/README.md#delete) - Delete Drive

#### [file_storage.files](docs/sdks/files/README.md)

* [list](docs/sdks/files/README.md#list) - List Files
* [search](docs/sdks/files/README.md#search) - Search Files
* [get](docs/sdks/files/README.md#get) - Get File
* [update](docs/sdks/files/README.md#update) - Rename or move File
* [delete](docs/sdks/files/README.md#delete) - Delete File
* [download](docs/sdks/files/README.md#download) - Download File
* [export](docs/sdks/files/README.md#export) - Export File

#### [file_storage.folders](docs/sdks/folders/README.md)

* [create](docs/sdks/folders/README.md#create) - Create Folder
* [get](docs/sdks/folders/README.md#get) - Get Folder
* [update](docs/sdks/folders/README.md#update) - Rename or move Folder
* [delete](docs/sdks/folders/README.md#delete) - Delete Folder
* [copy](docs/sdks/folders/README.md#copy) - Copy Folder

#### [file_storage.shared_links](docs/sdks/sharedlinks/README.md)

* [list](docs/sdks/sharedlinks/README.md#list) - List SharedLinks
* [create](docs/sdks/sharedlinks/README.md#create) - Create Shared Link
* [get](docs/sdks/sharedlinks/README.md#get) - Get Shared Link
* [update](docs/sdks/sharedlinks/README.md#update) - Update Shared Link
* [delete](docs/sdks/sharedlinks/README.md#delete) - Delete Shared Link

#### [file_storage.upload_sessions](docs/sdks/uploadsessions/README.md)

* [create](docs/sdks/uploadsessions/README.md#create) - Start Upload Session
* [get](docs/sdks/uploadsessions/README.md#get) - Get Upload Session
* [upload](docs/sdks/uploadsessions/README.md#upload) - Upload part of File to Upload Session
* [delete](docs/sdks/uploadsessions/README.md#delete) - Abort Upload Session
* [finish](docs/sdks/uploadsessions/README.md#finish) - Finish Upload Session

### [hris](docs/sdks/hris/README.md)


#### [hris.companies](docs/sdks/apideckcompanies/README.md)

* [list](docs/sdks/apideckcompanies/README.md#list) - List Companies
* [create](docs/sdks/apideckcompanies/README.md#create) - Create Company
* [get](docs/sdks/apideckcompanies/README.md#get) - Get Company
* [update](docs/sdks/apideckcompanies/README.md#update) - Update Company
* [delete](docs/sdks/apideckcompanies/README.md#delete) - Delete Company

#### [hris.departments](docs/sdks/apideckdepartments/README.md)

* [list](docs/sdks/apideckdepartments/README.md#list) - List Departments
* [create](docs/sdks/apideckdepartments/README.md#create) - Create Department
* [get](docs/sdks/apideckdepartments/README.md#get) - Get Department
* [update](docs/sdks/apideckdepartments/README.md#update) - Update Department
* [delete](docs/sdks/apideckdepartments/README.md#delete) - Delete Department

#### [hris.employee_payrolls](docs/sdks/employeepayrolls/README.md)

* [list](docs/sdks/employeepayrolls/README.md#list) - List Employee Payrolls
* [get](docs/sdks/employeepayrolls/README.md#get) - Get Employee Payroll

#### [hris.employee_schedules](docs/sdks/employeeschedulessdk/README.md)

* [list](docs/sdks/employeeschedulessdk/README.md#list) - List Employee Schedules

#### [hris.employees](docs/sdks/employees/README.md)

* [list](docs/sdks/employees/README.md#list) - List Employees
* [create](docs/sdks/employees/README.md#create) - Create Employee
* [get](docs/sdks/employees/README.md#get) - Get Employee
* [update](docs/sdks/employees/README.md#update) - Update Employee
* [delete](docs/sdks/employees/README.md#delete) - Delete Employee

#### [hris.payrolls](docs/sdks/payrolls/README.md)

* [list](docs/sdks/payrolls/README.md#list) - List Payroll
* [get](docs/sdks/payrolls/README.md#get) - Get Payroll

#### [hris.time_off_requests](docs/sdks/timeoffrequests/README.md)

* [list](docs/sdks/timeoffrequests/README.md#list) - List Time Off Requests
* [create](docs/sdks/timeoffrequests/README.md#create) - Create Time Off Request
* [get](docs/sdks/timeoffrequests/README.md#get) - Get Time Off Request
* [update](docs/sdks/timeoffrequests/README.md#update) - Update Time Off Request
* [delete](docs/sdks/timeoffrequests/README.md#delete) - Delete Time Off Request

### [issue_tracking](docs/sdks/issuetracking/README.md)


#### [issue_tracking.collection_tags](docs/sdks/collectiontags/README.md)

* [list](docs/sdks/collectiontags/README.md#list) - List Tags

#### [issue_tracking.collection_ticket_comments](docs/sdks/collectionticketcomments/README.md)

* [list](docs/sdks/collectionticketcomments/README.md#list) - List Comments
* [create](docs/sdks/collectionticketcomments/README.md#create) - Create Comment
* [get](docs/sdks/collectionticketcomments/README.md#get) - Get Comment
* [update](docs/sdks/collectionticketcomments/README.md#update) - Update Comment
* [delete](docs/sdks/collectionticketcomments/README.md#delete) - Delete Comment

#### [issue_tracking.collection_tickets](docs/sdks/collectiontickets/README.md)

* [list](docs/sdks/collectiontickets/README.md#list) - List Tickets
* [create](docs/sdks/collectiontickets/README.md#create) - Create Ticket
* [get](docs/sdks/collectiontickets/README.md#get) - Get Ticket
* [update](docs/sdks/collectiontickets/README.md#update) - Update Ticket
* [delete](docs/sdks/collectiontickets/README.md#delete) - Delete Ticket

#### [issue_tracking.collection_users](docs/sdks/collectionusers/README.md)

* [list](docs/sdks/collectionusers/README.md#list) - List Users
* [get](docs/sdks/collectionusers/README.md#get) - Get user

#### [issue_tracking.collections](docs/sdks/collections/README.md)

* [list](docs/sdks/collections/README.md#list) - List Collections
* [get](docs/sdks/collections/README.md#get) - Get Collection

### [sms](docs/sdks/sms/README.md)


#### [sms.messages](docs/sdks/messages/README.md)

* [list](docs/sdks/messages/README.md#list) - List Messages
* [create](docs/sdks/messages/README.md#create) - Create Message
* [get](docs/sdks/messages/README.md#get) - Get Message
* [update](docs/sdks/messages/README.md#update) - Update Message
* [delete](docs/sdks/messages/README.md#delete) - Delete Message

### [vault](docs/sdks/vault/README.md)


#### [vault.connection_custom_mappings](docs/sdks/connectioncustommappings/README.md)

* [list](docs/sdks/connectioncustommappings/README.md#list) - List connection custom mappings

#### [vault.connection_settings](docs/sdks/connectionsettings/README.md)

* [list](docs/sdks/connectionsettings/README.md#list) - Get resource settings
* [update](docs/sdks/connectionsettings/README.md#update) - Update settings

#### [vault.connections](docs/sdks/connections/README.md)

* [list](docs/sdks/connections/README.md#list) - Get all connections
* [get](docs/sdks/connections/README.md#get) - Get connection
* [update](docs/sdks/connections/README.md#update) - Update connection
* [delete](docs/sdks/connections/README.md#delete) - Deletes a connection
* [imports](docs/sdks/connections/README.md#imports) - Import connection
* [token](docs/sdks/connections/README.md#token) - Authorize Access Token

#### [vault.consumer_request_counts](docs/sdks/consumerrequestcounts/README.md)

* [list](docs/sdks/consumerrequestcounts/README.md#list) - Consumer request counts

#### [vault.consumers](docs/sdks/consumers/README.md)

* [create](docs/sdks/consumers/README.md#create) - Create consumer
* [list](docs/sdks/consumers/README.md#list) - Get all consumers
* [get](docs/sdks/consumers/README.md#get) - Get consumer
* [update](docs/sdks/consumers/README.md#update) - Update consumer
* [delete](docs/sdks/consumers/README.md#delete) - Delete consumer

#### [vault.create_callback](docs/sdks/createcallback/README.md)

* [state](docs/sdks/createcallback/README.md#state) - Create Callback State

#### [vault.custom_fields](docs/sdks/customfields/README.md)

* [list](docs/sdks/customfields/README.md#list) - Get resource custom fields

#### [vault.custom_mappings](docs/sdks/custommappings/README.md)

* [list](docs/sdks/custommappings/README.md#list) - List custom mappings

#### [vault.logs](docs/sdks/logs/README.md)

* [list](docs/sdks/logs/README.md#list) - Get all consumer request logs

#### [vault.sessions](docs/sdks/sessions/README.md)

* [create](docs/sdks/sessions/README.md#create) - Create Session

#### [vault.validate_connection](docs/sdks/validateconnection/README.md)

* [state](docs/sdks/validateconnection/README.md#state) - Validate Connection State

### [webhook](docs/sdks/webhooksdk/README.md)


#### [webhook.event_logs](docs/sdks/eventlogs/README.md)

* [list](docs/sdks/eventlogs/README.md#list) - List event logs

#### [webhook.webhooks](docs/sdks/webhooks/README.md)

* [list](docs/sdks/webhooks/README.md#list) - List webhook subscriptions
* [create](docs/sdks/webhooks/README.md#create) - Create webhook subscription
* [get](docs/sdks/webhooks/README.md#get) - Get webhook subscription
* [update](docs/sdks/webhooks/README.md#update) - Update webhook subscription
* [delete](docs/sdks/webhooks/README.md#delete) - Delete webhook subscription

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.attachments.upload(reference_type=apideck_unify.AttachmentReferenceType.INVOICE, reference_id="123456", request_body=open("example.file", "rb"), raw=False, x_apideck_metadata="{\"name\":\"document.pdf\",\"description\":\"Invoice attachment\"}", service_id="salesforce")

    assert res.create_attachment_response is not None

    # Handle response
    print(res.create_attachment_response)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from apideck_unify import Apideck
from apideck_unify.utils import BackoffStrategy, RetryConfig
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    while res is not None:
        # Handle items

        res = res.next()

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from apideck_unify import Apideck
from apideck_unify.utils import BackoffStrategy, RetryConfig
import os


with Apideck(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ApideckError`](./src/apideck_unify/models/apideckerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import apideck_unify
from apideck_unify import Apideck, models
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:
    res = None
    try:

        res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
            "assets": True,
            "equity": True,
            "expenses": True,
            "liabilities": True,
            "revenue": True,
        }, pass_through={
            "search": "San Francisco",
        }, fields="id,updated_at")

        while res is not None:
            # Handle items

            res = res.next()


    except models.ApideckError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.BadRequestResponse):
            print(e.data.status_code)  # Optional[float]
            print(e.data.error)  # Optional[str]
            print(e.data.type_name)  # Optional[str]
            print(e.data.message)  # Optional[str]
            print(e.data.detail)  # Optional[apideck_unify.BadRequestResponseDetail]
```

### Error Classes
**Primary errors:**
* [`ApideckError`](./src/apideck_unify/models/apideckerror.py): The base class for HTTP error responses.
  * [`UnauthorizedResponse`](./src/apideck_unify/models/unauthorizedresponse.py): Unauthorized. Status code `401`.
  * [`PaymentRequiredResponse`](./src/apideck_unify/models/paymentrequiredresponse.py): Payment Required. Status code `402`.
  * [`NotFoundResponse`](./src/apideck_unify/models/notfoundresponse.py): The specified resource was not found. Status code `404`. *
  * [`BadRequestResponse`](./src/apideck_unify/models/badrequestresponse.py): Bad Request. Status code `400`. *
  * [`UnprocessableResponse`](./src/apideck_unify/models/unprocessableresponse.py): Unprocessable. Status code `422`. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ApideckError`](./src/apideck_unify/models/apideckerror.py)**:
* [`ResponseValidationError`](./src/apideck_unify/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from apideck_unify import Apideck
import os


with Apideck(
    server_url="https://unify.apideck.com",
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.attachments.upload(reference_type=apideck_unify.AttachmentReferenceType.INVOICE, reference_id="123456", request_body=open("example.file", "rb"), raw=False, x_apideck_metadata="{\"name\":\"document.pdf\",\"description\":\"Invoice attachment\"}", service_id="salesforce", server_url="https://upload.apideck.com")

    assert res.create_attachment_response is not None

    # Handle response
    print(res.create_attachment_response)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from apideck_unify import Apideck
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Apideck(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from apideck_unify import Apideck
from apideck_unify.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Apideck(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Apideck` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from apideck_unify import Apideck
import os
def main():

    with Apideck(
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        api_key=os.getenv("APIDECK_API_KEY", ""),
    ) as apideck:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Apideck(
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
        api_key=os.getenv("APIDECK_API_KEY", ""),
    ) as apideck:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from apideck_unify import Apideck
import logging

logging.basicConfig(level=logging.DEBUG)
s = Apideck(debug_logger=logging.getLogger("apideck_unify"))
```

You can also enable a default debug logger by setting an environment variable `APIDECK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

There may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 