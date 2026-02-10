# ProxyPostProxyResponse


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `http_meta`                                      | [models.HTTPMetadata](../models/httpmetadata.md) | :heavy_check_mark:                               | N/A                                              |
| `response_json`                                  | Dict[str, *Any*]                                 | :heavy_minus_sign:                               | Ok                                               |
| `response_binary`                                | *Optional[httpx.Response]*                       | :heavy_minus_sign:                               | Ok                                               |
| `response_pdf`                                   | *Optional[httpx.Response]*                       | :heavy_minus_sign:                               | Ok                                               |
| `response_xml`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | Ok                                               |
| `response_csv`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | Ok                                               |
| `response_text`                                  | *Optional[str]*                                  | :heavy_minus_sign:                               | Ok                                               |
| `error_json`                                     | Dict[str, *Any*]                                 | :heavy_minus_sign:                               | Proxy error                                      |
| `error_xml`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Proxy error                                      |
| `error_html`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | Proxy error                                      |
| `error_text`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | Proxy error                                      |
| `headers`                                        | Dict[str, List[*str*]]                           | :heavy_check_mark:                               | N/A                                              |