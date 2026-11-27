# AccountingPaymentMethodsAllResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [models.HTTPMetadata](../models/httpmetadata.md)                                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `get_payment_methods_response`                                                       | [Optional[models.GetPaymentMethodsResponse]](../models/getpaymentmethodsresponse.md) | :heavy_minus_sign:                                                                   | Payment Methods                                                                      |
| `unexpected_error_response`                                                          | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)     | :heavy_minus_sign:                                                                   | Unexpected error                                                                     |