# VaultConnectionsUpdateRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `service_id`                                           | *str*                                                  | :heavy_check_mark:                                     | Service ID of the resource to return                   | pipedrive                                              |
| `unified_api`                                          | *str*                                                  | :heavy_check_mark:                                     | Unified API                                            | crm                                                    |
| `connection`                                           | [models.ConnectionInput](../models/connectioninput.md) | :heavy_check_mark:                                     | Fields that need to be updated on the resource         |                                                        |