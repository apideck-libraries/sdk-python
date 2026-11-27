# EmploymentStatus

The employment status of the employee, indicating whether they are currently employed, inactive, terminated, or in another status.

## Example Usage

```python
from apideck_unify.models import EmploymentStatus

value = EmploymentStatus.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `ACTIVE`     | active       |
| `INACTIVE`   | inactive     |
| `TERMINATED` | terminated   |
| `OTHER`      | other        |