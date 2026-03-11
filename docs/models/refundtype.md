# RefundType

Type of refund. `refund_receipt` for itemized refunds with product/service lines and payment (QBO RefundReceipt, NetSuite CashRefund). `cash_refund` for cash-out refunds with GL distribution or allocations (Sage Intacct). `credit_note_refund` for refunds applied against a credit note (Zoho Books).


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `REFUND_RECEIPT`     | refund_receipt       |
| `CASH_REFUND`        | cash_refund          |
| `CREDIT_NOTE_REFUND` | credit_note_refund   |