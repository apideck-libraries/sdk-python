# ConnectorDocs
(*connector.connector_docs*)

## Overview

### Available Operations

* [get](#get) - Get Connector Doc content

## get

Get Connector Doc content

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.connector.connector_docs.get(id="<id>", doc_id="application_owner+oauth_credentials")

    assert res.get_connector_doc_response is not None

    # Handle response
    print(res.get_connector_doc_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | ID of the record you are acting upon.                               |                                                                     |
| `doc_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | ID of the Doc                                                       | application_owner+oauth_credentials                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ConnectorConnectorDocsOneResponse](../../models/connectorconnectordocsoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |