# Applicants
(*ats.applicants*)

## Overview

### Available Operations

* [list](#list) - List Applicants
* [create](#create) - Create Applicant
* [get](#get) - Get Applicant
* [update](#update) - Update Applicant
* [delete](#delete) - Delete Applicant

## list

List Applicants

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:
    res = apideck.ats.applicants.list(request={
        "service_id": "salesforce",
        "filter_": {
            "job_id": "1234",
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
| `request`                                                                 | [models.AtsApplicantsAllRequest](../../models/atsapplicantsallrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.AtsApplicantsAllResponse](../../models/atsapplicantsallresponse.md)**

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

Create Applicant

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
    res = apideck.ats.applicants.create(applicant={
        "name": "Elon Musk",
        "first_name": "Elon",
        "last_name": "Musk",
        "middle_name": "D.",
        "initials": "EM",
        "birthday": dateutil.parser.parse("2000-08-12").date(),
        "cover_letter": "I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...",
        "photo_url": "https://unavatar.io/elon-musk",
        "headline": "PepsiCo, Inc, Central Perk",
        "title": "CEO",
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_unify.EmailType.PRIMARY,
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
                "value": "Uses Salesforce and Marketo",
            },
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_unify.PhoneNumberType.PRIMARY,
            },
        ],
        "addresses": [
            {
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
            {
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
            {
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
        ],
        "websites": [
            {
                "url": "http://example.com",
                "id": "12345",
                "type": apideck_unify.ApplicantType.PRIMARY,
            },
            {
                "url": "http://example.com",
                "id": "12345",
                "type": apideck_unify.ApplicantType.PRIMARY,
            },
            {
                "url": "http://example.com",
                "id": "12345",
                "type": apideck_unify.ApplicantType.PRIMARY,
            },
        ],
        "social_links": [
            {
                "url": "https://www.twitter.com/apideck",
                "id": "12345",
                "type": "twitter",
            },
        ],
        "stage_id": "12345",
        "recruiter_id": "12345",
        "coordinator_id": "12345",
        "application_ids": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "applications": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "followers": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "sources": [
            "Job site",
        ],
        "confidential": False,
        "anonymized": True,
        "tags": [
            "New",
        ],
        "archived": False,
        "owner_id": "54321",
        "record_url": "https://app.intercom.io/contacts/12345",
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
| `applicant`                                                                                                                                   | [models.ApplicantInput](../../models/applicantinput.md)                                                                                       | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AtsApplicantsAddResponse](../../models/atsapplicantsaddresponse.md)**

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

Get Applicant

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:
    res = apideck.ats.applicants.get(id="<id>", service_id="salesforce", fields="id,updated_at")

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

**[models.AtsApplicantsOneResponse](../../models/atsapplicantsoneresponse.md)**

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

Update Applicant

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
    res = apideck.ats.applicants.update(id="<id>", applicant={
        "name": "Elon Musk",
        "first_name": "Elon",
        "last_name": "Musk",
        "middle_name": "D.",
        "initials": "EM",
        "birthday": dateutil.parser.parse("2000-08-12").date(),
        "cover_letter": "I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...",
        "photo_url": "https://unavatar.io/elon-musk",
        "headline": "PepsiCo, Inc, Central Perk",
        "title": "CEO",
        "emails": [
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_unify.EmailType.PRIMARY,
            },
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_unify.EmailType.PRIMARY,
            },
            {
                "email": "elon@musk.com",
                "id": "123",
                "type": apideck_unify.EmailType.PRIMARY,
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
            },
        ],
        "phone_numbers": [
            {
                "number": "111-111-1111",
                "id": "12345",
                "country_code": "1",
                "area_code": "323",
                "extension": "105",
                "type": apideck_unify.PhoneNumberType.PRIMARY,
            },
        ],
        "addresses": [
            {
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
            {
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
            {
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
        ],
        "websites": [
            {
                "url": "http://example.com",
                "id": "12345",
                "type": apideck_unify.ApplicantType.PRIMARY,
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
        "stage_id": "12345",
        "recruiter_id": "12345",
        "coordinator_id": "12345",
        "application_ids": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "applications": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "followers": [
            "a0d636c6-43b3-4bde-8c70-85b707d992f4",
            "a98lfd96-43b3-4bde-8c70-85b707d992e6",
        ],
        "sources": [
            "Job site",
        ],
        "confidential": False,
        "anonymized": True,
        "tags": [
            "New",
        ],
        "archived": False,
        "owner_id": "54321",
        "record_url": "https://app.intercom.io/contacts/12345",
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
| `applicant`                                                                                                                                   | [models.ApplicantInput](../../models/applicantinput.md)                                                                                       | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |                                                                                                                                               |
| `service_id`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | salesforce                                                                                                                                    |
| `raw`                                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Include raw response. Mostly used for debugging purposes                                                                                      |                                                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.AtsApplicantsUpdateResponse](../../models/atsapplicantsupdateresponse.md)**

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

Delete Applicant

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:
    res = apideck.ats.applicants.delete(id="<id>", service_id="salesforce")

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

**[models.AtsApplicantsDeleteResponse](../../models/atsapplicantsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |