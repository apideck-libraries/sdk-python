# Employees
(*hris.employees*)

## Overview

### Available Operations

* [list](#list) - List Employees
* [create](#create) - Create Employee
* [get](#get) - Get Employee
* [update](#update) - Update Employee
* [delete](#delete) - Delete Employee

## list

Apideck operates as a stateless Unified API, which means that the list endpoint only provides a portion of the employee model. This is due to the fact that most HRIS systems do not readily provide all data in every call. However, you can access the complete employee model through an employee detail call.

### Example Usage

```python
import apideck
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.hris.employees.list(request={
        "service_id": "salesforce",
        "filter_": {
            "company_id": "1234",
            "email": "elon@tesla.com",
            "first_name": "Elon",
            "title": "Manager",
            "last_name": "Musk",
            "manager_id": "1234",
            "employment_status": apideck.EmployeesFilterEmploymentStatus.ACTIVE,
            "employee_number": "123456-AB",
            "department_id": "1234",
        },
        "sort": {
            "by": apideck.EmployeesSortBy.CREATED_AT,
            "direction": apideck.SortDirection.DESC,
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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.HrisEmployeesAllRequest](../../models/hrisemployeesallrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.HrisEmployeesAllResponse](../../models/hrisemployeesallresponse.md)**

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

Create Employee

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
    res = s.hris.employees.create(employee={
        "id": "12345",
        "first_name": "Elon",
        "last_name": "Musk",
        "middle_name": "D.",
        "display_name": "Technoking",
        "preferred_name": "Elon Musk",
        "initials": "EM",
        "salutation": "Mr",
        "title": "CEO",
        "marital_status": "married",
        "partner": {
            "first_name": "Elon",
            "last_name": "Musk",
            "middle_name": "D.",
            "gender": apideck.Gender.MALE,
            "initials": "EM",
            "birthday": dateutil.parser.parse("2000-08-12").date(),
            "deceased_on": dateutil.parser.parse("2000-08-12").date(),
        },
        "division": "Europe",
        "division_id": "12345",
        "department_id": "12345",
        "department_name": "12345",
        "team": {
            "id": "1234",
            "name": "Full Stack Engineers",
        },
        "company_id": "23456",
        "company_name": "SpaceX",
        "employment_start_date": "2021-10-26",
        "employment_end_date": "2028-10-26",
        "leaving_reason": apideck.LeavingReason.RESIGNED,
        "employee_number": "123456-AB",
        "employment_status": apideck.EmploymentStatus.ACTIVE,
        "ethnicity": "African American",
        "manager": {
            "id": "12345",
            "name": "Elon Musk",
            "first_name": "Elon",
            "last_name": "Musk",
            "email": "elon@musk.com",
            "employment_status": apideck.EmploymentStatus.ACTIVE,
        },
        "direct_reports": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "social_security_number": "123456789",
        "birthday": dateutil.parser.parse("2000-08-12").date(),
        "deceased_on": dateutil.parser.parse("2000-08-12").date(),
        "country_of_birth": "US",
        "description": "A description",
        "gender": apideck.Gender.MALE,
        "pronouns": "she,her",
        "preferred_language": "EN",
        "languages": [
            "EN",
        ],
        "nationalities": [
            "US",
        ],
        "photo_url": "https://unavatar.io/elon-musk",
        "timezone": "Europe/London",
        "source": "lever",
        "source_id": "12345",
        "record_url": "https://app.intercom.io/contacts/12345",
        "jobs": [
            {
                "title": "CEO",
                "role": "Sales",
                "start_date": dateutil.parser.parse("2020-08-12").date(),
                "end_date": dateutil.parser.parse("2020-08-12").date(),
                "compensation_rate": 72000,
                "currency": apideck.Currency.USD,
                "payment_unit": apideck.PaymentUnit.YEAR,
                "hired_at": dateutil.parser.parse("2020-08-12").date(),
                "is_primary": True,
                "is_manager": True,
                "status": apideck.EmployeeJobStatus.ACTIVE,
                "location": {
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
        ],
        "compensations": [
            {
                "rate": 50,
                "payment_unit": apideck.PaymentUnit.HOUR,
                "flsa_status": apideck.FlsaStatus.NONEXEMPT,
                "effective_date": "2021-06-11",
            },
        ],
        "works_remote": True,
        "addresses": [
            {
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
            {
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
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck.PhoneNumberType.PRIMARY,
            },
        ],
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck.EmailType.PRIMARY,
            },
        ],
        "custom_fields": [
            {
                "id": "2389328923893298",
                "name": "employee_level",
                "description": "Employee Level",
                "value": True,
            },
        ],
        "social_links": [
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
        ],
        "bank_accounts": [
            {
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
            {
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
            {
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
        ],
        "tax_code": "1111",
        "tax_id": "234-32-0000",
        "dietary_preference": "Veggie",
        "food_allergies": [
            "No allergies",
        ],
        "probation_period": {
            "start_date": dateutil.parser.parse("2021-10-01").date(),
            "end_date": dateutil.parser.parse("2021-11-28").date(),
        },
        "tags": [
            "New",
        ],
        "row_version": "1-12345",
        "deleted": True,
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
| `employee`                                                                                                                                    | [models.EmployeeInput](../../models/employeeinput.md)                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.HrisEmployeesAddResponse](../../models/hrisemployeesaddresponse.md)**

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

Get Employee

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.hris.employees.get(request={
        "id": "<id>",
        "service_id": "salesforce",
        "fields": "id,updated_at",
        "filter_": {
            "company_id": "1234",
        },
        "pass_through": {
            "search": "San Francisco",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.HrisEmployeesOneRequest](../../models/hrisemployeesonerequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.HrisEmployeesOneResponse](../../models/hrisemployeesoneresponse.md)**

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

Update Employee

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
    res = s.hris.employees.update(id="<id>", employee={
        "id": "12345",
        "first_name": "Elon",
        "last_name": "Musk",
        "middle_name": "D.",
        "display_name": "Technoking",
        "preferred_name": "Elon Musk",
        "initials": "EM",
        "salutation": "Mr",
        "title": "CEO",
        "marital_status": "married",
        "partner": {
            "first_name": "Elon",
            "last_name": "Musk",
            "middle_name": "D.",
            "gender": apideck.Gender.MALE,
            "initials": "EM",
            "birthday": dateutil.parser.parse("2000-08-12").date(),
            "deceased_on": dateutil.parser.parse("2000-08-12").date(),
        },
        "division": "Europe",
        "division_id": "12345",
        "department_id": "12345",
        "department_name": "12345",
        "team": {
            "id": "1234",
            "name": "Full Stack Engineers",
        },
        "company_id": "23456",
        "company_name": "SpaceX",
        "employment_start_date": "2021-10-26",
        "employment_end_date": "2028-10-26",
        "leaving_reason": apideck.LeavingReason.RESIGNED,
        "employee_number": "123456-AB",
        "employment_status": apideck.EmploymentStatus.ACTIVE,
        "ethnicity": "African American",
        "manager": {
            "id": "12345",
            "name": "Elon Musk",
            "first_name": "Elon",
            "last_name": "Musk",
            "email": "elon@musk.com",
            "employment_status": apideck.EmploymentStatus.ACTIVE,
        },
        "direct_reports": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "social_security_number": "123456789",
        "birthday": dateutil.parser.parse("2000-08-12").date(),
        "deceased_on": dateutil.parser.parse("2000-08-12").date(),
        "country_of_birth": "US",
        "description": "A description",
        "gender": apideck.Gender.MALE,
        "pronouns": "she,her",
        "preferred_language": "EN",
        "languages": [
            "EN",
        ],
        "nationalities": [
            "US",
        ],
        "photo_url": "https://unavatar.io/elon-musk",
        "timezone": "Europe/London",
        "source": "lever",
        "source_id": "12345",
        "record_url": "https://app.intercom.io/contacts/12345",
        "jobs": [
            {
                "title": "CEO",
                "role": "Sales",
                "start_date": dateutil.parser.parse("2020-08-12").date(),
                "end_date": dateutil.parser.parse("2020-08-12").date(),
                "compensation_rate": 72000,
                "currency": apideck.Currency.USD,
                "payment_unit": apideck.PaymentUnit.YEAR,
                "hired_at": dateutil.parser.parse("2020-08-12").date(),
                "is_primary": True,
                "is_manager": True,
                "status": apideck.EmployeeJobStatus.ACTIVE,
                "location": {
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
            {
                "title": "CEO",
                "role": "Sales",
                "start_date": dateutil.parser.parse("2020-08-12").date(),
                "end_date": dateutil.parser.parse("2020-08-12").date(),
                "compensation_rate": 72000,
                "currency": apideck.Currency.USD,
                "payment_unit": apideck.PaymentUnit.YEAR,
                "hired_at": dateutil.parser.parse("2020-08-12").date(),
                "is_primary": True,
                "is_manager": True,
                "status": apideck.EmployeeJobStatus.ACTIVE,
                "location": {
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
            {
                "title": "CEO",
                "role": "Sales",
                "start_date": dateutil.parser.parse("2020-08-12").date(),
                "end_date": dateutil.parser.parse("2020-08-12").date(),
                "compensation_rate": 72000,
                "currency": apideck.Currency.USD,
                "payment_unit": apideck.PaymentUnit.YEAR,
                "hired_at": dateutil.parser.parse("2020-08-12").date(),
                "is_primary": True,
                "is_manager": True,
                "status": apideck.EmployeeJobStatus.ACTIVE,
                "location": {
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
        ],
        "compensations": [
            {
                "rate": 50,
                "payment_unit": apideck.PaymentUnit.HOUR,
                "flsa_status": apideck.FlsaStatus.NONEXEMPT,
                "effective_date": "2021-06-11",
            },
        ],
        "works_remote": True,
        "addresses": [
            {
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
            {
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
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck.PhoneNumberType.PRIMARY,
            },
        ],
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck.EmailType.PRIMARY,
            },
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck.EmailType.PRIMARY,
            },
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck.EmailType.PRIMARY,
            },
        ],
        "custom_fields": [
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
        ],
        "social_links": [
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
        ],
        "bank_accounts": [
            {
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
        ],
        "tax_code": "1111",
        "tax_id": "234-32-0000",
        "dietary_preference": "Veggie",
        "food_allergies": [
            "No allergies",
        ],
        "probation_period": {
            "start_date": dateutil.parser.parse("2021-10-01").date(),
            "end_date": dateutil.parser.parse("2021-11-28").date(),
        },
        "tags": [
            "New",
        ],
        "row_version": "1-12345",
        "deleted": True,
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
| `id`                                                                                                                                          | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | ID of the record you are acting upon.                                                                                                         |                                                                                                                                               |
| `employee`                                                                                                                                    | [models.EmployeeInput](../../models/employeeinput.md)                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.HrisEmployeesUpdateResponse](../../models/hrisemployeesupdateresponse.md)**

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

Delete Employee

### Example Usage

```python
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.hris.employees.delete(id="<id>", service_id="salesforce")

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

**[models.HrisEmployeesDeleteResponse](../../models/hrisemployeesdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |