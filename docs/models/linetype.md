# LineType

`account`: a ledger account. `unappropriated_result`: the result of earlier fiscal years not yet posted to an equity account, added by the connector. `unmapped`: a balance the accounting system reports without a ledger account.

## Example Usage

```python
from apideck_unify.models import LineType

value = LineType.ACCOUNT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `ACCOUNT`               | account                 |
| `UNAPPROPRIATED_RESULT` | unappropriated_result   |
| `UNMAPPED`              | unmapped                |