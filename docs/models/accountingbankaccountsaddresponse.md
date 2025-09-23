# AccountingBankAccountsAddResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [models.HTTPMetadata](../models/httpmetadata.md)                                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `create_bank_account_response`                                                       | [Optional[models.CreateBankAccountResponse]](../models/createbankaccountresponse.md) | :heavy_minus_sign:                                                                   | Bank Account created                                                                 |
| `unexpected_error_response`                                                          | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)     | :heavy_minus_sign:                                                                   | Unexpected error                                                                     |