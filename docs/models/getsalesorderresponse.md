# GetSalesOrderResponse

Sales Orders


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `status_code`                                | *int*                                        | :heavy_check_mark:                           | HTTP Response Status Code                    | 200                                          |
| `status`                                     | *str*                                        | :heavy_check_mark:                           | HTTP Response Status                         | OK                                           |
| `service`                                    | *str*                                        | :heavy_check_mark:                           | Apideck ID of service provider               | acumatica                                    |
| `resource`                                   | *str*                                        | :heavy_check_mark:                           | Unified API resource name                    | SalesOrders                                  |
| `operation`                                  | *str*                                        | :heavy_check_mark:                           | Operation performed                          | one                                          |
| `data`                                       | [models.SalesOrder](../models/salesorder.md) | :heavy_check_mark:                           | N/A                                          |                                              |
| `meta`                                       | [Optional[models.Meta]](../models/meta.md)   | :heavy_minus_sign:                           | Response metadata                            |                                              |