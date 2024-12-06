# ~~DeprecatedLinkedSupplier~~

The supplier this entity is linked to.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *Optional[str]*                                  | :heavy_minus_sign:                               | A unique identifier for an object.               | 12345                                            |
| `display_id`                                     | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The display ID of the supplier.                  | SUPP00101                                        |
| `display_name`                                   | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The display name of the supplier.                | Windsurf Shop                                    |
| `company_name`                                   | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | The company name of the supplier.                | The boring company                               |
| `address`                                        | [Optional[models.Address]](../models/address.md) | :heavy_minus_sign:                               | N/A                                              |                                                  |