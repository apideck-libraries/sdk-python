# GeneralLedgerTransactionSourceType

The originating transaction type that produced this posting in the general ledger. Discriminates whether the entry came from an invoice, a bill, a payment, a manual journal, etc. This is the key field that distinguishes general-ledger-transactions from journal-entries (which only covers manually-captured entries). May be `null` when the upstream connector did not return an origin discriminator (e.g. Xero's single-record endpoint strips `SourceType` for every record; certain historical records also omit it). To recover a populated value, query the list endpoint.


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