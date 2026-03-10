# Email


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | Unique identifier for the email address                      | 123                                                          |
| `email`                                                      | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | Email address                                                | elon@musk.com                                                |
| `type`                                                       | [OptionalNullable[models.EmailType]](../models/emailtype.md) | :heavy_minus_sign:                                           | Email type                                                   | primary                                                      |
| `__pydantic_extra__`                                         | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |                                                              |