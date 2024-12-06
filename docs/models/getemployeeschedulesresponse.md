# GetEmployeeSchedulesResponse

EmployeeSchedules


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `status_code`                                              | *int*                                                      | :heavy_check_mark:                                         | HTTP Response Status Code                                  | 200                                                        |
| `status`                                                   | *str*                                                      | :heavy_check_mark:                                         | HTTP Response Status                                       | OK                                                         |
| `service`                                                  | *str*                                                      | :heavy_check_mark:                                         | Apideck ID of service provider                             | sage-hr                                                    |
| `resource`                                                 | *str*                                                      | :heavy_check_mark:                                         | Unified API resource name                                  | Employees                                                  |
| `operation`                                                | *str*                                                      | :heavy_check_mark:                                         | Operation performed                                        | all                                                        |
| `data`                                                     | [models.EmployeeSchedules](../models/employeeschedules.md) | :heavy_check_mark:                                         | N/A                                                        |                                                            |