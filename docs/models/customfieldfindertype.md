# CustomFieldFinderType

The declared data type of the custom field. Only returned by connectors that can read the field's definition; omitted otherwise.

## Example Usage

```python
from apideck_unify.models import CustomFieldFinderType

value = CustomFieldFinderType.TEXT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `TEXT`            | text              |
| `CHECKBOX`        | checkbox          |
| `TEL`             | tel               |
| `EMAIL`           | email             |
| `URL`             | url               |
| `TEXTAREA`        | textarea          |
| `SELECT`          | select            |
| `FILTERED_SELECT` | filtered-select   |
| `MULTI_SELECT`    | multi-select      |
| `DATETIME`        | datetime          |
| `DATE`            | date              |
| `TIME`            | time              |
| `NUMBER`          | number            |
| `PASSWORD`        | password          |