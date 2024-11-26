# BalanceSheetSDK
(*accounting.balance_sheet*)

## Overview

### Available Operations

* [get](#get) - Get BalanceSheet

## get

Get BalanceSheet

### Example Usage

```python
from apideck_sdk import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    customer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.balance_sheet.get(service_id="salesforce", pass_through={
        "search": "San Francisco",
    }, filter_={
        "start_date": "2021-01-01",
        "end_date": "2021-12-31",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                      | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.     | salesforce                                                                                                                                        |
| `pass_through`                                                                                                                                    | Dict[str, *Any*]                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads | {<br/>"search": "San Francisco"<br/>}                                                                                                             |
| `filter_`                                                                                                                                         | [Optional[models.BalanceSheetFilter]](../../models/balancesheetfilter.md)                                                                         | :heavy_minus_sign:                                                                                                                                | Apply filters                                                                                                                                     | {<br/>"start_date": "2021-01-01",<br/>"end_date": "2021-12-31"<br/>}                                                                              |
| `raw`                                                                                                                                             | *Optional[bool]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Include raw response. Mostly used for debugging purposes                                                                                          |                                                                                                                                                   |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[models.AccountingBalanceSheetOneResponse](../../models/accountingbalancesheetoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |