# Website


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `url`                                                            | *str*                                                            | :heavy_check_mark:                                               | The website URL                                                  | http://example.com                                               |
| `id`                                                             | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | Unique identifier for the website                                | 12345                                                            |
| `type`                                                           | [OptionalNullable[models.WebsiteType]](../models/websitetype.md) | :heavy_minus_sign:                                               | The type of website                                              | primary                                                          |