# BatchSupportResourcesMode

`none` means this resource refuses batch writes. `native` satisfies a batch in a single downstream call against the provider's own batch endpoint, so the request counts as one request against your plan. `loop` satisfies it as a bounded sequential fan-out, one downstream call per item — so a request of N records takes roughly N times as long and counts as N requests.


## Values

| Name     | Value    |
| -------- | -------- |
| `NONE`   | none     |
| `NATIVE` | native   |
| `LOOP`   | loop     |