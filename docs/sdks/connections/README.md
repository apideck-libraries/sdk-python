# Connections
(*vault.connections*)

## Overview

### Available Operations

* [list](#list) - Get all connections
* [get](#get) - Get connection
* [update](#update) - Update connection
* [delete](#delete) - Deletes a connection
* [imports](#imports) - Import connection
* [token](#token) - Authorize Access Token

## list

This endpoint includes all the configured integrations and contains the required assets
to build an integrations page where your users can install integrations.
OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows.


### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.list(consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", api="crm", configured=True)

    assert res.get_connections_response is not None

    # Handle response
    print(res.get_connections_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `consumer_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the consumer which you want to get or push data from          | test-consumer                                                       |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `api`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Scope results to Unified API                                        | crm                                                                 |
| `configured`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Scopes results to connections that have been configured or not      | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConnectionsAllResponse](../../models/vaultconnectionsallresponse.md)**

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

Get a connection

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.get(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_connection_response is not None

    # Handle response
    print(res.get_connection_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `consumer_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the consumer which you want to get or push data from          | test-consumer                                                       |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConnectionsOneResponse](../../models/vaultconnectionsoneresponse.md)**

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

Update a connection

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.update(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", enabled=True, settings={
        "instance_url": "https://eu28.salesforce.com",
        "api_key": "12345xxxxxx",
    }, metadata={
        "account": {
            "name": "My Company",
            "id": "c01458a5-7276-41ce-bc19-639906b0450a",
        },
        "plan": "enterprise",
    }, configuration=[
        {
            "resource": "leads",
            "defaults": [
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "id": "1234",
                            "label": "General Channel",
                            "options": [
                                {
                                    "label": "General Channel",
                                    "value": 12.5,
                                },
                                {
                                    "label": "General Channel",
                                    "value": [
                                        "team",
                                        "general",
                                    ],
                                },
                            ],
                        },
                        {
                            "label": "General Channel",
                            "value": [
                                "team",
                                "general",
                            ],
                        },
                    ],
                    "value": 10.5,
                },
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "label": "General Channel",
                            "value": "general",
                        },
                    ],
                    "value": True,
                },
            ],
        },
        {
            "resource": "leads",
            "defaults": [
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "label": "General Channel",
                            "value": True,
                        },
                    ],
                    "value": True,
                },
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "label": "General Channel",
                            "value": True,
                        },
                        {
                            "id": "1234",
                            "label": "General Channel",
                            "options": [
                                {
                                    "label": "General Channel",
                                    "value": 12.5,
                                },
                                {
                                    "label": "General Channel",
                                    "value": "general",
                                },
                            ],
                        },
                    ],
                    "value": 10,
                },
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "id": "1234",
                            "label": "General Channel",
                            "options": [
                                {
                                    "label": "General Channel",
                                    "value": [
                                        "team",
                                        "general",
                                    ],
                                },
                                {
                                    "label": "General Channel",
                                    "value": True,
                                },
                                {
                                    "label": "General Channel",
                                    "value": 12.5,
                                },
                            ],
                        },
                        {
                            "label": "General Channel",
                            "value": 12.5,
                        },
                    ],
                    "value": 10.5,
                },
            ],
        },
        {
            "resource": "leads",
            "defaults": [
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "label": "General Channel",
                            "value": "general",
                        },
                        {
                            "label": "General Channel",
                            "value": True,
                        },
                        {
                            "label": "General Channel",
                            "value": True,
                        },
                    ],
                    "value": "GC5000 series",
                },
                {
                    "id": "ProductInterest",
                    "options": [
                        {
                            "label": "General Channel",
                            "value": True,
                        },
                        {
                            "label": "General Channel",
                            "value": 123,
                        },
                    ],
                    "value": 10.5,
                },
            ],
        },
    ], custom_mappings=[
        {
            "value": "$.root.training.first_aid",
        },
    ])

    assert res.update_connection_response is not None

    # Handle response
    print(res.update_connection_response)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                      | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Service ID of the resource to return                                                                              | pipedrive                                                                                                         |
