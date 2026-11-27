# TargetURLScope

Where the vendor stores the webhook target URL. `app` means one URL per vendor developer app, which customers on Apideck's own credentials cannot configure. `tenant` means each customer's vendor account holds its own URL.

## Example Usage

```python
from apideck_unify.models import TargetURLScope

value = TargetURLScope.APP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `APP`    | app      |
| `TENANT` | tenant   |