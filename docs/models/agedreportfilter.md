# AgedReportFilter


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `customer_id`                                             | *Optional[str]*                                           | :heavy_minus_sign:                                        | Filter by customer id                                     | 123abc                                                    |
| `supplier_id`                                             | *Optional[str]*                                           | :heavy_minus_sign:                                        | Filter by supplier id                                     | 123abc                                                    |
| `report_as_of_date`                                       | *Optional[str]*                                           | :heavy_minus_sign:                                        | The cutoff date for considering transactions              | 2024-01-01                                                |
| `period_count`                                            | *Optional[int]*                                           | :heavy_minus_sign:                                        | Number of periods to split the aged creditors report into | 3                                                         |
| `period_length`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | Length of each period in days                             | 30                                                        |