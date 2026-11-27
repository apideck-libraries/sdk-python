# GeneralLedgerTransactionLineItemType

Side of the entry. Redundant with the sign of net_amount but exposed as an explicit flag for filtering convenience.

## Example Usage

```python
from apideck_unify.models import GeneralLedgerTransactionLineItemType

value = GeneralLedgerTransactionLineItemType.DEBIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `DEBIT`  | debit    |
| `CREDIT` | credit   |