# AccountingPaymentsBatchAddResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `batch_payments_response`                                                        | [Optional[models.BatchPaymentsResponse]](../models/batchpaymentsresponse.md)     | :heavy_minus_sign:                                                               | Payments batch processed                                                         |
| `unexpected_error_response`                                                      | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md) | :heavy_minus_sign:                                                               | Unexpected error                                                                 |