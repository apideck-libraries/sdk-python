# SourceType

Filter by the originating transaction type.

## Example Usage

```python
from apideck_unify.models import SourceType

value = SourceType.OTHER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `OTHER`         | other           |
| `INVOICE`       | invoice         |
| `BILL`          | bill            |
| `CREDIT_NOTE`   | credit_note     |
| `PAYMENT`       | payment         |
| `REFUND`        | refund          |
| `EXPENSE`       | expense         |
| `JOURNAL_ENTRY` | journal_entry   |
| `PAYROLL`       | payroll         |