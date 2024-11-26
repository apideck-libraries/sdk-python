# ConnectorResources
(*connector.connector_resources*)

## Overview

### Available Operations

* [get](#get) - Get Connector Resource

## get

Get Connector Resource

### Example Usage

```python
import apideck
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.connector.connector_resources.get(id="<id>", resource_id="<id>", unified_api=apideck.UnifiedAPIID.CRM)

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | ID of the record you are acting upon.                                                                   |                                                                                                         |
| `resource_id`                                                                                           | *str*                                                                                                   | :heavy_check_mark:                                                                                      | ID of the resource you are acting upon.                                                                 |                                                                                                         |
| `unified_api`                                                                                           | [Optional[models.UnifiedAPIID]](../../models/unifiedapiid.md)                                           | :heavy_minus_sign:                                                                                      | Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs | crm                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.ConnectorConnectorResourcesOneResponse](../../models/connectorconnectorresourcesoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |