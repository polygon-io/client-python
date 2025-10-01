#!/usr/bin/env python3
"""
Example usage of the new Polygon Fundamentals API endpoints.

This example demonstrates how to use all 6 new fundamentals endpoints:
1. Balance Sheets
2. Cash Flow Statements
3. Income Statements
4. Financial Ratios
5. Short Interest
6. Short Volume

The new fundamentals client replaces the deprecated VXClient.
"""

import os
from polygon import RESTClient
from datetime import date, timedelta


def main():
    # Initialize the client
    # You can set your API key in environment variable POLYGON_API_KEY
    # or pass it directly: RESTClient(api_key="your_api_key")
    client = RESTClient()

    # Example ticker
    ticker = "AAPL"

    print("🚀 Polygon Fundamentals API Examples")
    print("=" * 50)
    print("💡 Note: All methods are available directly on client - clean & simple!")
    print()

    # 1. Balance Sheets
    print("\n📊 1. Balance Sheets")
    print("-" * 20)
    try:
        balance_sheets = client.list_balance_sheets(tickers=ticker, timeframe="quarterly", limit=5)
        for bs in balance_sheets:
            if bs.period_end and bs.total_assets:
                print(f"Period: {bs.period_end}, Total Assets: ${bs.total_assets:,.0f}")
    except Exception as e:
        print(f"Error fetching balance sheets: {e}")

    # 2. Cash Flow Statements
    print("\n💰 2. Cash Flow Statements")
    print("-" * 25)
    try:
        cash_flows = client.list_cash_flow_statements(tickers=ticker, timeframe="quarterly", limit=5)
        for cf in cash_flows:
            if cf.period_end and cf.net_cash_from_operating_activities:
                print(f"Period: {cf.period_end}, Operating Cash Flow: ${cf.net_cash_from_operating_activities:,.0f}")
    except Exception as e:
        print(f"Error fetching cash flow statements: {e}")

    # 3. Income Statements
    print("\n📈 3. Income Statements")
    print("-" * 20)
    try:
        income_statements = client.list_income_statements(tickers=ticker, timeframe="quarterly", limit=5)
        for inc in income_statements:
            if inc.period_end and inc.revenue:
                print(f"Period: {inc.period_end}, Revenue: ${inc.revenue:,.0f}")
    except Exception as e:
        print(f"Error fetching income statements: {e}")

    # 4. Financial Ratios
    print("\n📋 4. Financial Ratios")
    print("-" * 18)
    try:
        ratios = client.list_financial_ratios(ticker=ticker, limit=5)
        for ratio in ratios:
            if ratio.date:
                print(f"Date: {ratio.date}")
                if ratio.price_to_earnings:
                    print(f"  P/E Ratio: {ratio.price_to_earnings:.2f}")
                if ratio.price_to_book:
                    print(f"  P/B Ratio: {ratio.price_to_book:.2f}")
                if ratio.debt_to_equity:
                    print(f"  Debt/Equity: {ratio.debt_to_equity:.2f}")
                break
    except Exception as e:
        print(f"Error fetching financial ratios: {e}")

    # 5. Short Interest
    print("\n🔻 5. Short Interest")
    print("-" * 17)
    try:
        short_interest = client.list_short_interest(ticker=ticker, limit=5)
        for si in short_interest:
            if si.settlement_date and si.short_interest:
                print(f"Settlement: {si.settlement_date}, Short Interest: {si.short_interest:,} shares")
                if si.days_to_cover:
                    print(f"  Days to Cover: {si.days_to_cover:.1f}")
    except Exception as e:
        print(f"Error fetching short interest: {e}")

    # 6. Short Volume
    print("\n📉 6. Short Volume")
    print("-" * 15)
    try:
        # Get data from last week
        last_week = date.today() - timedelta(days=7)
        short_volumes = client.list_short_volume(ticker=ticker, date=last_week.strftime("%Y-%m-%d"), limit=5)
        for sv in short_volumes:
            if sv.date and sv.short_volume:
                print(f"Date: {sv.date}, Short Volume: {sv.short_volume:,}")
                if sv.short_volume_ratio:
                    print(f"  Short Volume Ratio: {sv.short_volume_ratio:.1f}%")
    except Exception as e:
        print(f"Error fetching short volume: {e}")

    print("\n✅ Example completed!")
    print("\nNote: The old VXClient (client.vx) is deprecated.")
    print("Use the new direct methods: client.list_balance_sheets(), etc.")


if __name__ == "__main__":
    main()
