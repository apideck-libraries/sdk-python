# Rebilling

Rebilling metadata for this line item.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `rebillable`                                                       | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether this line item is eligible for rebilling.                  | true                                                               |
| `rebill_status`                                                    | [OptionalNullable[models.RebillStatus]](../models/rebillstatus.md) | :heavy_minus_sign:                                                 | Status of the rebilling process for this line item.                | billed                                                             |
| `linked_transaction_id`                                            | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | The ID of the transaction this line item was rebilled to.          | txn_abc123                                                         |
| `linked_transaction_line_id`                                       | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | The ID of the line item in the rebilled transaction.               | line_xyz789                                                        |