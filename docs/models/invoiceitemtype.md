# InvoiceItemType

The type of invoice item, indicating whether it is an inventory item, a service, or another type.

## Example Usage

```python
from apideck_unify.models import InvoiceItemType

value = InvoiceItemType.INVENTORY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `INVENTORY` | inventory   |
| `SERVICE`   | service     |
| `OTHER`     | other       |