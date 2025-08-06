# ConnectorResources
(*connector.connector_resources*)

## Overview

### Available Operations

* [get](#get) - Get Connector Resource

## get

Get Connector Resource

### Example Usage

<!-- UsageSnippet language="python" operationID="connector.connectorResourcesOne" method="get" path="/connector/connectors/{id}/resources/{resource_id}" -->
```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.connector.connector_resources.get(id="<id>", resource_id="<id>", unified_api=apideck_unify.UnifiedAPIID.CRM)

    assert res.get_connector_resource_response is not None

    # Handle response
    print(res.get_connector_resource_response)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | ID of the record you are acting upon.                                                                   |                                                                                                         |
| `resource_id`                                                                                           | *str*                                                                                                   | :heavy_check_mark:                                                                                      | ID of the resource you are acting upon.                                                                 |                                                                                                         |
| `app_id`                                                                                                | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | The ID of your Unify application                                                                        | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                 |
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