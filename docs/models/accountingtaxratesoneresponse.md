# AccountingTaxRatesOneResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `get_tax_rate_response`                                                          | [Optional[models.GetTaxRateResponse]](../models/gettaxrateresponse.md)           | :heavy_minus_sign:                                                               | TaxRate                                                                          |
| `unexpected_error_response`                                                      | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md) | :heavy_minus_sign:                                                               | Unexpected error                                                                 |