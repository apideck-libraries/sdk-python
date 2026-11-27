# CustomObjectSchemaType

## Example Usage

```python
from apideck_unify.models import CustomObjectSchemaType

value = CustomObjectSchemaType.STRING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `STRING`      | string        |
| `NUMBER`      | number        |
| `INTEGER`     | integer       |
| `BOOLEAN`     | boolean       |
| `DATE`        | date          |
| `DATETIME`    | datetime      |
| `CURRENCY`    | currency      |
| `EMAIL`       | email         |
| `PHONE`       | phone         |
| `REFERENCE`   | reference     |
| `SELECT`      | select        |
| `MULTISELECT` | multiselect   |