# AccountingCreditNotesDeleteResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [models.HTTPMetadata](../models/httpmetadata.md)                                   | :heavy_check_mark:                                                                 | N/A                                                                                |
| `delete_credit_note_response`                                                      | [Optional[models.DeleteCreditNoteResponse]](../models/deletecreditnoteresponse.md) | :heavy_minus_sign:                                                                 | Credit Note deleted                                                                |
| `unexpected_error_response`                                                        | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)   | :heavy_minus_sign:                                                                 | Unexpected error                                                                   |