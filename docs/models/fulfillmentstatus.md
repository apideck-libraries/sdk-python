# FulfillmentStatus

Current fulfillment status of the order.

## Example Usage

```python
from apideck_unify.models import FulfillmentStatus

value = FulfillmentStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `SHIPPED`   | shipped     |
| `PARTIAL`   | partial     |
| `DELIVERED` | delivered   |
| `CANCELLED` | cancelled   |
| `RETURNED`  | returned    |
| `UNKNOWN`   | unknown     |