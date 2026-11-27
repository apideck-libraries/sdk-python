# AllocationType

Type of entity this payment should be attributed to.

## Example Usage

```python
from apideck_unify.models import AllocationType

value = AllocationType.INVOICE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `INVOICE`       | invoice         |
| `ORDER`         | order           |
| `EXPENSE`       | expense         |
| `CREDIT_MEMO`   | credit_memo     |
| `OVER_PAYMENT`  | over_payment    |
| `PRE_PAYMENT`   | pre_payment     |
| `JOURNAL_ENTRY` | journal_entry   |
| `OTHER`         | other           |
| `BILL`          | bill            |