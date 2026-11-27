# EcommerceOrderPaymentStatus

Current payment status of the order.

## Example Usage

```python
from apideck_unify.models import EcommerceOrderPaymentStatus

value = EcommerceOrderPaymentStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `PENDING`            | pending              |
| `AUTHORIZED`         | authorized           |
| `PAID`               | paid                 |
| `PARTIAL`            | partial              |
| `REFUNDED`           | refunded             |
| `VOIDED`             | voided               |
| `UNKNOWN`            | unknown              |
| `PARTIALLY_REFUNDED` | partially_refunded   |