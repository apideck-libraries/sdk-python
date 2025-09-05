# ConnectionConsent
(*vault.connection_consent*)

## Overview

### Available Operations

* [update](#update) - Update consent state

## update

Update the consent state of a connection

### Example Usage

<!-- UsageSnippet language="python" operationID="vault.connectionConsentUpdate" method="patch" path="/vault/connections/{unified_api}/{service_id}/consent" -->
```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.vault.connection_consent.update(service_id="pipedrive", unified_api="crm", resources=apideck_unify.Two.WILDCARD_, granted=True)

    assert res.update_consent_response is not None

    # Handle response
    print(res.update_consent_response)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `service_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | Service ID of the resource to return                                                  | pipedrive                                                                             |
| `unified_api`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Unified API                                                                           | crm                                                                                   |
| `resources`                                                                           | [models.UpdateConsentRequestResources](../../models/updateconsentrequestresources.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |                                                                                       |
| `granted`                                                                             | *bool*                                                                                | :heavy_check_mark:                                                                    | Whether consent is being granted (true) or denied/revoked (false)                     | true                                                                                  |
| `consumer_id`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | ID of the consumer which you want to get or push data from                            | test-consumer                                                                         |
| `app_id`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | The ID of your Unify application                                                      | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                               |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.VaultConnectionConsentUpdateResponse](../../models/vaultconnectionconsentupdateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |