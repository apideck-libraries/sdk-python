# CustomField


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Unique identifier for the custom field.              | 2389328923893298                                     |
| `name`                                               | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Name of the custom field.                            | employee_level                                       |
| `description`                                        | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | More information about the custom field              | Employee Level                                       |
| `value`                                              | [OptionalNullable[models.Value]](../models/value.md) | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `__pydantic_extra__`                                 | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | N/A                                                  |                                                      |