# VaultConsumerRequestCountsAllRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `consumer_id`                                            | *str*                                                    | :heavy_check_mark:                                       | ID of the consumer to return                             | test_user_id                                             |
| `start_datetime`                                         | *str*                                                    | :heavy_check_mark:                                       | Scopes results to requests that happened after datetime  | 2021-05-01T12:00:00.000Z                                 |
| `end_datetime`                                           | *str*                                                    | :heavy_check_mark:                                       | Scopes results to requests that happened before datetime | 2021-05-30T12:00:00.000Z                                 |