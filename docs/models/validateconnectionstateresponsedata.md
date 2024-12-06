# ValidateConnectionStateResponseData


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The unique identifier of the connection.                         | crm+salesforce                                                   |
| `state`                                                          | [Optional[models.ConnectionState]](../models/connectionstate.md) | :heavy_minus_sign:                                               | [Connection state flow](#section/Connection-state)               | authorized                                                       |