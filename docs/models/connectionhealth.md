# ConnectionHealth

The operational health status of the connection

## Example Usage

```python
from apideck_unify.models import ConnectionHealth

value = ConnectionHealth.OK

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `OK`                   | ok                     |
| `PENDING_REFRESH`      | pending_refresh        |
| `NEEDS_AUTH`           | needs_auth             |
| `PENDING_CONFIRMATION` | pending_confirmation   |
| `NEEDS_CONSENT`        | needs_consent          |
| `REVOKED`              | revoked                |
| `MISSING_SETTINGS`     | missing_settings       |
| `DEGRADED`             | degraded               |