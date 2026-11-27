# Health

Operational health status of the connection

## Example Usage

```python
from apideck_unify.models import Health

value = Health.REVOKED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `REVOKED`              | revoked                |
| `MISSING_SETTINGS`     | missing_settings       |
| `NEEDS_CONSENT`        | needs_consent          |
| `PENDING_CONFIRMATION` | pending_confirmation   |
| `NEEDS_AUTH`           | needs_auth             |
| `PENDING_REFRESH`      | pending_refresh        |
| `OK`                   | ok                     |
| `DEGRADED`             | degraded               |