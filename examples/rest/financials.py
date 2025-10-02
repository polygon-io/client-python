"""
Modern Fundamentals API Example

This example demonstrates the NEW fundamentals API endpoints.
The old VXClient financials methods are deprecated.

For complete examples, see: fundamentals_example.py
"""

from polygon import RESTClient

client = RESTClient()

# Company details (not part of fundamentals - still works as before)
ticker_details = client.get_ticker_details("NFLX")
print(f"Company: {ticker_details.name} ({ticker_details.ticker})")

# News (not part of fundamentals - still works as before)
print("\nRecent News:")
for i, news in enumerate(client.list_ticker_news("INTC", limit=3)):
    print(f"{i+1}. {news.title}")

print("\n" + "=" * 60)
print("🚀 NEW FUNDAMENTALS API EXAMPLES")
print("=" * 60)

# NEW: Financial Fundamentals using dedicated endpoints
ticker = "NFLX"

print(f"\n📊 Financial Data for {ticker}:")

# Balance Sheets
print("\n1. Balance Sheets (latest 2 quarters):")
for bs in client.list_balance_sheets(tickers=ticker, timeframe="quarterly", limit=2):
    if bs.period_end and bs.total_assets:
        print(f"   {bs.period_end}: Total Assets = ${bs.total_assets:,.0f}")

# Income Statements
print("\n2. Income Statements (latest 2 quarters):")
for inc in client.list_income_statements(tickers=ticker, timeframe="quarterly", limit=2):
    if inc.period_end and inc.revenues:
        print(f"   {inc.period_end}: Revenue = ${inc.revenues:,.0f}")

# Financial Ratios
print("\n3. Financial Ratios (latest data):")
for ratio in client.list_financial_ratios(ticker=ticker, limit=1):
    if ratio.price_to_earnings and ratio.market_cap:
        print(f"   P/E Ratio: {ratio.price_to_earnings:.2f}")
        print(f"   Market Cap: ${ratio.market_cap:,.0f}")

print("\n💡 For complete examples, see: fundamentals_example.py")
print("📖 Migration Guide: FUNDAMENTALS_MIGRATION.md")
