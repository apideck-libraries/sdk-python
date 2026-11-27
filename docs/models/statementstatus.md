# StatementStatus

The current status of the bank feed statement.

## Example Usage

```python
from apideck_unify.models import StatementStatus

value = StatementStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `REJECTED` | rejected   |
| `SUCCESS`  | success    |