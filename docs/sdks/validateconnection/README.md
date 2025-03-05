# ValidateConnection
(*vault.validate_connection*)

## Overview

### Available Operations

* [state](#state) - Validate Connection State

## state

This endpoint validates the current state of a given connection. This will perform different checks based on the connection auth type. For basic and apiKey auth types, the presence of required fields is checked.
For connectors that implement OAuth2, this operation forces the refresh flow for an access token regardless of its expiry.

Note:
  - Do not include any credentials in the request body. This operation does not persist changes, but only triggers the validation of connection state.
  - If a refresh token flow was performed and successful, the new access token will then be used for subsequent API requests.


### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.validate_connection.state(service_id="pipedrive", unified_api="crm", consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.validate_connection_state_response is not None

    # Handle response
    print(res.validate_connection_state_response)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         | Example                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                        | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Service ID of the resource to return                                                                                | pipedrive                                                                                                           |
| `unified_api`                                                                                                       | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Unified API                                                                                                         | crm                                                                                                                 |
| `consumer_id`                                                                                                       | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | ID of the consumer which you want to get or push data from                                                          | test-consumer                                                                                                       |
| `app_id`                                                                                                            | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | The ID of your Unify application                                                                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                             |
| `request_body`                                                                                                      | [Optional[models.VaultValidateConnectionStateRequestBody]](../../models/vaultvalidateconnectionstaterequestbody.md) | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |                                                                                                                     |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |                                                                                                                     |

### Response

**[models.VaultValidateConnectionStateResponse](../../models/vaultvalidateconnectionstateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |