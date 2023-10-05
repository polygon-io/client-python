# Mapping Market Movements with Polygon.io and D3.js Treemap

This repository contains code and resources for visualizing stock market data using D3.js Treemap and Polygon.io's API.

## Structure

The repo consists of:

- `polygon_sic_code_data_gatherer.py`: Gathers data using Polygon's APIs and groups them by SIC codes.
- `sic_code_groups.json`: Pre-built JSON file containing grouped ticker to SIC code data.
- `treemap_server.py`: Simple server to host the treemap visualization.

## Getting Started

### Prerequisites

- Python 3.x
- Polygon.io account and API key

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/polygon-io/client-python.git
   ```

2. Install the necessary Python packages. 
   ```
   pip install -U polygon-api-client
   ```

3. Store your Polygon.io API key securely, or set it as an environment variable:
   ```
   export POLYGON_API_KEY=YOUR_API_KEY_HERE
   ```

### Running the Treemap Server

Change into the treemap example directory and execute the `treemap_server.py` script:
```
cd examples/tools/treemap
python3 treemap_server.py
```

Upon successful execution, the server will start, and you can view the treemap visualization by navigating to:
```
http://localhost:8889
```
