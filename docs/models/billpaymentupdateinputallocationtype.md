# BillPaymentUpdateInputAllocationType

Type of entity this payment should be attributed to.

## Example Usage

```python
from apideck_unify.models import BillPaymentUpdateInputAllocationType

value = BillPaymentUpdateInputAllocationType.BILL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `BILL`          | bill            |
| `EXPENSE`       | expense         |
| `CREDIT_MEMO`   | credit_memo     |
| `OVER_PAYMENT`  | over_payment    |
| `PRE_PAYMENT`   | pre_payment     |
| `JOURNAL_ENTRY` | journal_entry   |
| `OTHER`         | other           |