| `unified_api`                                                                                                     | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Unified API                                                                                                       | crm                                                                                                               |
| `consumer_id`                                                                                                     | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | ID of the consumer which you want to get or push data from                                                        | test-consumer                                                                                                     |
| `app_id`                                                                                                          | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | The ID of your Unify application                                                                                  | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                           |
| `enabled`                                                                                                         | *Optional[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                | Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API. | true                                                                                                              |
| `settings`                                                                                                        | Dict[str, *Any*]                                                                                                  | :heavy_minus_sign:                                                                                                | Connection settings. Values will persist to `form_fields` with corresponding id                                   | {<br/>"instance_url": "https://eu28.salesforce.com",<br/>"api_key": "12345xxxxxx"<br/>}                           |
| `metadata`                                                                                                        | Dict[str, *Any*]                                                                                                  | :heavy_minus_sign:                                                                                                | Attach your own consumer specific metadata                                                                        | {<br/>"account": {<br/>"name": "My Company",<br/>"id": "c01458a5-7276-41ce-bc19-639906b0450a"<br/>},<br/>"plan": "enterprise"<br/>} |
| `configuration`                                                                                                   | List[[models.ConnectionConfiguration](../../models/connectionconfiguration.md)]                                   | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `custom_mappings`                                                                                                 | List[[models.CustomMappingInput](../../models/custommappinginput.md)]                                             | :heavy_minus_sign:                                                                                                | List of custom mappings configured for this connection                                                            |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.VaultConnectionsUpdateResponse](../../models/vaultconnectionsupdateresponse.md)**

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

Deletes a connection

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.delete(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `consumer_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the consumer which you want to get or push data from          | test-consumer                                                       |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConnectionsDeleteResponse](../../models/vaultconnectionsdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## imports

Import an authorized connection.


### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.imports(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", credentials={
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    }, settings={}, metadata={
        "account": {
            "name": "My Company",
            "id": "c01458a5-7276-41ce-bc19-639906b0450a",
        },
        "plan": "enterprise",
    })

    assert res.create_connection_response is not None

    # Handle response
    print(res.create_connection_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                | Service ID of the resource to return                                                                                                                                                                                                                                                                                                                              | pipedrive                                                                                                                                                                                                                                                                                                                                                         |
| `unified_api`                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                | Unified API                                                                                                                                                                                                                                                                                                                                                       | crm                                                                                                                                                                                                                                                                                                                                                               |
| `consumer_id`                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | ID of the consumer which you want to get or push data from                                                                                                                                                                                                                                                                                                        | test-consumer                                                                                                                                                                                                                                                                                                                                                     |
| `app_id`                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | The ID of your Unify application                                                                                                                                                                                                                                                                                                                                  | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                                                                                                                                                                                                                           |
| `credentials`                                                                                                                                                                                                                                                                                                                                                     | [Optional[models.Credentials]](../../models/credentials.md)                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                               | {<br/>"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",<br/>"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ"<br/>} |
| `settings`                                                                                                                                                                                                                                                                                                                                                        | [OptionalNullable[models.ConnectionImportDataSettings]](../../models/connectionimportdatasettings.md)                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | Connection settings. Values will persist to `form_fields` with corresponding id                                                                                                                                                                                                                                                                                   | {<br/>"instance_url": "https://eu28.salesforce.com"<br/>}                                                                                                                                                                                                                                                                                                         |
| `metadata`                                                                                                                                                                                                                                                                                                                                                        | Dict[str, *Any*]                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | Attach your own consumer specific metadata                                                                                                                                                                                                                                                                                                                        | {<br/>"account": {<br/>"name": "My Company",<br/>"id": "c01458a5-7276-41ce-bc19-639906b0450a"<br/>},<br/>"plan": "enterprise"<br/>}                                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.VaultConnectionsImportResponse](../../models/vaultconnectionsimportresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## token

Triggers exchanging persisted connection credentials for an access token and store it in Vault. Currently supported for connections with the `client_credentials` or `password` OAuth grant type.

Note:
  - Do not include any credentials in the request body. This operation does not persist changes, but only triggers the exchange of persisted connection credentials for an access token.
  - The access token will not be returned in the response. A 200 response code indicates the authorization was successful and that a valid access token was stored on the connection.
  - The access token will be used for subsequent API requests.


### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.connections.token(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_connection_response is not None

    # Handle response
    print(res.get_connection_response)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Service ID of the resource to return                                                                  | pipedrive                                                                                             |
| `unified_api`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Unified API                                                                                           | crm                                                                                                   |
| `consumer_id`                                                                                         | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | ID of the consumer which you want to get or push data from                                            | test-consumer                                                                                         |
| `app_id`                                                                                              | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | The ID of your Unify application                                                                      | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                               |
| `request_body`                                                                                        | [Optional[models.VaultConnectionsTokenRequestBody]](../../models/vaultconnectionstokenrequestbody.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.VaultConnectionsTokenResponse](../../models/vaultconnectionstokenresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |