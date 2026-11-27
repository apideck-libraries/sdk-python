# GoodsReceiptStatus

Lifecycle status of the receipt. `draft` covers unposted or awaiting-validation documents, `pending_approval` covers documents submitted into an approval flow, `received` covers posted/validated/released receipts that have affected stock or the receiving ledger, `cancelled` covers voided, reversed or denied receipts.

## Example Usage

```python
from apideck_unify.models import GoodsReceiptStatus

value = GoodsReceiptStatus.DRAFT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `DRAFT`            | draft              |
| `PENDING_APPROVAL` | pending_approval   |
| `RECEIVED`         | received           |
| `CANCELLED`        | cancelled          |
| `OTHER`            | other              |