# ListType

Whether the List is static (a fixed set of records) or dynamic (a saved segment that is automatically kept up to date based on filter criteria).

## Example Usage

```python
from apideck_unify.models import ListType

value = ListType.STATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `STATIC`  | static    |
| `DYNAMIC` | dynamic   |