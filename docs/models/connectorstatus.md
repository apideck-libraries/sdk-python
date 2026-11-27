# ConnectorStatus

Status of the connector. Connectors with status live or beta are callable.

## Example Usage

```python
from apideck_unify.models import ConnectorStatus

value = ConnectorStatus.LIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `LIVE`         | live           |
| `BETA`         | beta           |
| `EARLY_ACCESS` | early-access   |
| `DEVELOPMENT`  | development    |
| `CONSIDERING`  | considering    |