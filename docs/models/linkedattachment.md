# LinkedAttachment


## Fields

| Field                            | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `name`                           | *OptionalNullable[str]*          | :heavy_minus_sign:               | The name of the file             | sample.jpg                       |
| `mime_type`                      | *OptionalNullable[str]*          | :heavy_minus_sign:               | The MIME type of the file.       | image/jpeg                       |
| `is_compressed`                  | *OptionalNullable[bool]*         | :heavy_minus_sign:               | Whether the file is c ompressed. | false                            |
| `encoding`                       | *OptionalNullable[str]*          | :heavy_minus_sign:               | The encoding of the file.        | base64                           |
| `content`                        | *OptionalNullable[str]*          | :heavy_minus_sign:               | The content of the file.         | data:image/jpeg;base64,...       |
| `notes`                          | *OptionalNullable[str]*          | :heavy_minus_sign:               | The notes of the file.           | A sample image                   |