# Schedule


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | A unique identifier for an object.                       | 12345                                                    |
| `start_date`                                             | *Optional[str]*                                          | :heavy_minus_sign:                                       | The start date, inclusive, of the schedule period.       | 2022-04-08                                               |
| `end_date`                                               | *Optional[str]*                                          | :heavy_minus_sign:                                       | The end date, inclusive, of the schedule period.         | 2022-04-21                                               |
| `work_pattern`                                           | [Optional[models.WorkPattern]](../models/workpattern.md) | :heavy_minus_sign:                                       | N/A                                                      |                                                          |
| `__pydantic_extra__`                                     | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | N/A                                                      |                                                          |