# PaymentUnit

Unit of measurement for employee compensation.

## Example Usage

```python
from apideck_unify.models import PaymentUnit

value = PaymentUnit.HOUR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `HOUR`     | hour       |
| `WEEK`     | week       |
| `MONTH`    | month      |
| `YEAR`     | year       |
| `PAYCHECK` | paycheck   |
| `OTHER`    | other      |