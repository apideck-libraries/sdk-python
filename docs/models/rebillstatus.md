# RebillStatus

Status of the rebilling process for this line item.

## Example Usage

```python
from apideck_unify.models import RebillStatus

value = RebillStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PENDING` | pending   |
| `BILLED`  | billed    |
| `VOIDED`  | voided    |
| `OTHER`   | other     |