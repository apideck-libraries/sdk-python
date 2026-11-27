# JournalType

Normalized journal classification.

## Example Usage

```python
from apideck_unify.models import JournalType

value = JournalType.GENERAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `GENERAL`              | general                |
| `SALES`                | sales                  |
| `PURCHASE`             | purchase               |
| `SALES_CREDIT_NOTE`    | sales_credit_note      |
| `PURCHASE_CREDIT_NOTE` | purchase_credit_note   |
| `CASH`                 | cash                   |
| `BANK`                 | bank                   |
| `PAYMENT_SERVICE`      | payment_service        |
| `OTHER`                | other                  |