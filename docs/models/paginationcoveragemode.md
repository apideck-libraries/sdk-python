# PaginationCoverageMode

How pagination is implemented on this connector. Native mode means Apideck is using the pagination parameters of the connector. With virtual pagination, the connector does not support pagination, but Apideck emulates it.

## Example Usage

```python
from apideck_unify.models import PaginationCoverageMode

value = PaginationCoverageMode.NATIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `NATIVE`  | native    |
| `VIRTUAL` | virtual   |