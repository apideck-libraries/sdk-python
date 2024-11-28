# IssueTrackingCollectionTicketsOneResponse


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `http_meta`                                                                      | [models.HTTPMetadata](../models/httpmetadata.md)                                 | :heavy_check_mark:                                                               | N/A                                                                              |
| `get_ticket_response`                                                            | [Optional[models.GetTicketResponse]](../models/getticketresponse.md)             | :heavy_minus_sign:                                                               | Get a Ticket                                                                     |
| `unexpected_error_response`                                                      | [Optional[models.UnexpectedErrorResponse]](../models/unexpectederrorresponse.md) | :heavy_minus_sign:                                                               | Unexpected error                                                                 |