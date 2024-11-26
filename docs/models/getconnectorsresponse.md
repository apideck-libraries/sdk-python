# GetConnectorsResponse

Connectors


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `status_code`                                               | *int*                                                       | :heavy_check_mark:                                          | HTTP Response Status Code                                   | 200                                                         |
| `status`                                                    | *str*                                                       | :heavy_check_mark:                                          | HTTP Response Status                                        | OK                                                          |
| `data`                                                      | List[[models.Connector](../models/connector.md)]            | :heavy_check_mark:                                          | N/A                                                         |                                                             |
| `meta`                                                      | [Optional[models.Meta]](../models/meta.md)                  | :heavy_minus_sign:                                          | Response metadata                                           |                                                             |
| `links`                                                     | [Optional[models.Links]](../models/links.md)                | :heavy_minus_sign:                                          | Links to navigate to previous or next pages through the API |                                                             |