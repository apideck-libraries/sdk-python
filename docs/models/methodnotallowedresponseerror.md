# MethodNotAllowedResponseError

Why the operation is unsupported. Absent when there is no reason to give (the connector does not implement the operation). A string when the connector states a reason. An object `{ reason, error }` when a batch request is refused: `reason` is a stable code, `error` a human-readable explanation.


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.Error2`

```python
value: models.Error2 = /* values here */
```

