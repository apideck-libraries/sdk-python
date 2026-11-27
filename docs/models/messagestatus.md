# MessageStatus

Status of the delivery of the message.

## Example Usage

```python
from apideck_unify.models import MessageStatus

value = MessageStatus.ACCEPTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `ACCEPTED`    | accepted      |
| `SCHEDULED`   | scheduled     |
| `CANCELED`    | canceled      |
| `QUEUED`      | queued        |
| `SENDING`     | sending       |
| `SENT`        | sent          |
| `FAILED`      | failed        |
| `DELIVERED`   | delivered     |
| `UNDELIVERED` | undelivered   |
| `RECEIVING`   | receiving     |
| `RECEIVED`    | received      |
| `READ`        | read          |