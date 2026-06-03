# PathMatchMode

How the path filter is matched. CONTAINS matches the path anywhere; STARTS_WITH / ENDS_WITH anchor the match; EXACT requires the whole path to match. Only applied when path is set.


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CONTAINS`    | CONTAINS      |
| `STARTS_WITH` | STARTS_WITH   |
| `ENDS_WITH`   | ENDS_WITH     |
| `EXACT`       | EXACT         |