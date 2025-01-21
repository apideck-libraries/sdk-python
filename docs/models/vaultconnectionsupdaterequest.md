# VaultConnectionsUpdateRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `service_id`                                               | *str*                                                      | :heavy_check_mark:                                         | Service ID of the resource to return                       | pipedrive                                                  |
| `unified_api`                                              | *str*                                                      | :heavy_check_mark:                                         | Unified API                                                | crm                                                        |
| `connection`                                               | [models.ConnectionInput](../models/connectioninput.md)     | :heavy_check_mark:                                         | Fields that need to be updated on the resource             |                                                            |
| `consumer_id`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | ID of the consumer which you want to get or push data from | test-consumer                                              |
| `app_id`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | The ID of your Unify application                           | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                    |