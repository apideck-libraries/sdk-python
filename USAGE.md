<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from apideck import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as s:
    res = s.accounting.tax_rates.list(request={
        "service_id": "salesforce",
        "filter_": {
            "assets": True,
            "equity": True,
            "expenses": True,
            "liabilities": True,
            "revenue": True,
        },
        "pass_through": {
            "search": "San Francisco",
        },
        "fields": "id,updated_at",
    })

    if res.get_tax_rates_response is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from apideck import Apideck
import asyncio
import os

async def main():
    async with Apideck(
        api_key=os.getenv("APIDECK_API_KEY", ""),
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    ) as s:
        res = await s.accounting.tax_rates.list_async(request={
            "service_id": "salesforce",
            "filter_": {
                "assets": True,
                "equity": True,
                "expenses": True,
                "liabilities": True,
                "revenue": True,
            },
            "pass_through": {
                "search": "San Francisco",
            },
            "fields": "id,updated_at",
        })

        if res.get_tax_rates_response is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->