# Sessions
(*vault.sessions*)

## Overview

### Available Operations

* [create](#create) - Create Session

## create

Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
URL to allow temporary access to manage their integrations and settings.

Note: This is a short lived token that will expire after 1 hour (TTL: 3600).


### Example Usage

```python
import apideck_unify
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.vault.sessions.create(request={
        "consumer_metadata": {
            "account_name": "SpaceX",
            "user_name": "Elon Musk",
            "email": "elon@musk.com",
            "image": "https://www.spacex.com/static/images/share.jpg",
        },
        "redirect_uri": "https://mysaas.com/dashboard",
        "settings": {
            "unified_apis": [
                apideck_unify.UnifiedAPIID.CRM,
            ],
            "session_length": "30m",
        },
        "theme": {
            "favicon": "https://res.cloudinary.com/apideck/icons/intercom",
            "logo": "https://res.cloudinary.com/apideck/icons/intercom",
            "primary_color": "#286efa",
            "sidepanel_background_color": "#286efa",
            "sidepanel_text_color": "#FFFFFF",
            "vault_name": "Intercom",
            "privacy_url": "https://compliance.apideck.com/privacy-policy",
            "terms_url": "https://www.termsfeed.com/terms-conditions/957c85c1b089ae9e3219c83eff65377e",
        },
        "custom_consumer_settings": {
            "feature_flag_1": True,
            "tax_rates": [
                {
                    "id": "6",
                    "label": "6%",
                },
                {
                    "id": "21",
                    "label": "21%",
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Session](../../models/session.md)                           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VaultSessionsCreateResponse](../../models/vaultsessionscreateresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.BadRequestResponse      | 400                            | application/json               |
| models.UnauthorizedResponse    | 401                            | application/json               |
| models.PaymentRequiredResponse | 402                            | application/json               |
| models.NotFoundResponse        | 404                            | application/json               |
| models.UnprocessableResponse   | 422                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |