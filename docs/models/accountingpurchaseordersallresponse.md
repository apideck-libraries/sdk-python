# AccountingPurchaseOrdersAllResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [models.HTTPMetadata](../models/httpmetadata.md)                                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `get_purchase_orders_response`                                                       | [Optional[models.GetPurchaseOrdersResponse]](../models/getpurchaseordersresponse.md) | :heavy_minus_sign:                                                                   | PurchaseOrders                                                                       |
| `unexpected_error_response`                                                          | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)     | :heavy_minus_sign:                                                                   | Unexpected error                                                                     |