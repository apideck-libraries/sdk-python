# EcommerceDiscount

An object representing a discount applied to an ecommerce order or product.


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `code`                               | *OptionalNullable[str]*              | :heavy_minus_sign:                   | The code used to apply the discount. | SUMMER20                             |
| `amount`                             | *OptionalNullable[str]*              | :heavy_minus_sign:                   | The fixed amount of the discount.    | 5.99                                 |
| `percentage`                         | *OptionalNullable[str]*              | :heavy_minus_sign:                   | The percentage of the discount.      | 0.1                                  |