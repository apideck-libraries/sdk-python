# EcommerceOrdersFilter


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `email`                                  | *Optional[str]*                          | :heavy_minus_sign:                       | Customer email address to filter on      | elon@musk.com                            |
| `customer_id`                            | *Optional[str]*                          | :heavy_minus_sign:                       | Customer id to filter on                 | 123                                      |
| `updated_since`                          | *Optional[str]*                          | :heavy_minus_sign:                       | Minimum date the order was last modified | 2020-09-30T07:43:32.000Z                 |
| `created_since`                          | *Optional[str]*                          | :heavy_minus_sign:                       | Minimum date the order was created       | 2020-09-30T07:43:32.000Z                 |