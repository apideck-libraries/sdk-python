# ProjectUpdateInputScheduleStatus

Current status of project schedule compared to plan

## Example Usage

```python
from apideck_unify.models import ProjectUpdateInputScheduleStatus

value = ProjectUpdateInputScheduleStatus.AHEAD_OF_SCHEDULE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                | Value               |
| ------------------- | ------------------- |
| `AHEAD_OF_SCHEDULE` | ahead_of_schedule   |
| `ON_SCHEDULE`       | on_schedule         |
| `BEHIND_SCHEDULE`   | behind_schedule     |
| `CRITICAL_DELAY`    | critical_delay      |