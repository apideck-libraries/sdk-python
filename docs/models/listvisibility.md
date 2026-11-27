# ListVisibility

The visibility of the List. Which of these values a given connector can return depends on its native sharing model — see the connector-specific gotchas below for details.

## Example Usage

```python
from apideck_unify.models import ListVisibility

value = ListVisibility.PRIVATE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `PRIVATE` | private   |
| `SHARED`  | shared    |
| `PUBLIC`  | public    |