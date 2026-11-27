# OauthCredentialsSource

Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.

## Example Usage

```python
from apideck_unify.models import OauthCredentialsSource

value = OauthCredentialsSource.INTEGRATION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `INTEGRATION` | integration   |
| `CONNECTION`  | connection    |