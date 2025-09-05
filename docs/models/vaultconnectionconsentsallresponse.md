# VaultConnectionConsentsAllResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [models.HTTPMetadata](../models/httpmetadata.md)                                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `get_consent_records_response`                                                       | [Optional[models.GetConsentRecordsResponse]](../models/getconsentrecordsresponse.md) | :heavy_minus_sign:                                                                   | Consent records                                                                      |
| `unexpected_error_response`                                                          | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)     | :heavy_minus_sign:                                                                   | Unexpected error                                                                     |