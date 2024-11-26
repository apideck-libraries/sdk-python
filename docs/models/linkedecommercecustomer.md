# LinkedEcommerceCustomer

The customer this entity is linked to.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *Nullable[str]*                                      | :heavy_check_mark:                                   | The ID of the customer this entity is linked to.     | 12345                                                |
| `name`                                               | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Full name of the customer                            | John Doe                                             |
| `first_name`                                         | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | First name of the customer                           | John                                                 |
| `last_name`                                          | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Last name of the customer                            | Doe                                                  |
| `company_name`                                       | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Company name of the customer                         | Acme Inc.                                            |
| `phone_numbers`                                      | List[[models.PhoneNumber](../models/phonenumber.md)] | :heavy_minus_sign:                                   | N/A                                                  |                                                      |
| `emails`                                             | List[[models.Email](../models/email.md)]             | :heavy_minus_sign:                                   | N/A                                                  |                                                      |