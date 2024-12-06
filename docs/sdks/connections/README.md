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
) as s:
    res = s.vault.connections.list(api="crm", configured=True)

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
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
) as s:
    res = s.vault.connections.get(service_id="pipedrive", unified_api="crm")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
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
) as s:
    res = s.vault.connections.update(service_id="pipedrive", unified_api="crm", connection={
        "enabled": True,
        "settings": {
            "instance_url": "https://eu28.salesforce.com",
            "api_key": "12345xxxxxx",
        },
        "metadata": {
            "account": {
                "name": "My Company",
                "id": "c01458a5-7276-41ce-bc19-639906b0450a",
            },
            "plan": "enterprise",
        },
        "configuration": [
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
                        ],
                        "value": "GC5000 series",
                    },
                    {
                        "id": "ProductInterest",
                        "options": [
                            {
                                "label": "General Channel",
                                "value": 123,
                            },
                            {
                                "label": "General Channel",
                                "value": "general",
                            },
                            {
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 123,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                    {
                                        "label": "General Channel",
                                        "value": True,
                                    },
                                ],
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
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 12.5,
                                    },
                                ],
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
                                "id": "1234",
                                "label": "General Channel",
                                "options": [
                                    {
                                        "label": "General Channel",
                                        "value": 123,
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
                                        "value": "general",
                                    },
                                ],
                            },
                            {
                                "label": "General Channel",
                                "value": 123,
                            },
                        ],
                        "value": True,
                    },
                ],
            },
        ],
        "custom_mappings": [
            {
                "value": "$.root.training.first_aid",
            },
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `connection`                                                        | [models.ConnectionInput](../../models/connectioninput.md)           | :heavy_check_mark:                                                  | Fields that need to be updated on the resource                      |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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
) as s:
    res = s.vault.connections.delete(service_id="pipedrive", unified_api="crm")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnexpectedErrorResponse](../../models/unexpectederrorresponse.md)**

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
) as s:
    res = s.vault.connections.imports(service_id="pipedrive", unified_api="crm", connection_import_data={
        "credentials": {
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ",
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
        },
        "metadata": {
            "account": {
                "name": "My Company",
                "id": "c01458a5-7276-41ce-bc19-639906b0450a",
            },
            "plan": "enterprise",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `connection_import_data`                                            | [models.ConnectionImportData](../../models/connectionimportdata.md) | :heavy_check_mark:                                                  | Fields that need to be persisted on the resource                    |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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
) as s:
    res = s.vault.connections.token(service_id="pipedrive", unified_api="crm")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Service ID of the resource to return                                                                  | pipedrive                                                                                             |
| `unified_api`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Unified API                                                                                           | crm                                                                                                   |
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