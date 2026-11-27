# RefundStatus

Status of refund. Maps to: QBO (limited status), NetSuite CashRefund status, Sage Intacct state (draft/posted/voided), Zoho Books vis_state.

## Example Usage

```python
from apideck_unify.models import RefundStatus

value = RefundStatus.DRAFT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `DRAFT`      | draft        |
| `AUTHORISED` | authorised   |
| `POSTED`     | posted       |
| `PAID`       | paid         |
| `VOIDED`     | voided       |
| `DELETED`    | deleted      |