# PathMatchMode

How the path filter is matched. CONTAINS matches the path anywhere; STARTS_WITH / ENDS_WITH anchor the match; EXACT requires the whole path to match. Only applied when path is set.

## Example Usage

```python
from apideck_unify.models import PathMatchMode

value = PathMatchMode.CONTAINS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CONTAINS`    | CONTAINS      |
| `STARTS_WITH` | STARTS_WITH   |
| `ENDS_WITH`   | ENDS_WITH     |
| `EXACT`       | EXACT         |