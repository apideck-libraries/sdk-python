# SharedLinkTarget


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `id`                                                       | *Optional[str]*                                            | :heavy_minus_sign:                                         | A unique identifier for an object.                         | 12345                                                      |
| `name`                                                     | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | The name of the file                                       | sample.jpg                                                 |
| `type`                                                     | [OptionalNullable[models.FileType]](../models/filetype.md) | :heavy_minus_sign:                                         | The type of resource. Could be file, folder or url         | file                                                       |
| `__pydantic_extra__`                                       | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |                                                            |