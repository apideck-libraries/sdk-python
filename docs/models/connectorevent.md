# ConnectorEvent

Unify event that is supported on the connector. Events are delivered via Webhooks.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `event_type`                                             | *Optional[str]*                                          | :heavy_minus_sign:                                       | Unify event type                                         | employee.created                                         |
| `event_source`                                           | [Optional[models.EventSource]](../models/eventsource.md) | :heavy_minus_sign:                                       | Unify event source                                       | native                                                   |
| `downstream_event_type`                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | Downstream event type                                    | person_created                                           |
| `resources`                                              | List[*str*]                                              | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `entity_type`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Unify entity type                                        | employee                                                 |