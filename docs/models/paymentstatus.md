# PaymentStatus

Status of payment

## Example Usage

```python
from apideck_unify.models import PaymentStatus

value = PaymentStatus.DRAFT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `DRAFT`      | draft        |
| `AUTHORISED` | authorised   |
| `REJECTED`   | rejected     |
| `PAID`       | paid         |
| `VOIDED`     | voided       |
| `DELETED`    | deleted      |