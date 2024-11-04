# Hunting Anomalies in the Stock Market

This repository contains all the necessary scripts and data directories used in the [Hunting Anomalies in the Stock Market](https://polygon.io/blog/hunting-anomalies-in-stock-market/) tutorial, hosted on Polygon.io's blog. The tutorial demonstrates how to detect statistical anomalies in historical US stock market data through a comprehensive workflow that involves downloading data, building a lookup table, querying for anomalies, and visualizing them through a web interface.

### Prerequisites

- Python 3.8+
- Access to Polygon.io's historical data via Flat Files
- An active Polygon.io API key, obtainable by signing up for a Stocks paid plan

### Repository Contents

- `README.md`: This file, outlining setup and execution instructions.
- `aggregates_day`: Directory where downloaded CSV data files are stored.
- `build-lookup-table.py`: Python script to build a lookup table from the historical data.
- `query-lookup-table.py`: Python script to query the lookup table for anomalies.
- `gui-lookup-table.py`: Python script for a browser-based interface to explore anomalies visually.

### Running the Tutorial

1. **Ensure Python 3.8+ is installed:** Check your Python version and ensure all required libraries (polygon-api-client, pandas, pickle, and argparse) are installed.

2. **Set up your API key:** Make sure you have an active paid Polygon.io Stock subscription for accessing Flat Files. Set up your API key in your environment or directly in the scripts where required.

3. **Download Historical Data:** Use the MinIO client to download historical stock market data:
   ```bash
   mc alias set s3polygon https://files.polygon.io YOUR_ACCESS_KEY YOUR_SECRET_KEY
   mc cp --recursive s3polygon/flatfiles/us_stocks_sip/day_aggs_v1/2024/08/ ./aggregates_day/
   mc cp --recursive s3polygon/flatfiles/us_stocks_sip/day_aggs_v1/2024/09/ ./aggregates_day/
   mc cp --recursive s3polygon/flatfiles/us_stocks_sip/day_aggs_v1/2024/10/ ./aggregates_day/
   gunzip ./aggregates_day/*.gz
   ```
   Adjust the commands and paths based on the data you're interested in.

4. **Build the Lookup Table:** This script processes the downloaded data and builds a lookup table, saving it as `lookup_table.pkl`.
   ```bash
   python build-lookup-table.py
   ```

5. **Query Anomalies:** Replace `2024-10-18` with the date you want to analyze for anomalies.
   ```bash
   python query-lookup-table.py 2024-10-18
   ```

6. **Run the GUI:** Access the web interface at `http://localhost:8888` to explore the anomalies visually.
   ```bash
   python gui-lookup-table.py
   ```

For a complete step-by-step guide on each phase of the anomaly detection process, including additional configurations and troubleshooting, refer to the detailed [tutorial on our blog](https://polygon.io/blog/hunting-anomalies-in-stock-market).
