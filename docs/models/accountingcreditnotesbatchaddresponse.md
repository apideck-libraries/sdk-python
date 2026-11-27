# AccountingCreditNotesBatchAddResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [models.HTTPMetadata](../models/httpmetadata.md)                                   | :heavy_check_mark:                                                                 | N/A                                                                                |
| `batch_credit_notes_response`                                                      | [Optional[models.BatchCreditNotesResponse]](../models/batchcreditnotesresponse.md) | :heavy_minus_sign:                                                                 | Credit Notes batch processed                                                       |
| `unexpected_error_response`                                                        | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)   | :heavy_minus_sign:                                                                 | Unexpected error                                                                   |