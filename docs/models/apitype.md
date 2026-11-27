# APIType

Indicates whether the API is a Unified API. If unified_api is false, the API is a Platform API.

## Example Usage

```python
from apideck_unify.models import APIType

value = APIType.PLATFORM

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PLATFORM` | platform   |
| `UNIFIED`  | unified    |