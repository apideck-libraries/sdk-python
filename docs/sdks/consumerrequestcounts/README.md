# ConsumerRequestCounts
(*vault.consumer_request_counts*)

## Overview

### Available Operations

* [list](#list) - Consumer request counts

## list

Get consumer request counts within a given datetime range.


### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.vault.consumer_request_counts.list(consumer_id="test_user_id", start_datetime="2021-05-01T12:00:00.000Z", end_datetime="2021-05-30T12:00:00.000Z")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `consumer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the consumer to return                                        | test_user_id                                                        |
| `start_datetime`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Scopes results to requests that happened after datetime             | 2021-05-01T12:00:00.000Z                                            |
| `end_datetime`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Scopes results to requests that happened before datetime            | 2021-05-30T12:00:00.000Z                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VaultConsumerRequestCountsAllResponse](../../models/vaultconsumerrequestcountsallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |