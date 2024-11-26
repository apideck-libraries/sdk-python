# ConsumerMetadata

The metadata of the consumer. This is used to display the consumer in the sidebar. This is optional, but recommended.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `account_name`                                             | *Optional[str]*                                            | :heavy_minus_sign:                                         | The name of the account as shown in the sidebar.           | SpaceX                                                     |
| `user_name`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | The name of the user as shown in the sidebar.              | Elon Musk                                                  |
| `email`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | The email of the user as shown in the sidebar.             | elon@musk.com                                              |
| `image`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | The avatar of the user in the sidebar. Must be a valid URL | https://www.spacex.com/static/images/share.jpg             |