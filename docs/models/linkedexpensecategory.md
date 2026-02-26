# LinkedExpenseCategory

The expense category this entity is linked to.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *Optional[str]*                                 | :heavy_minus_sign:                              | The ID of the expense category.                 | 12345                                           |
| `downstream_id`                                 | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | The third-party API ID of the expense category. | 12345                                           |
| `display_id`                                    | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | The display ID of the expense category.         | Airfare                                         |
| `name`                                          | *OptionalNullable[str]*                         | :heavy_minus_sign:                              | The name of the expense category.               | Airfare                                         |