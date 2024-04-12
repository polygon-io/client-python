# Here's a Python script for analyzing the dataset, that identifies the
# distribution of trades across different exchanges and calculates their
# respective percentages of the total trades. Please see
# https://polygon.io/blog/insights-from-trade-level-data
#
import pandas as pd  # type: ignore

# Replace '2024-04-05.csv' with the path to your actual file
file_path = "2024-04-05.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Count the number of trades for each exchange
exchange_counts = df["exchange"].value_counts()

# Calculate the total number of trades
total_trades = exchange_counts.sum()

# Print out all exchanges and their percentage of total trades
for exchange, count in exchange_counts.items():
    percentage = (count / total_trades) * 100
    print(f"Exchange {exchange}: {count} trades, {percentage:.2f}% of total trades")
