# TaxType

The tax applicability of this line item. Overrides the root-level tax_type for this line.

## Example Usage

```python
from apideck_unify.models import TaxType

value = TaxType.SALES

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `SALES`    | sales      |
| `PURCHASE` | purchase   |