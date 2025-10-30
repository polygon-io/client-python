import datetime
import concurrent.futures
import logging
from massive import RESTClient
import signal
import sys
import pickle
import lz4.frame  # type: ignore

"""
This script performs the following tasks:

1. Downloads aggregated market data (referred to as 'aggs') for specific stock symbols using the Massive API.
2. Handles data for multiple dates and performs these operations in parallel to improve efficiency.
3. Saves the downloaded data in a compressed format (LZ4) using Python's pickle serialization.
4. Utilizes logging to track its progress and any potential errors.
5. Designed to be interruptible: listens for a Ctrl+C keyboard interrupt and exits gracefully when detected.

Usage:
1. pip install lz4
2. Set your Massive API key in the environment variable 'MASSIVE_API_KEY'.
3. Specify the date range and stock symbols you are interested in within the script.
4. Run the script.

The script will create compressed '.pickle.lz4' files containing the aggs for each specified stock symbol and date.

Note: This script is designed to be compatible with a data reader script, such as 'bulk_aggs_reader.py'.
"""

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def get_aggs_for_symbol_and_date(symbol_date_pair):
    """Retrieve aggs for a given symbol and date"""
    symbol, date = symbol_date_pair
    aggs = []
    client = RESTClient(trace=True)  # Uses MASSIVE_API_KEY environment variable

    for a in client.list_aggs(
        symbol,
        1,
        "minute",
        date,
        date,
        limit=50000,
    ):
        aggs.append(a)

    print(len(aggs))

    filename = f"{symbol}-aggs-{date}.pickle.lz4"
    with open(filename, "wb") as file:
        try:
            compressed_data = lz4.frame.compress(pickle.dumps(aggs))
            file.write(compressed_data)
        except TypeError as e:
            print(f"Serialization Error: {e}")

    logging.info(f"Downloaded aggs for {date} and saved to {filename}")


def weekdays_between(start_date, end_date):
    """Generate all weekdays between start_date and end_date"""
    day = start_date
    while day <= end_date:
        if day.weekday() < 5:  # 0-4 denotes Monday to Friday
            yield day
        day += datetime.timedelta(days=1)


def main():
    start_date = datetime.date(2023, 8, 1)
    end_date = datetime.date(2023, 8, 31)

    symbols = ["TSLA", "AAPL", "HCP", "GOOG"]  # The array of symbols you want

    dates = list(weekdays_between(start_date, end_date))

    # Generate a list of (symbol, date) pairs
    symbol_date_pairs = [(symbol, date) for symbol in symbols for date in dates]

    # Use ThreadPoolExecutor to download data in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(get_aggs_for_symbol_and_date, symbol_date_pairs)


if __name__ == "__main__":
    main()
