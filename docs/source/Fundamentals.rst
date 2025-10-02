Fundamentals
============

.. currentmodule:: polygon

The Fundamentals API provides access to comprehensive financial data for public companies through 6 specialized endpoints. This modern API replaces the deprecated ``VXClient`` with focused, high-performance endpoints for specific data types.

.. note::
   **🚨 Migration Notice**: The old ``client.vx.list_stock_financials()`` method is deprecated. 
   Use the new dedicated endpoints listed below for better performance and cleaner data access.

Quick Start
-----------

.. code-block:: python

   from polygon import RESTClient
   
   client = RESTClient(api_key="your_api_key")
   
   # Get balance sheets - clean and direct!
   balance_sheets = client.list_balance_sheets(tickers="AAPL", timeframe="quarterly", limit=5)
   for sheet in balance_sheets:
       print(f"Period: {sheet.period_end}, Assets: ${sheet.total_assets:,.0f}")

Available Endpoints
-------------------

The fundamentals API consists of 6 specialized endpoints:

1. **Balance Sheets** - :meth:`RESTClient.list_balance_sheets`
2. **Cash Flow Statements** - :meth:`RESTClient.list_cash_flow_statements`  
3. **Income Statements** - :meth:`RESTClient.list_income_statements`
4. **Financial Ratios** - :meth:`RESTClient.list_financial_ratios`
5. **Short Interest** - :meth:`RESTClient.list_short_interest`
6. **Short Volume** - :meth:`RESTClient.list_short_volume`

Balance Sheets
--------------

.. automethod:: RESTClient.list_balance_sheets

**Example:**

.. code-block:: python

   # Get quarterly balance sheets for Apple from 2023 onwards
   balance_sheets = client.list_balance_sheets(
       tickers="AAPL",
       timeframe="quarterly", 
       period_end_gte="2023-01-01",
       limit=8
   )
   
   for sheet in balance_sheets:
       print(f"Q{sheet.fiscal_quarter} {sheet.fiscal_year}: ${sheet.total_assets:,.0f} total assets")

Cash Flow Statements
--------------------

.. automethod:: RESTClient.list_cash_flow_statements

**Example:**

.. code-block:: python

   # Get annual cash flow statements for multiple companies
   cash_flows = client.list_cash_flow_statements(
       tickers_any_of="AAPL,GOOGL,MSFT",
       timeframe="annual",
       limit=10
   )
   
   for cf in cash_flows:
       if cf.net_cash_flow_from_operating_activities:
           print(f"{cf.tickers[0]} {cf.fiscal_year}: Operating CF = ${cf.net_cash_flow_from_operating_activities:,.0f}")

Income Statements  
-----------------

.. automethod:: RESTClient.list_income_statements

**Example:**

.. code-block:: python

   # Get income statements with revenue filtering
   income_statements = client.list_income_statements(
       tickers="TSLA",
       timeframe="quarterly",
       revenues_gt=10000000000,  # Revenue > $10B
       limit=5
   )
   
   for stmt in income_statements:
       print(f"Q{stmt.fiscal_quarter} {stmt.fiscal_year}: Revenue ${stmt.revenues:,.0f}, Net Income ${stmt.net_income_loss:,.0f}")

Financial Ratios
----------------

.. automethod:: RESTClient.list_financial_ratios

**Example:**

.. code-block:: python

   # Find stocks with low P/E ratios and high market cap
   ratios = client.list_financial_ratios(
       price_to_earnings_lt=15,     # P/E < 15
       market_cap_gt=50000000000,   # Market cap > $50B
       limit=20
   )
   
   for ratio in ratios:
       print(f"{ratio.ticker}: P/E = {ratio.price_to_earnings:.2f}, Market Cap = ${ratio.market_cap:,.0f}")

Short Interest
--------------

.. automethod:: RESTClient.list_short_interest

**Example:**

.. code-block:: python

   # Get short interest data with high days-to-cover
   short_interest = client.list_short_interest(
       ticker_any_of="GME,AMC,BBBY",
       days_to_cover_gt=5,  # High short squeeze potential
       limit=10
   )
   
   for si in short_interest:
       print(f"{si.ticker} ({si.settlement_date}): {si.short_interest:,} shares, {si.days_to_cover:.1f} days to cover")

Short Volume
------------

.. automethod:: RESTClient.list_short_volume  

**Example:**

.. code-block:: python

   # Analyze recent short volume patterns
   from datetime import date, timedelta
   
   recent_date = date.today() - timedelta(days=7)
   short_volume = client.list_short_volume(
       ticker="AAPL",
       date_gte=recent_date,
       short_volume_ratio_gt=0.4,  # High short ratio
       limit=10
   )
   
   for sv in short_volume:
       print(f"{sv.date}: {sv.short_volume_ratio:.1%} short ratio ({sv.short_volume:,} of {sv.total_volume:,} shares)")

Filter Modifiers
----------------

All fundamentals endpoints support advanced filtering with these modifiers:

* ``.gt`` - Greater than
* ``.gte`` - Greater than or equal to  
* ``.lt`` - Less than
* ``.lte`` - Less than or equal to
* ``.any_of`` - Equals any of (comma-separated values)
* ``.all_of`` - Contains all of (comma-separated values, for arrays)

**Examples:**

.. code-block:: python

   # Multiple filter examples
   
   # Date range filtering
   balance_sheets = client.list_balance_sheets(
       tickers="AAPL",
       period_end_gte="2023-01-01",
       period_end_lt="2024-01-01"
   )
   
   # Multiple tickers with any_of
   ratios = client.list_financial_ratios(
       ticker_any_of="AAPL,GOOGL,MSFT,AMZN,TSLA"
   )
   
   # Numeric range filtering  
   high_growth = client.list_income_statements(
       revenues_gt=1000000000,     # Revenue > $1B
       fiscal_year_gte=2022        # 2022 onwards
   )

Migration from VXClient
-----------------------

If you're migrating from the old ``VXClient``, here's the mapping:

.. list-table:: Migration Guide
   :widths: 50 50
   :header-rows: 1

   * - Old (Deprecated)
     - New (Recommended)
   * - ``client.vx.list_stock_financials()``
     - Use 6 specific methods based on data needed
   * - Single complex endpoint
     - Dedicated optimized endpoints
   * - Mixed data types in response
     - Clean, focused response models

**Before (Deprecated):**

.. code-block:: python

   # OLD - Shows deprecation warnings
   financials = client.vx.list_stock_financials(ticker="AAPL")

**After (Modern):**

.. code-block:: python

   # NEW - Clean, fast, and focused
   balance_sheets = client.list_balance_sheets(tickers="AAPL")
   income_statements = client.list_income_statements(tickers="AAPL") 
   ratios = client.list_financial_ratios(ticker="AAPL")

Benefits of New API
-------------------

✅ **Performance**: Smaller, focused responses load faster

✅ **Clarity**: Each endpoint returns exactly what you need

✅ **Features**: Better filtering, TTM data support, cleaner models

✅ **Type Safety**: Better IDE support and error catching

✅ **Maintenance**: Easier to extend and maintain

✅ **Documentation**: Comprehensive parameter documentation

Error Handling
--------------

All fundamentals methods use the same error handling patterns as other REST client methods:

.. code-block:: python

   try:
       balance_sheets = client.list_balance_sheets(tickers="INVALID")
       for sheet in balance_sheets:
           print(sheet)
   except Exception as e:
       print(f"Error: {e}")

For more examples, see the `examples/rest/fundamentals_example.py <https://github.com/polygon-io/client-python/blob/master/examples/rest/fundamentals_example.py>`_ file.