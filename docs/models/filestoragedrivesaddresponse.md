# FileStorageDrivesAddResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `create_drive_response`                                                          | [Optional[models.CreateDriveResponse]](../models/createdriveresponse.md)         | :heavy_minus_sign:                                                               | Drives                                                                           |
| `unexpected_error_response`                                                      | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md) | :heavy_minus_sign:                                                               | Unexpected error                                                                 |