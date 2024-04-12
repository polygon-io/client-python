# Here's a Python script for analyzing the dataset, that identifies the top 10
# most traded stocks and calculates their respective percentages of the total
# trades. Please see https://polygon.io/blog/insights-from-trade-level-data
#
import pandas as pd  # type: ignore

# Replace '2024-04-05.csv' with the path to your actual file
file_path = "2024-04-05.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Count the number of trades for each ticker
trade_counts = df["ticker"].value_counts()

# Calculate the total number of trades
total_trades = trade_counts.sum()

# Get the top 10 traded stocks
top_10_traded = trade_counts.head(10)

# Print out the top 10 traded stocks and their percentage of total trades
for ticker, count in top_10_traded.items():
    percentage = (count / total_trades) * 100
    print(f"{ticker}: {count} trades, {percentage:.2f}% of total trades")
