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
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.ats.applicants.list(raw=False, service_id="salesforce", limit=20, filter_={
        "job_id": "1234",
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
| `filter_`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[models.ApplicantsFilter]](../../models/applicantsfilter.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Apply filters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {<br/>"job_id": "1234"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `pass_through`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {<br/>"search": "San Francisco"<br/>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `fields`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded. | id,updated_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

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
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.ats.applicants.create(raw=False, service_id="salesforce", name="Elon Musk", first_name="Elon", last_name="Musk", middle_name="D.", initials="EM", birthday=date.fromisoformat("2000-08-12"), cover_letter="I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...", photo_url="https://unavatar.io/elon-musk", headline="PepsiCo, Inc, Central Perk", title="CEO", emails=[
        {
            "id": "123",
            "email": "elon@musk.com",
            "type": apideck_unify.EmailType.PRIMARY,
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
    ], phone_numbers=[
        {
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "number": "111-111-1111",
            "extension": "105",
            "type": apideck_unify.PhoneNumberType.PRIMARY,
        },
        {
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "number": "111-111-1111",
            "extension": "105",
            "type": apideck_unify.PhoneNumberType.PRIMARY,
        },
    ], addresses=[
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
    ], websites=[
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
    ], social_links=[
        {
            "id": "12345",
            "url": "https://www.twitter.com/apideck",
            "type": "twitter",
        },
        {
            "id": "12345",
            "url": "https://www.twitter.com/apideck",
            "type": "twitter",
        },
    ], stage_id="12345", recruiter_id="12345", coordinator_id="12345", application_ids=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], applications=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], followers=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], sources=[
        "Job site",
    ], confidential=False, anonymized=True, tags=[
        "New",
    ], archived=False, owner_id="54321", record_url="https://app.intercom.io/contacts/12345", deleted=True, pass_through=[
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

    assert res.create_applicant_response is not None

    # Handle response
    print(res.create_applicant_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `name`                                                                                                                                                  | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The name of an applicant.                                                                                                                               | Elon Musk                                                                                                                                               |
| `first_name`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The first name of the person.                                                                                                                           | Elon                                                                                                                                                    |
| `last_name`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The last name of the person.                                                                                                                            | Musk                                                                                                                                                    |
| `middle_name`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Middle name of the person.                                                                                                                              | D.                                                                                                                                                      |
| `initials`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The initials of the person, usually derived from their first, middle, and last names.                                                                   | EM                                                                                                                                                      |
| `birthday`                                                                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date of birth of the person.                                                                                                                        | 2000-08-12                                                                                                                                              |
| `cover_letter`                                                                                                                                          | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...  |
| `photo_url`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The URL of the photo of a person.                                                                                                                       | https://unavatar.io/elon-musk                                                                                                                           |
| `headline`                                                                                                                                              | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Typically a list of previous companies where the contact has worked or schools that the contact has attended                                            | PepsiCo, Inc, Central Perk                                                                                                                              |
| `title`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The job title of the person.                                                                                                                            | CEO                                                                                                                                                     |
| `emails`                                                                                                                                                | List[[models.Email](../../models/email.md)]                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `phone_numbers`                                                                                                                                         | List[[models.PhoneNumber](../../models/phonenumber.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `addresses`                                                                                                                                             | List[[models.Address](../../models/address.md)]                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `websites`                                                                                                                                              | List[[models.Websites](../../models/websites.md)]                                                                                                       | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `social_links`                                                                                                                                          | List[[models.SocialLinks](../../models/sociallinks.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `stage_id`                                                                                                                                              | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `recruiter_id`                                                                                                                                          | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `coordinator_id`                                                                                                                                        | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `application_ids`                                                                                                                                       | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `applications`                                                                                                                                          | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `followers`                                                                                                                                             | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `sources`                                                                                                                                               | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"Job site"<br/>]                                                                                                                                  |
| `confidential`                                                                                                                                          | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | false                                                                                                                                                   |
| `anonymized`                                                                                                                                            | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | true                                                                                                                                                    |
| `tags`                                                                                                                                                  | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"New"<br/>]                                                                                                                                       |
| `archived`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | false                                                                                                                                                   |
| `owner_id`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 54321                                                                                                                                                   |
| `record_url`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | https://app.intercom.io/contacts/12345                                                                                                                  |
| `deleted`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Flag to indicate if the object is deleted.                                                                                                              | true                                                                                                                                                    |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.ats.applicants.get(id="<id>", service_id="salesforce", raw=False, fields="id,updated_at")

    assert res.get_applicant_response is not None

    # Handle response
    print(res.get_applicant_response)

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
from datetime import date
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.ats.applicants.update(id="<id>", service_id="salesforce", raw=False, name="Elon Musk", first_name="Elon", last_name="Musk", middle_name="D.", initials="EM", birthday=date.fromisoformat("2000-08-12"), cover_letter="I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...", photo_url="https://unavatar.io/elon-musk", headline="PepsiCo, Inc, Central Perk", title="CEO", emails=[
        {
            "id": "123",
            "email": "elon@musk.com",
            "type": apideck_unify.EmailType.PRIMARY,
        },
        {
            "id": "123",
            "email": "elon@musk.com",
            "type": apideck_unify.EmailType.PRIMARY,
        },
        {
            "id": "123",
            "email": "elon@musk.com",
            "type": apideck_unify.EmailType.PRIMARY,
        },
    ], custom_fields=[
        {
            "id": "2389328923893298",
            "name": "employee_level",
            "description": "Employee Level",
            "value": {
                "0": {

                },
                "1": {

                },
            },
        },
    ], phone_numbers=[
        {
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "number": "111-111-1111",
            "extension": "105",
            "type": apideck_unify.PhoneNumberType.PRIMARY,
        },
        {
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "number": "111-111-1111",
            "extension": "105",
            "type": apideck_unify.PhoneNumberType.PRIMARY,
        },
        {
            "id": "12345",
            "country_code": "1",
            "area_code": "323",
            "number": "111-111-1111",
            "extension": "105",
            "type": apideck_unify.PhoneNumberType.PRIMARY,
        },
    ], addresses=[
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
    ], websites=[
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
        {
            "id": "12345",
            "url": "http://example.com",
            "type": apideck_unify.ApplicantType.PRIMARY,
        },
    ], social_links=[
        {
            "id": "12345",
            "url": "https://www.twitter.com/apideck",
            "type": "twitter",
        },
    ], stage_id="12345", recruiter_id="12345", coordinator_id="12345", application_ids=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], applications=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], followers=[
        "a0d636c6-43b3-4bde-8c70-85b707d992f4",
        "a98lfd96-43b3-4bde-8c70-85b707d992e6",
    ], sources=[
        "Job site",
    ], confidential=False, anonymized=True, tags=[
        "New",
    ], archived=False, owner_id="54321", record_url="https://app.intercom.io/contacts/12345", deleted=True, pass_through=[
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

    assert res.update_applicant_response is not None

    # Handle response
    print(res.update_applicant_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `name`                                                                                                                                                  | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The name of an applicant.                                                                                                                               | Elon Musk                                                                                                                                               |
| `first_name`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The first name of the person.                                                                                                                           | Elon                                                                                                                                                    |
| `last_name`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The last name of the person.                                                                                                                            | Musk                                                                                                                                                    |
| `middle_name`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Middle name of the person.                                                                                                                              | D.                                                                                                                                                      |
| `initials`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The initials of the person, usually derived from their first, middle, and last names.                                                                   | EM                                                                                                                                                      |
| `birthday`                                                                                                                                              | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                            | :heavy_minus_sign:                                                                                                                                      | The date of birth of the person.                                                                                                                        | 2000-08-12                                                                                                                                              |
| `cover_letter`                                                                                                                                          | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...  |
| `photo_url`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The URL of the photo of a person.                                                                                                                       | https://unavatar.io/elon-musk                                                                                                                           |
| `headline`                                                                                                                                              | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Typically a list of previous companies where the contact has worked or schools that the contact has attended                                            | PepsiCo, Inc, Central Perk                                                                                                                              |
| `title`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The job title of the person.                                                                                                                            | CEO                                                                                                                                                     |
| `emails`                                                                                                                                                | List[[models.Email](../../models/email.md)]                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `custom_fields`                                                                                                                                         | List[[models.CustomField](../../models/customfield.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `phone_numbers`                                                                                                                                         | List[[models.PhoneNumber](../../models/phonenumber.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `addresses`                                                                                                                                             | List[[models.Address](../../models/address.md)]                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `websites`                                                                                                                                              | List[[models.Websites](../../models/websites.md)]                                                                                                       | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `social_links`                                                                                                                                          | List[[models.SocialLinks](../../models/sociallinks.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     |                                                                                                                                                         |
| `stage_id`                                                                                                                                              | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `recruiter_id`                                                                                                                                          | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `coordinator_id`                                                                                                                                        | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 12345                                                                                                                                                   |
| `application_ids`                                                                                                                                       | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `applications`                                                                                                                                          | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `followers`                                                                                                                                             | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"a0d636c6-43b3-4bde-8c70-85b707d992f4",<br/>"a98lfd96-43b3-4bde-8c70-85b707d992e6"<br/>]                                                          |
| `sources`                                                                                                                                               | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"Job site"<br/>]                                                                                                                                  |
| `confidential`                                                                                                                                          | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | false                                                                                                                                                   |
| `anonymized`                                                                                                                                            | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | true                                                                                                                                                    |
| `tags`                                                                                                                                                  | List[*str*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | [<br/>"New"<br/>]                                                                                                                                       |
| `archived`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | false                                                                                                                                                   |
| `owner_id`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | 54321                                                                                                                                                   |
| `record_url`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | N/A                                                                                                                                                     | https://app.intercom.io/contacts/12345                                                                                                                  |
| `deleted`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Flag to indicate if the object is deleted.                                                                                                              | true                                                                                                                                                    |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

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
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.ats.applicants.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_applicant_response is not None

    # Handle response
    print(res.delete_applicant_response)

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