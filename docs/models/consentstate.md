# ConsentState

The current consent state of the connection

## Example Usage

```python
from apideck_unify.models import ConsentState

value = ConsentState.IMPLICIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `IMPLICIT`           | implicit             |
| `PENDING`            | pending              |
| `GRANTED`            | granted              |
| `DENIED`             | denied               |
| `REVOKED`            | revoked              |
| `REQUIRES_RECONSENT` | requires_reconsent   |