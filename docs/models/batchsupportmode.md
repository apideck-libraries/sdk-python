# BatchSupportMode

The connector's overall batch capability: `none` when no resource supports a batch write, otherwise the mode most of its resources use. This is a summary — read `resources` for the answer that applies to the resource you are calling, because a connector can be `native` for one resource and `loop` for another.

## Example Usage

```python
from apideck_unify.models import BatchSupportMode

value = BatchSupportMode.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `NONE`   | none     |
| `NATIVE` | native   |
| `LOOP`   | loop     |