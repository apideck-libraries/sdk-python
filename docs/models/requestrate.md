# RequestRate

The rate at which requests for resources will be made to downstream.


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `rate`                                  | *int*                                   | :heavy_check_mark:                      | The number of requests per window unit. |
| `size`                                  | *int*                                   | :heavy_check_mark:                      | Size of request window.                 |
| `unit`                                  | [models.Unit](../models/unit.md)        | :heavy_check_mark:                      | The window unit for the rate.           |