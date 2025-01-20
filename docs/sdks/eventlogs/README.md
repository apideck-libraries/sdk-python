# EventLogs
(*webhook.event_logs*)

## Overview

### Available Operations

* [list](#list) - List event logs

## list

List event logs

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.webhook.event_logs.list(limit=20, filter_={
        "exclude_apis": "vault,proxy",
        "consumer_id": "test_user_id",
        "entity_type": "Connection",
        "event_type": "vault.connection.callable",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                         | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | Number of results to return. Minimum 1, Maximum 200, Default 20                                                  |
| `filter_`                                                                                                        | [Optional[models.WebhookEventLogsFilter]](../../models/webhookeventlogsfilter.md)                                | :heavy_minus_sign:                                                                                               | Filter results                                                                                                   |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[models.WebhookEventLogsAllResponse](../../models/webhookeventlogsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |