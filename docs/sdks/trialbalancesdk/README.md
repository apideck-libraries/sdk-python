# TrialBalanceSDK
(*accounting.trial_balance*)

## Overview

### Available Operations

* [get](#get) - Get Trial Balance

## get

Get the trial balance as of a date. Read-only.

### Example Usage

<!-- UsageSnippet language="python" operationID="accounting.trialBalanceOne" method="get" path="/accounting/trial-balance" -->
```python
import apideck_unify
from apideck_unify import Apideck
import os


with Apideck(
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    api_key=os.getenv("APIDECK_API_KEY", ""),
) as apideck:

    res = apideck.accounting.trial_balance.get(service_id="salesforce", company_id="12345", pass_through={
        "search": "San Francisco",
    }, filter_={
        "end_date": "2025-12-31",
        "accounting_method": apideck_unify.TrialBalanceFilterAccountingMethod.ACCRUAL,
    }, raw=False)

    assert res.get_trial_balance_response is not None

    # Handle response
    print(res.get_trial_balance_response)

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  | Example                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `consumer_id`                                                                                                                                                | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | ID of the consumer which you want to get or push data from                                                                                                   | test-consumer                                                                                                                                                |
| `app_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The ID of your Unify application                                                                                                                             | dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX                                                                                                                      |
| `service_id`                                                                                                                                                 | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.                | salesforce                                                                                                                                                   |
| `company_id`                                                                                                                                                 | *Optional[str]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                           | The ID of the company to scope requests to. For connectors that support multi-company, this overrides the default company configured in connection settings. | 12345                                                                                                                                                        |
| `pass_through`                                                                                                                                               | Dict[str, *Any*]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                           | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads            | {<br/>"search": "San Francisco"<br/>}                                                                                                                        |
| `filter_`                                                                                                                                                    | [Optional[models.TrialBalanceFilter]](../../models/trialbalancefilter.md)                                                                                    | :heavy_minus_sign:                                                                                                                                           | Apply filters                                                                                                                                                | {<br/>"end_date": "2025-12-31",<br/>"accounting_method": "accrual"<br/>}                                                                                     |
| `raw`                                                                                                                                                        | *Optional[bool]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                           | Include raw response. Mostly used for debugging purposes                                                                                                     |                                                                                                                                                              |
| `retries`                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                             | :heavy_minus_sign:                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                          |                                                                                                                                                              |

### Response

**[models.AccountingTrialBalanceOneResponse](../../models/accountingtrialbalanceoneresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |