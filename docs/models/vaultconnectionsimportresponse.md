# VaultConnectionsImportResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `http_meta`                                                                        | [models.HTTPMetadata](../models/httpmetadata.md)                                   | :heavy_check_mark:                                                                 | N/A                                                                                |
| `create_connection_response`                                                       | [Optional[models.CreateConnectionResponse]](../models/createconnectionresponse.md) | :heavy_minus_sign:                                                                 | Connection created                                                                 |
| `unexpected_error_response`                                                        | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)   | :heavy_minus_sign:                                                                 | Unexpected error                                                                   |