# OAuthGrantType

OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types

## Example Usage

```python
from apideck_unify.models import OAuthGrantType

value = OAuthGrantType.AUTHORIZATION_CODE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `AUTHORIZATION_CODE` | authorization_code   |
| `CLIENT_CREDENTIALS` | client_credentials   |
| `PASSWORD`           | password             |