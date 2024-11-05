import pickle
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Anomaly Detection Script")
parser.add_argument("date", type=str, help="Target date in YYYY-MM-DD format")
args = parser.parse_args()

# Load the lookup_table
with open("lookup_table.pkl", "rb") as f:
    lookup_table = pickle.load(f)

# Threshold for considering an anomaly (e.g., 3 standard deviations)
threshold_multiplier = 3

# Date for which we want to find anomalies
target_date_str = args.date

# List to store anomalies
anomalies = []

# Iterate over all tickers in the lookup table
for ticker, date_data in lookup_table.items():
    if target_date_str in date_data:
        data = date_data[target_date_str]
        trades = data["trades"]
        avg_trades = data["avg_trades"]
        std_trades = data["std_trades"]
        if avg_trades is not None and std_trades is not None and std_trades > 0:
            z_score = (trades - avg_trades) / std_trades
            if z_score > threshold_multiplier:
                anomalies.append(
                    {
                        "ticker": ticker,
                        "date": target_date_str,
                        "trades": trades,
                        "avg_trades": avg_trades,
                        "std_trades": std_trades,
                        "z_score": z_score,
                        "close_price": data["close_price"],
                        "price_diff": data["price_diff"],
                    }
                )

# Sort anomalies by trades in descending order
anomalies.sort(key=lambda x: x["trades"], reverse=True)

# Print the anomalies with aligned columns
print(f"\nAnomalies Found for {target_date_str}:\n")
print(
    f"{'Ticker':<10}{'Trades':>10}{'Avg Trades':>15}{'Std Dev':>10}{'Z-score':>10}{'Close Price':>12}{'Price Diff':>12}"
)
print("-" * 91)
for anomaly in anomalies:
    print(
        f"{anomaly['ticker']:<10}"
        f"{anomaly['trades']:>10.0f}"
        f"{anomaly['avg_trades']:>15.2f}"
        f"{anomaly['std_trades']:>10.2f}"
        f"{anomaly['z_score']:>10.2f}"
        f"{anomaly['close_price']:>12.2f}"
        f"{anomaly['price_diff']:>12.2f}"
    )
