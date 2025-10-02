"""
⚠️  DEPRECATED EXAMPLE - For Migration Reference Only

This example shows the OLD (deprecated) way of accessing financial data.
The VXClient and list_stock_financials method are deprecated.

👉 NEW WAY: Use the dedicated fundamentals endpoints instead!
See: examples/rest/fundamentals_example.py for modern usage.

Migration Guide: https://github.com/polygon-io/client-python/blob/master/FUNDAMENTALS_MIGRATION.md
"""

from polygon import RESTClient
import warnings

# Show deprecation warnings
warnings.simplefilter("always", DeprecationWarning)

# docs (DEPRECATED)
# https://polygon.io/docs/stocks/get_vx_reference_financials
# https://polygon-api-client.readthedocs.io/en/latest/vX.html#list-stock-financials

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

print("🚨 Using DEPRECATED API - This will show deprecation warnings")
print("👉 NEW WAY: Use client.list_balance_sheets(), client.list_income_statements(), etc.")
print("📖 See examples/rest/fundamentals_example.py for modern usage\n")

# OLD WAY (DEPRECATED) - This will show deprecation warnings
financials = []
for f in client.vx.list_stock_financials("AAPL", filing_date="2024-11-01"):
    financials.append(f)

    # get diluted_earnings_per_share
    # print(f.financials.income_statement.diluted_earnings_per_share)

    # get net_income_loss
    # print(f.financials.income_statement.net_income_loss)

print(f"Found {len(financials)} financial records (using deprecated API)")

print("\n" + "=" * 60)
print("🚀 MODERN WAY - Recommended for new code:")
print("=" * 60)

# NEW WAY (RECOMMENDED)
print("\n📊 Balance Sheets:")
balance_sheets = list(client.list_balance_sheets(tickers="AAPL", limit=2))
for bs in balance_sheets:
    if bs.period_end and bs.total_assets:
        print(f"  Period: {bs.period_end}, Total Assets: ${bs.total_assets:,.0f}")

print("\n💰 Income Statements:")
income_statements = list(client.list_income_statements(tickers="AAPL", limit=2))
for inc in income_statements:
    if inc.period_end and inc.revenues:
        print(f"  Period: {inc.period_end}, Revenue: ${inc.revenues:,.0f}")

print("\n📈 Financial Ratios:")
ratios = list(client.list_financial_ratios(ticker="AAPL", limit=2))
for ratio in ratios:
    if ratio.price_to_earnings:
        print(f"  P/E Ratio: {ratio.price_to_earnings:.2f}")

print("\nℹ️  See examples/rest/fundamentals_example.py for complete examples!")
print("📖 Migration Guide: FUNDAMENTALS_MIGRATION.md")
