# GetFileResponse

File


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `status_code`                                  | *int*                                          | :heavy_check_mark:                             | HTTP Response Status Code                      | 200                                            |
| `status`                                       | *str*                                          | :heavy_check_mark:                             | HTTP Response Status                           | OK                                             |
| `service`                                      | *str*                                          | :heavy_check_mark:                             | Apideck ID of service provider                 | google-drive                                   |
| `resource`                                     | *str*                                          | :heavy_check_mark:                             | Unified API resource name                      | files                                          |
| `operation`                                    | *str*                                          | :heavy_check_mark:                             | Operation performed                            | one                                            |
| `data`                                         | [models.UnifiedFile](../models/unifiedfile.md) | :heavy_check_mark:                             | N/A                                            |                                                |