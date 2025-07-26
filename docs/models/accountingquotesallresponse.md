# AccountingQuotesAllResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `get_quotes_response`                                                            | [Optional[models.GetQuotesResponse]](../models/getquotesresponse.md)             | :heavy_minus_sign:                                                               | Quotes                                                                           |
| `unexpected_error_response`                                                      | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md) | :heavy_minus_sign:                                                               | Unexpected error                                                                 |