# AccountingSalesOrdersAddResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [models.HTTPMetadata](../models/httpmetadata.md)                                   | :heavy_check_mark:                                                                 | N/A                                                                                |
| `create_sales_order_response`                                                      | [Optional[models.CreateSalesOrderResponse]](../models/createsalesorderresponse.md) | :heavy_minus_sign:                                                                 | Sales Orders                                                                       |
| `unexpected_error_response`                                                        | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)   | :heavy_minus_sign:                                                                 | Unexpected error                                                                   |