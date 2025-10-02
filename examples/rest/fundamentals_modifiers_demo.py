#!/usr/bin/env python3
"""
Demo of Polygon Fundamentals API Filter Modifiers

This demonstrates the powerful filtering capabilities using the _gt, _gte, _lt, _lte modifiers
that are now available on all fundamentals endpoints, just like the economy API.
"""

from polygon import RESTClient
from datetime import date, timedelta


def demo_filter_modifiers():
    client = RESTClient("dummy_api_key")

    print("🔍 Polygon Fundamentals Filter Modifiers Demo")
    print("=" * 50)

    print("\n📊 1. Balance Sheet Filtering Examples")
    print("-" * 35)
    print("# Get balance sheets from 2023 onwards:")
    print("client.list_balance_sheets(")
    print("    tickers='AAPL',")
    print("    period_end_gte='2023-01-01'")
    print(")")
    print()
    print("# Get balance sheets for a specific fiscal year range:")
    print("client.list_balance_sheets(")
    print("    tickers='AAPL',")
    print("    fiscal_year_gte=2022,")
    print("    fiscal_year_lte=2024")
    print(")")

    print("\n💰 2. Cash Flow Statement Filtering Examples")
    print("-" * 40)
    print("# Get quarterly reports from last year:")
    print("client.list_cash_flow_statements(")
    print("    tickers='MSFT',")
    print("    timeframe='quarterly',")
    print("    period_end_gte='2023-01-01',")
    print("    fiscal_quarter_gte=2")
    print(")")

    print("\n📈 3. Income Statement Filtering Examples")
    print("-" * 38)
    print("# Get annual reports for fiscal years 2022-2024:")
    print("client.list_income_statements(")
    print("    tickers='GOOGL',")
    print("    timeframe='annual',")
    print("    fiscal_year_gte=2022,")
    print("    fiscal_year_lte=2024")
    print(")")

    print("\n📋 4. Financial Ratios Filtering Examples")
    print("-" * 38)
    print("# Find high-value stocks with good ratios:")
    print("client.list_financial_ratios(")
    print("    price_gt=100.0,                    # Stock price > $100")
    print("    market_cap_gte=10000000000,        # Market cap >= $10B")
    print("    price_to_earnings_lt=25.0,         # P/E ratio < 25")
    print("    debt_to_equity_lt=0.5,             # Low debt")
    print("    return_on_equity_gt=0.15           # ROE > 15%")
    print(")")

    print("\n🔻 5. Short Interest Filtering Examples")
    print("-" * 36)
    print("# Find stocks with high short interest:")
    print("client.list_short_interest(")
    print("    days_to_cover_gt=5.0,              # High days to cover")
    print("    settlement_date_gte='2024-01-01',  # Recent data")
    print("    avg_daily_volume_gte=1000000       # High volume stocks")
    print(")")

    print("\n📉 6. Short Volume Filtering Examples")
    print("-" * 34)
    print("# Find high short volume activity:")
    print("client.list_short_volume(")
    print("    date_gte='2024-09-01',             # Recent dates")
    print("    short_volume_ratio_gt=20.0,        # High short %")
    print("    total_volume_gte=5000000           # High volume days")
    print(")")

    print("\n🎯 Key Benefits of Filter Modifiers:")
    print("-" * 36)
    print("✅ Precise date range filtering")
    print("✅ Numeric range queries")
    print("✅ Complex multi-field filtering")
    print("✅ Server-side filtering (better performance)")
    print("✅ Consistent with Polygon's other APIs")

    print("\n🔧 Available Modifiers:")
    print("-" * 21)
    print("• _gt   - Greater than")
    print("• _gte  - Greater than or equal to")
    print("• _lt   - Less than")
    print("• _lte  - Less than or equal to")

    print("\n🌟 This makes the Polygon Fundamentals API incredibly powerful!")
    print("   You can now create sophisticated screening and filtering logic!")


if __name__ == "__main__":
    demo_filter_modifiers()
