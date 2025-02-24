# UpdateConnectionResponse

Connection updated


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `status_code`                                                           | *int*                                                                   | :heavy_check_mark:                                                      | HTTP Response Status Code                                               | 200                                                                     |
| `status`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | HTTP Response Status                                                    | OK                                                                      |
| `data`                                                                  | [models.Connection](../models/connection.md)                            | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `raw`                                                                   | Dict[str, *Any*]                                                        | :heavy_minus_sign:                                                      | Raw response from the integration when raw=true query param is provided |                                                                         |