# Migration Guide

This guide helps you migrate from the previous apideck SDK to the new apideck-unify SDK.

## Key Changes

1. ** Package Name and Installation **

```sh
# Old package
pip install apideck

# New package
pip install apideck-unify
```

Now you will have to import apideck_unify:

```
from apideck_unify import Apideck
```


2. **Method Naming Changes**

```
# Old SDK
from apideck.api import crm_api

api_instance = crm_api.CrmApi(api_client)
response = api_instance.contacts_all(
    raw=False,
    consumer_id="test-consumer",
    app_id="app-id",
    service_id="salesforce"
)

# New SDK
from apideck_unify import Apideck

client = Apideck(
    api_key="your-api-key",
    app_id="app-id",
    consumer_id="test-consumer"
)

response = client.crm.contacts.list()
```

3. **Response Structure**

The new SDK wraps all responses in a typed response object that includes both the API response and HTTP metadata:

```
# Old SDK
response = api_instance.contacts_all()
print(response.data[0].id)

# New SDK

## Access data payload
result = client.crm.contacts.list()
print(result.get_contacts_response.data[0].id)

# Access HTTP metadata
print(result.http_meta.status_code)
print(result.http_meta.headers)
```

4. **Method Naming Convention Changes**

```
| Old Method | New Method |
|------------|------------|
| contacts_all | contacts.list |
| contacts_add | contacts.create |
| contacts_one | contacts.get |
| contacts_update | contacts.update |
| contacts_delete | contacts.delete |
...
```

5. **Configuration and Authentication**

```
# Old SDK
import apideck
from apideck.api import crm_api

configuration = apideck.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'Bearer'

with apideck.ApiClient(configuration) as api_client:
    api_instance = crm_api.CrmApi(api_client)

# New SDK
from apideck_unify import Apideck

client = Apideck(
    api_key="your-api-key",
    app_id="your-app-id",
    consumer_id="test-consumer"
)
```

6. ** Error Handling**

```
# Old SDK
try:
    response = api_instance.contacts_all()
except apideck.ApiException as e:
    print("Exception when calling CrmApi->contacts_all: %s\n" % e)

# New SDK
from apideck_unify.errors import ApiError, ValidationError

try:
    result = client.crm.contacts.list()
except ValidationError as e:
    print("Validation error:", e.message)
except ApiError as e:
    print("API error:", e.message, e.status_code)
```

For more information about error handling, please check our [documentation](https://github.com/apideck-libraries/sdk-python?tab=readme-ov-file#error-handling)

## Breaking Changes

- Package name has changed from `apideck` to `apideck-unify`
- All API method names have been restructured for consistency
- Configuration and client initialization has been simplified
- Response structure now includes typed response wrappers and HTTP metadata
- Error handling has been improved with specific error types
- Some property names in request/response objects may have changed to follow Python naming conventions


## Need help?

If you encounter any issues during migration:

1. Checkout out our [documentation](https://github.com/apideck-libraries/sdk-python?tab=readme-ov-file#apideck-unify)
2. Open an issue on our [GitHub repository](https://github.com/apideck-libraries/sdk-python/issues)
3. Contact our support at `support@apideck.com`