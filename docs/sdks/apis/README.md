# Apis
(*connector.apis*)

## Overview

### Available Operations

* [list](#list) - List APIs
* [get](#get) - Get API

## list

List APIs

### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.connector.apis.list(app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", filter_={
        "status": apideck_unify.APIStatus.BETA,
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `app_id`                                                                                                         | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | The ID of your Unify application                                                                                 | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                          |
| `cursor`                                                                                                         | *OptionalNullable[str]*                                                                                          | :heavy_minus_sign:                                                                                               | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. |                                                                                                                  |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | Number of results to return. Minimum 1, Maximum 200, Default 20                                                  |                                                                                                                  |
| `filter_`                                                                                                        | [Optional[models.ApisFilter]](../../models/apisfilter.md)                                                        | :heavy_minus_sign:                                                                                               | Apply filters                                                                                                    | {<br/>"status": "beta"<br/>}                                                                                     |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[models.ConnectorApisAllResponse](../../models/connectorapisallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## get

Get API

### Example Usage

```python
from apideck_unify import Apideck
import os


with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.connector.apis.get(id="<id>", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_api_response is not None

    # Handle response
    print(res.get_api_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the record you are acting upon.                               |                                                                     |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The ID of your Unify application                                    | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ConnectorApisOneResponse](../../models/connectorapisoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |