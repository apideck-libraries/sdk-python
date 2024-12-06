# WebhookSupport

How webhooks are supported for the connector. Sometimes the connector natively supports webhooks, other times Apideck virtualizes them based on polling.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `mode`                                                               | [Optional[models.Mode]](../models/mode.md)                           | :heavy_minus_sign:                                                   | Mode of the webhook support.                                         | native                                                               |
| `subscription_level`                                                 | [Optional[models.SubscriptionLevel]](../models/subscriptionlevel.md) | :heavy_minus_sign:                                                   | Received events are scoped to connection or across integration.      | integration                                                          |
| `managed_via`                                                        | [Optional[models.ManagedVia]](../models/managedvia.md)               | :heavy_minus_sign:                                                   | How the subscription is managed in the downstream.                   | api                                                                  |
| `virtual_webhooks`                                                   | [Optional[models.VirtualWebhooks]](../models/virtualwebhooks.md)     | :heavy_minus_sign:                                                   | Virtual webhook config for the connector.                            |                                                                      |