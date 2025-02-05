# Webhooks
(*webhook.webhooks*)

## Overview

### Available Operations

* [list](#list) - List webhook subscriptions
* [create](#create) - Create webhook subscription
* [get](#get) - Get webhook subscription
* [update](#update) - Update webhook subscription
* [delete](#delete) - Delete webhook subscription

## list

List all webhook subscriptions

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.webhook.webhooks.list(app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

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
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |                                                                                                                  |

### Response

**[models.WebhookWebhooksAllResponse](../../models/webhookwebhooksallresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## create

Create a webhook subscription to receive events

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

    res = apideck.webhook.webhooks.create(unified_api=apideck_unify.UnifiedAPIID.CRM, status=apideck_unify.Status.ENABLED, delivery_url="https://example.com/my/webhook/endpoint", events=[
        apideck_unify.WebhookEventType.VAULT_CONNECTION_CREATED,
        apideck_unify.WebhookEventType.VAULT_CONNECTION_UPDATED,
    ], app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", description="A description")

    assert res.create_webhook_response is not None

    # Handle response
    print(res.create_webhook_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  | Example                                                                                      |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `unified_api`                                                                                | [models.UnifiedAPIID](../../models/unifiedapiid.md)                                          | :heavy_check_mark:                                                                           | Name of Apideck Unified API                                                                  | crm                                                                                          |
| `status`                                                                                     | [models.Status](../../models/status.md)                                                      | :heavy_check_mark:                                                                           | The status of the webhook.                                                                   | enabled                                                                                      |
| `delivery_url`                                                                               | *str*                                                                                        | :heavy_check_mark:                                                                           | The delivery url of the webhook endpoint.                                                    | https://example.com/my/webhook/endpoint                                                      |
| `events`                                                                                     | List[[models.WebhookEventType](../../models/webhookeventtype.md)]                            | :heavy_check_mark:                                                                           | The list of subscribed events for this webhook. [`*`] indicates that all events are enabled. | [<br/>"vault.connection.created",<br/>"vault.connection.updated"<br/>]                       |
| `app_id`                                                                                     | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | The ID of your Unify application                                                             | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                      |
| `description`                                                                                | *OptionalNullable[str]*                                                                      | :heavy_minus_sign:                                                                           | A description of the object.                                                                 | A description                                                                                |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |                                                                                              |

### Response

**[models.WebhookWebhooksAddResponse](../../models/webhookwebhooksaddresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## get

Get the webhook subscription details

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.webhook.webhooks.get(id="<id>", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.get_webhook_response is not None

    # Handle response
    print(res.get_webhook_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |                                                                                                    |
| `app_id`                                                                                           | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The ID of your Unify application                                                                   | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                            |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.WebhookWebhooksOneResponse](../../models/webhookwebhooksoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## update

Update a webhook subscription

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

    res = apideck.webhook.webhooks.update(id="<id>", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", description="A description", status=apideck_unify.Status.ENABLED, delivery_url="https://example.com/my/webhook/endpoint", events=[
        apideck_unify.WebhookEventType.VAULT_CONNECTION_CREATED,
        apideck_unify.WebhookEventType.VAULT_CONNECTION_UPDATED,
    ])

    assert res.update_webhook_response is not None

    # Handle response
    print(res.update_webhook_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |                                                                                                    |
| `app_id`                                                                                           | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The ID of your Unify application                                                                   | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                            |
| `description`                                                                                      | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | A description of the object.                                                                       | A description                                                                                      |
| `status`                                                                                           | [Optional[models.Status]](../../models/status.md)                                                  | :heavy_minus_sign:                                                                                 | The status of the webhook.                                                                         | enabled                                                                                            |
| `delivery_url`                                                                                     | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The delivery url of the webhook endpoint.                                                          | https://example.com/my/webhook/endpoint                                                            |
| `events`                                                                                           | List[[models.WebhookEventType](../../models/webhookeventtype.md)]                                  | :heavy_minus_sign:                                                                                 | The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.       | [<br/>"vault.connection.created",<br/>"vault.connection.updated"<br/>]                             |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.WebhookWebhooksUpdateResponse](../../models/webhookwebhooksupdateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## delete

Delete a webhook subscription

### Example Usage

```python
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.webhook.webhooks.delete(id="<id>", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX")

    assert res.delete_webhook_response is not None

    # Handle response
    print(res.delete_webhook_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. |                                                                                                    |
| `app_id`                                                                                           | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The ID of your Unify application                                                                   | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                            |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.WebhookWebhooksDeleteResponse](../../models/webhookwebhooksdeleteresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |