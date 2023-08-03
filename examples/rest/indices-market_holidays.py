from polygon import RESTClient
from polygon.rest.models import (
    MarketHoliday,
)

# docs
# https://polygon.io/docs/indices/get_v1_marketstatus_upcoming
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-market-holidays

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

holidays = client.get_market_holidays()
# print(holidays)

# print date, name, and exchange
for holiday in holidays:
    # verify this is an exchange
    if isinstance(holiday, MarketHoliday):
        print("{:<15}{:<15} ({})".format(holiday.date, holiday.name, holiday.exchange))
