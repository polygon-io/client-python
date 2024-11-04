import os
import pandas as pd # type: ignore
from collections import defaultdict
import pickle
import json

# Directory containing the daily CSV files
data_dir = "./aggregates_day/"

# Initialize a dictionary to hold trades data
trades_data = defaultdict(list)

# List all CSV files in the directory
files = sorted([f for f in os.listdir(data_dir) if f.endswith(".csv")])

print("Starting to process files...")

# Process each file (assuming files are named in order)
for file in files:
    print(f"Processing {file}")
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path)
    # For each stock, store the date and relevant data
    for _, row in df.iterrows():
        ticker = row["ticker"]
        date = pd.to_datetime(row["window_start"], unit="ns").date()
        trades = row["transactions"]
        close_price = row["close"]  # Ensure 'close' column exists in your CSV
        trades_data[ticker].append(
            {"date": date, "trades": trades, "close_price": close_price}
        )

print("Finished processing files.")
print("Building lookup table...")

# Now, build the lookup table with rolling averages and percentage price change
lookup_table = defaultdict(dict)  # Nested dict: ticker -> date -> stats

for ticker, records in trades_data.items():
    # Convert records to DataFrame
    df_ticker = pd.DataFrame(records)
    # Sort records by date
    df_ticker.sort_values("date", inplace=True)
    df_ticker.set_index("date", inplace=True)

    # Calculate the percentage change in close_price
    df_ticker["price_diff"] = (
        df_ticker["close_price"].pct_change() * 100
    )  # Multiply by 100 for percentage

    # Shift trades to exclude the current day from rolling calculations
    df_ticker["trades_shifted"] = df_ticker["trades"].shift(1)
    # Calculate rolling average and standard deviation over the previous 5 days
    df_ticker["avg_trades"] = df_ticker["trades_shifted"].rolling(window=5).mean()
    df_ticker["std_trades"] = df_ticker["trades_shifted"].rolling(window=5).std()
    # Store the data in the lookup table
    for date, row in df_ticker.iterrows():
        # Convert date to string for JSON serialization
        date_str = date.strftime("%Y-%m-%d")
        # Ensure rolling stats are available
        if pd.notnull(row["avg_trades"]) and pd.notnull(row["std_trades"]):
            lookup_table[ticker][date_str] = {
                "trades": row["trades"],
                "close_price": row["close_price"],
                "price_diff": row["price_diff"],
                "avg_trades": row["avg_trades"],
                "std_trades": row["std_trades"],
            }
        else:
            # Store data without rolling stats if not enough data points
            lookup_table[ticker][date_str] = {
                "trades": row["trades"],
                "close_price": row["close_price"],
                "price_diff": row["price_diff"],
                "avg_trades": None,
                "std_trades": None,
            }

print("Lookup table built successfully.")

# Convert defaultdict to regular dict for JSON serialization
lookup_table = {k: v for k, v in lookup_table.items()}

# Save the lookup table to a JSON file
with open("lookup_table.json", "w") as f:
    json.dump(lookup_table, f, indent=4)

print("Lookup table saved to 'lookup_table.json'.")

# Save the lookup table to a file for later use
with open("lookup_table.pkl", "wb") as f:
    pickle.dump(lookup_table, f)

print("Lookup table saved to 'lookup_table.pkl'.")
