# Proxy
(*proxy*)

## Overview

### Available Operations

* [get](#get) - GET
* [options](#options) - OPTIONS
* [post](#post) - POST
* [put](#put) - PUT
* [patch](#patch) - PATCH
* [delete](#delete) - DELETE

## get

Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.getProxy" method="get" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.get(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyGetProxyResponse](../../models/proxygetproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## options

Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.optionsProxy" method="options" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.options(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyOptionsProxyResponse](../../models/proxyoptionsproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## post

Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.postProxy" method="post" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.post(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `request_body`                                                                                                                                            | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                                                    | :heavy_minus_sign:                                                                                                                                        | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.                                                |                                                                                                                                                           |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyPostProxyResponse](../../models/proxypostproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## put

Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.putProxy" method="put" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.put(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `request_body`                                                                                                                                            | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                                                    | :heavy_minus_sign:                                                                                                                                        | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.                                                |                                                                                                                                                           |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyPutProxyResponse](../../models/proxyputproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## patch

Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.patchProxy" method="patch" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.patch(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `request_body`                                                                                                                                            | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                                                    | :heavy_minus_sign:                                                                                                                                        | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.                                                |                                                                                                                                                           |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyPatchProxyResponse](../../models/proxypatchproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## delete

Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.


### Example Usage

<!-- UsageSnippet language="python" operationID="proxy.deleteProxy" method="delete" path="/proxy" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.proxy.delete(service_id="close", downstream_url="https://api.close.com/api/v1/lead", unified_api="hris", downstream_authorization="Bearer <token>")

    assert res.response_json is not None

    # Handle response
    print(res.response_json)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                              | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.             | close                                                                                                                                                     |
| `downstream_url`                                                                                                                                          | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | Downstream URL                                                                                                                                            | https://api.close.com/api/v1/lead                                                                                                                         |
| `consumer_id`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | ID of the consumer which you want to get or push data from                                                                                                | test-consumer                                                                                                                                             |
| `app_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The ID of your Unify application                                                                                                                          | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                   |
| `unified_api`                                                                                                                                             | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Specify which unified API to use for the connection lookup. Required for multi-API connectors (e.g., Workday) to ensure the correct credentials are used. | hris                                                                                                                                                      |
| `downstream_authorization`                                                                                                                                | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | Downstream authorization header. This will skip the Vault token injection.                                                                                | Bearer <token>                                                                                                                                            |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |                                                                                                                                                           |

### Response

**[models.ProxyDeleteProxyResponse](../../models/proxydeleteproxyresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |