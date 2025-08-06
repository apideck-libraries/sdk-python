# CreateCallback
(*vault.create_callback*)

## Overview

### Available Operations

* [state](#state) - Create Callback State

## state

This endpoint creates a callback state that can be used to issue requests to the callback endpoint.


### Example Usage

<!-- UsageSnippet language="python" operationID="vault.createCallbackState" method="post" path="/vault/connections/{unified_api}/{service_id}/callback-state" -->
```python
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.vault.create_callback.state(service_id="pipedrive", unified_api="crm", redirect_uri="https://example.com/callback")

    assert res.create_callback_state_response is not None

    # Handle response
    print(res.create_callback_state_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service ID of the resource to return                                | pipedrive                                                           |
| `unified_api`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Unified API                                                         | crm                                                                 |
| `consumer_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | ID of the consumer which you want to get or push data from          | test-consumer                                                       |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `redirect_uri`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The redirect URI to be used after the connection is created.        | https://example.com/callback                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultCreateCallbackStateResponse](../../models/vaultcreatecallbackstateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |