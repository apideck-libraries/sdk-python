# DisabledReason

Indicates why the webhook has been disabled. `retry_limit`: webhook reached its retry limit. `usage_limit`: account is over its usage limit. `delivery_url_validation_failed`: delivery URL failed validation during webhook creation or update.


## Values

| Name                             | Value                            |
| -------------------------------- | -------------------------------- |
| `NONE`                           | none                             |
| `RETRY_LIMIT`                    | retry_limit                      |
| `USAGE_LIMIT`                    | usage_limit                      |
| `DELIVERY_URL_VALIDATION_FAILED` | delivery_url_validation_failed   |