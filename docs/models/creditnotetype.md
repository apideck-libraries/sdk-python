# CreditNoteType

Whether this credit note reduces an amount owed by a customer (accounts receivable) or owed to a supplier (accounts payable). `accounts_payable_credit` support is connector-specific — most connectors only expose the accounts-receivable side. Check the connector's gotchas for known deviations.

## Example Usage

```python
from apideck_unify.models import CreditNoteType

value = CreditNoteType.ACCOUNTS_RECEIVABLE_CREDIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `ACCOUNTS_RECEIVABLE_CREDIT` | accounts_receivable_credit   |
| `ACCOUNTS_PAYABLE_CREDIT`    | accounts_payable_credit      |