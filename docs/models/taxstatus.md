# TaxStatus

The tax applicability of the product: `taxable` (the product is taxed), `shipping` (only the shipping is taxed, the product itself is exempt) or `none` (neither is taxed).

## Example Usage

```python
from apideck_unify.models import TaxStatus

value = TaxStatus.TAXABLE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `TAXABLE`  | taxable    |
| `SHIPPING` | shipping   |
| `NONE`     | none       |