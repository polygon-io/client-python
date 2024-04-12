# To visualize these dynamics, we can use a Python script to create a histogram
# aggregating trades into 30-minute intervals, providing a clear view of when
# trading activity concentrates during the day. This analysis aims to highlight
# the distribution of trading volume across the day, from pre-market to after-
# hours. Please see https://polygon.io/blog/insights-from-trade-level-data
#
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# Replace '2024-04-05.csv' with the path to your actual file
file_path = "2024-04-05.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Convert 'participant_timestamp' to datetime (assuming nanoseconds Unix timestamp)
df["participant_timestamp"] = pd.to_datetime(
    df["participant_timestamp"], unit="ns", utc=True
)

# Convert to Eastern Time (ET), accounting for both EST and EDT
df["participant_timestamp"] = df["participant_timestamp"].dt.tz_convert(
    "America/New_York"
)

# Create a new column for 30-minute time intervals, now in ET
df["time_interval"] = df["participant_timestamp"].dt.floor("30T")

# Aggregate trades into 30-minute intervals for the entire dataset
trade_counts_per_interval = df.groupby("time_interval").size()

# Prepare the plot
plt.figure(figsize=(15, 7))

# Plotting the histogram/bar chart
bars = plt.bar(
    trade_counts_per_interval.index, trade_counts_per_interval.values, width=0.02
)

# Adding trade count annotations on each bar
for bar in bars:
    height = bar.get_height()
    plt.annotate(
        f"{int(height)}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

plt.title("Trade Counts Aggregated by 30-Minute Intervals (ET)")
plt.xlabel("Time Interval (ET)")
plt.ylabel("Number of Trades")
plt.xticks(rotation=45, ha="right")

# Ensure that every 30-minute interval is represented on the x-axis
plt.gca().set_xticklabels(
    [t.strftime("%Y-%m-%d %H:%M") for t in trade_counts_per_interval.index], rotation=90
)

plt.tight_layout()
plt.show()
