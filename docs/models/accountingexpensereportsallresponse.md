# AccountingExpenseReportsAllResponse


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `http_meta`                                                                          | [models.HTTPMetadata](../models/httpmetadata.md)                                     | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `get_expense_reports_response`                                                       | [Optional[models.GetExpenseReportsResponse]](../models/getexpensereportsresponse.md) | :heavy_minus_sign:                                                                   | Expense Reports                                                                      |
| `unexpected_error_response`                                                          | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md)     | :heavy_minus_sign:                                                                   | Unexpected error                                                                     |