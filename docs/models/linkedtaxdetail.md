# LinkedTaxDetail


## Fields

| Field                                 | Type                                  | Required                              | Description                           | Example                               |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `type`                                | *Optional[str]*                       | :heavy_minus_sign:                    | The type of tax.                      | GST on Purchases                      |
| `number`                              | *OptionalNullable[str]*               | :heavy_minus_sign:                    | The number of the tax.                | 123456                                |
| `is_transaction_tax`                  | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether the tax is a transaction tax. | true                                  |
| `is_primary_tax`                      | *Optional[bool]*                      | :heavy_minus_sign:                    | Whether the tax is a primary tax.     | true                                  |