# BankFeedAccountStatus

Whether the data consumer may see this account. `revoked` hides it from the consumer without deleting it; `active` restores it. Unrelated to `feed_status`. Only connectors that list it support it; others ignore the field, so setting it there changes nothing.

## Example Usage

```python
from apideck_unify.models import BankFeedAccountStatus

value = BankFeedAccountStatus.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ACTIVE`  | active    |
| `REVOKED` | revoked   |