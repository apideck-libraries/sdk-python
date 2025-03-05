# APIResourceCoverageSDK
(*connector.api_resource_coverage*)

## Overview

### Available Operations

* [get](#get) - Get API Resource Coverage

## get

Get API Resource Coverage

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.connector.api_resource_coverage.get(id="<id>", resource_id="<id>", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_api_resource_coverage_response is not None

    # Handle response
    print(res.get_api_resource_coverage_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the record you are acting upon.                               |                                                                     |
| `resource_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the resource you are acting upon.                             |                                                                     |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ConnectorAPIResourceCoverageOneResponse](../../models/connectorapiresourcecoverageoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |