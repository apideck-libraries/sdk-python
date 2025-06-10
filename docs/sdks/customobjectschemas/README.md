# CustomObjectSchemas
(*crm.custom_object_schemas*)

## Overview

### Available Operations

* [list](#list) - List custom object schemas
* [create](#create) - Create custom object schema
* [get](#get) - Get custom object schema
* [update](#update) - Update custom object schema
* [delete](#delete) - Delete custom object schema

## list

List custom object schemas

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.crm.custom_object_schemas.list(raw=False, service_id="salesforce", limit=20, pass_through={
        "search": "San Francisco",
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
| `limit`                                                                                                                                           | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Number of results to return. Minimum 1, Maximum 200, Default 20                                                                                   |                                                                                                                                                   |
| `pass_through`                                                                                                                                    | Dict[str, *Any*]                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads | {<br/>"search": "San Francisco"<br/>}                                                                                                             |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[models.CrmCustomObjectSchemasAllResponse](../../models/crmcustomobjectschemasallresponse.md)**

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

Create custom object schema

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.crm.custom_object_schemas.create(raw=False, service_id="salesforce", name="project", description="This schema defines a project custom object", fields=[
        {
            "id": "field_123",
            "name": "project_name",
            "description": "Name of the project",
            "type": apideck_unify.CustomObjectSchemaType.STRING,
            "required": True,
            "options": [
                {
                    "value": "option1",
                    "label": "Option 1",
                },
            ],
            "default_value": "New Project",
        },
    ], visible=True, active=True, pass_through=[
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

    assert res.create_custom_object_schema_response is not None

    # Handle response
    print(res.create_custom_object_schema_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `name`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The name of the custom object schema                                                                                                                    | project                                                                                                                                                 |
| `description`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The description of the custom object schema                                                                                                             | This schema defines a project custom object                                                                                                             |
| `fields`                                                                                                                                                | List[[models.Fields](../../models/fields.md)]                                                                                                           | :heavy_minus_sign:                                                                                                                                      | The fields defined in the schema                                                                                                                        |                                                                                                                                                         |
| `visible`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Whether the custom object schema is visible in the UI                                                                                                   | true                                                                                                                                                    |
| `active`                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Whether the custom object schema is active                                                                                                              | true                                                                                                                                                    |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.CrmCustomObjectSchemasAddResponse](../../models/crmcustomobjectschemasaddresponse.md)**

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

Get custom object schema

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.crm.custom_object_schemas.get(id="<id>", service_id="salesforce", raw=False)

    assert res.get_custom_object_schema_response is not None

    # Handle response
    print(res.get_custom_object_schema_response)

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

**[models.CrmCustomObjectSchemasOneResponse](../../models/crmcustomobjectschemasoneresponse.md)**

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

Update custom object schema

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.crm.custom_object_schemas.update(id="<id>", service_id="salesforce", raw=False, name="project", description="This schema defines a project custom object", fields=[
        {
            "id": "field_123",
            "name": "project_name",
            "description": "Name of the project",
            "type": apideck_unify.CustomObjectSchemaType.STRING,
            "required": True,
            "options": [
                {
                    "value": "option1",
                    "label": "Option 1",
                },
                {
                    "value": "option1",
                    "label": "Option 1",
                },
            ],
            "default_value": "New Project",
        },
        {
            "id": "field_123",
            "name": "project_name",
            "description": "Name of the project",
            "type": apideck_unify.CustomObjectSchemaType.STRING,
            "required": True,
            "options": [
                {
                    "value": "option1",
                    "label": "Option 1",
                },
                {
                    "value": "option1",
                    "label": "Option 1",
                },
            ],
            "default_value": "New Project",
        },
        {
            "id": "field_123",
            "name": "project_name",
            "description": "Name of the project",
            "type": apideck_unify.CustomObjectSchemaType.STRING,
            "required": True,
            "options": [
                {
                    "value": "option1",
                    "label": "Option 1",
                },
                {
                    "value": "option1",
                    "label": "Option 1",
                },
            ],
            "default_value": "New Project",
        },
    ], visible=True, active=True, pass_through=[
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

    assert res.update_custom_object_schema_response is not None

    # Handle response
    print(res.update_custom_object_schema_response)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             | Example                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                    | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | ID of the record you are acting upon.                                                                                                                   |                                                                                                                                                         |
| `consumer_id`                                                                                                                                           | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | ID of the consumer which you want to get or push data from                                                                                              | test-consumer                                                                                                                                           |
| `app_id`                                                                                                                                                | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | The ID of your Unify application                                                                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                 |
| `service_id`                                                                                                                                            | *Optional[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                      | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.           | salesforce                                                                                                                                              |
| `raw`                                                                                                                                                   | *Optional[bool]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                      | Include raw response. Mostly used for debugging purposes                                                                                                |                                                                                                                                                         |
| `name`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The name of the custom object schema                                                                                                                    | project                                                                                                                                                 |
| `description`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | The description of the custom object schema                                                                                                             | This schema defines a project custom object                                                                                                             |
| `fields`                                                                                                                                                | List[[models.Fields](../../models/fields.md)]                                                                                                           | :heavy_minus_sign:                                                                                                                                      | The fields defined in the schema                                                                                                                        |                                                                                                                                                         |
| `visible`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Whether the custom object schema is visible in the UI                                                                                                   | true                                                                                                                                                    |
| `active`                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                                      | Whether the custom object schema is active                                                                                                              | true                                                                                                                                                    |
| `pass_through`                                                                                                                                          | List[[models.PassThroughBody](../../models/passthroughbody.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                      | The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources. |                                                                                                                                                         |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |                                                                                                                                                         |

### Response

**[models.CrmCustomObjectSchemasUpdateResponse](../../models/crmcustomobjectschemasupdateresponse.md)**

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

Delete custom object schema

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.crm.custom_object_schemas.delete(id="<id>", service_id="salesforce", raw=False)

    assert res.delete_custom_object_schema_response is not None

    # Handle response
    print(res.delete_custom_object_schema_response)

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

**[models.CrmCustomObjectSchemasDeleteResponse](../../models/crmcustomobjectschemasdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |