# Logs
(*vault.logs*)

## Overview

### Available Operations

* [list](#list) - Get all consumer request logs

## list

This endpoint includes all consumer request logs.


### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.vault.logs.list(filter_={
        "connector_id": "crm+salesforce",
        "status_code": 201,
        "exclude_unified_apis": "vault,proxy",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                        | [Optional[models.LogsFilter]](../../models/logsfilter.md)                                                        | :heavy_minus_sign:                                                                                               | Filter results                                                                                                   |
| `cursor`                                                                                                         | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | Number of results to return. Minimum 1, Maximum 200, Default 20                                                  |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[models.VaultLogsAllResponse](../../models/vaultlogsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |