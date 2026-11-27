# APIStatus

Status of the API. APIs with status live or beta are callable.

## Example Usage

```python
from apideck_unify.models import APIStatus

value = APIStatus.LIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `LIVE`        | live          |
| `BETA`        | beta          |
| `DEVELOPMENT` | development   |
| `CONSIDERING` | considering   |