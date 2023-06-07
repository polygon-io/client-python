# This Python script uses the Polygon.io API to fetch and aggregate monthly
# stock market data for a specified ticker symbol from the start of 2020 to
# June 8, 2023. This provides you with a method to pull a large set of
# aggregate market data for a specific ticker symbol over an extended period
# of time, storing all data in a single list for later use or analysis.
#
# Just set your API key, the start_year, and final_end_date.
#
from polygon import RESTClient
from datetime import datetime
from dateutil.relativedelta import relativedelta

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

# Define your ticker
ticker = "AAPL"

# Define your start year
start_year = 2020

# Initialize start date
start_date = datetime(start_year, 1, 1)

# Define the final end date
final_end_date = datetime(2023, 6, 8)

# Create an empty list to store all the aggs
all_aggs = []

while start_date <= final_end_date:
    # Calculate end date as the last day of the current month
    end_date = start_date + relativedelta(day=31)

    # Make sure we don't exceed the specific end date
    end_date = min(end_date, final_end_date)

    # Break the loop if start_date is after the final_end_date
    if start_date > final_end_date:
        break

    # Print status message
    print(
        f"Fetching data for {ticker} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    )

    aggs = client.get_aggs(
        ticker,
        1,
        "minute",
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
        limit=50000,
    )

    # Add each item in the current month's aggs to the list
    for item in aggs:
        all_aggs.append(item)

    # Increment start_date to the next month
    start_date += relativedelta(months=1)

print(len(all_aggs))

# Print all the aggs at the end
# for aggs in all_aggs:
#    print(aggs)
