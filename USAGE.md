<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from apideck_unify import Apideck
import os

with Apideck(
    api_key=os.getenv("APIDECK_API_KEY", ""),
    consumer_id="test-consumer",
    app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
) as apideck:

    res = apideck.accounting.tax_rates.list(raw=False, consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", limit=20, filter_={
        "assets": True,
        "equity": True,
        "expenses": True,
        "liabilities": True,
        "revenue": True,
    }, pass_through={
        "search": "San Francisco",
    }, fields="id,updated_at")

    while res is not None:
        # Handle items

        res = res.next()
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from apideck_unify import Apideck
import asyncio
import os

async def main():
    async with Apideck(
        api_key=os.getenv("APIDECK_API_KEY", ""),
        consumer_id="test-consumer",
        app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    ) as apideck:

        res = await apideck.accounting.tax_rates.list_async(raw=False, consumer_id="test-consumer", app_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX", service_id="salesforce", limit=20, filter_={
            "assets": True,
            "equity": True,
            "expenses": True,
            "liabilities": True,
            "revenue": True,
        }, pass_through={
            "search": "San Francisco",
        }, fields="id,updated_at")

        while res is not None:
            # Handle items

            res = res.next()

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->