# AccountingAttachmentsUploadResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [models.HTTPMetadata](../models/httpmetadata.md)                                   | :heavy_check_mark:                                                                 | N/A                                                                                |
| `create_attachment_response`                                                       | [Optional[models.CreateAttachmentResponse]](../models/createattachmentresponse.md) | :heavy_minus_sign:                                                                 | Attachments                                                                        |
| `unexpected_error_response`                                                        | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)   | :heavy_minus_sign:                                                                 | Unexpected error                                                                   |