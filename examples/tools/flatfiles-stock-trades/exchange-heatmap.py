# We can use a Python script that aggregates trades by exchange into 30-minute
# chunks, setting the stage for a visual analysis. This approach will highlight
# trade flows, including opening hours and peak activity times, across the
# exchanges. Please see https://polygon.io/blog/insights-from-trade-level-data
#
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pytz  # type: ignore

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
df["time_interval"] = df["participant_timestamp"].dt.floor("30T").dt.time

# Ensure full 24-hour coverage by generating all possible 30-minute intervals
all_intervals = pd.date_range(start="00:00", end="23:59", freq="30T").time
all_exchanges = df["exchange"].unique()
full_index = pd.MultiIndex.from_product(
    [all_exchanges, all_intervals], names=["exchange", "time_interval"]
)

# Group by 'exchange' and 'time_interval', count trades, and reset index
grouped = (
    df.groupby(["exchange", "time_interval"])
    .size()
    .reindex(full_index, fill_value=0)
    .reset_index(name="trade_count")
)

# Pivot the DataFrame for the heatmap, ensuring all intervals and exchanges are represented
pivot_table = grouped.pivot("exchange", "time_interval", "trade_count").fillna(0)

# Apply a log scale transformation to the trade counts + 1 to handle zero trades correctly
log_scale_data = np.log1p(pivot_table.values)

# Plotting the heatmap using the log scale data
plt.figure(figsize=(20, 10))
sns.heatmap(
    log_scale_data,
    annot=False,
    cmap="Reds",
    linewidths=0.5,
    cbar=False,
    xticklabels=[t.strftime("%H:%M") for t in all_intervals],
    yticklabels=pivot_table.index,
)
plt.title("Trade Count Heatmap by Exchange and Time Interval (Log Scale, ET)")
plt.ylabel("Exchange")
plt.xlabel("Time Interval (ET)")
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()
