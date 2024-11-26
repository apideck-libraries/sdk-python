# VirtualWebhooks

Virtual webhook config for the connector.


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request_rate`                                                                    | [models.RequestRate](../models/requestrate.md)                                    | :heavy_check_mark:                                                                | The rate at which requests for resources will be made to downstream.              |
| `resources`                                                                       | Dict[str, [models.WebhookSupportResources](../models/webhooksupportresources.md)] | :heavy_minus_sign:                                                                | The resources that will be requested from downstream.                             |