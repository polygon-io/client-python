#!/usr/bin/env python3
"""
Advanced Fundamentals API Examples with Filter Modifiers

This example demonstrates the power of the new fundamentals API with:
- Advanced filtering using comparison operators (.gt, .gte, .lt, .lte)
- Multi-value filtering with .any_of and .all_of
- Complex screening strategies
- Performance optimization techniques
- Real-world use cases

The new fundamentals API provides much more flexible filtering than the deprecated VXClient.
"""

import os
from polygon import RESTClient
from datetime import date, timedelta
from typing import List


def screen_value_stocks(client: RESTClient) -> None:
    """Screen for value stocks using financial ratios with multiple filters."""
    print("🔍 SCREENING: Value Stocks (Low P/E, High Dividend Yield)")
    print("-" * 60)

    try:
        # Multi-criteria value stock screening
        value_stocks = client.list_financial_ratios(
            price_to_earnings_gt=0,  # Positive P/E (profitable)
            price_to_earnings_lt=15,  # P/E < 15 (undervalued)
            dividend_yield_gt=0.02,  # Dividend yield > 2%
            market_cap_gt=1000000000,  # Market cap > $1B (stability)
            price_to_book_lt=3,  # P/B < 3 (reasonable book value)
            debt_to_equity_lt=0.5,  # Low debt ratio
            limit=10,
        )

        print("Found value stock candidates:")
        for stock in value_stocks:
            if all([stock.ticker, stock.price_to_earnings, stock.dividend_yield, stock.market_cap]):
                print(
                    f"  {stock.ticker:6} | P/E: {stock.price_to_earnings:5.1f} | "
                    f"Div Yield: {stock.dividend_yield:.1%} | "
                    f"Market Cap: ${stock.market_cap/1e9:.1f}B"
                )

    except Exception as e:
        print(f"Error in value stock screening: {e}")


def analyze_mega_caps(client: RESTClient) -> None:
    """Analyze mega-cap stocks using ticker filtering."""
    print("\n📊 ANALYSIS: Mega-Cap Tech Stocks Financial Health")
    print("-" * 60)

    mega_caps = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA"]

    try:
        # Get latest financial ratios for mega-caps using any_of filter
        ratios = client.list_financial_ratios(ticker_any_of=",".join(mega_caps), limit=len(mega_caps))

        print("Current Financial Health Metrics:")
        print(f"{'Ticker':<6} {'P/E':<6} {'ROE':<8} {'ROA':<8} {'Debt/Eq':<8} {'Market Cap'}")
        print("-" * 70)

        for ratio in ratios:
            if ratio.ticker:
                pe = f"{ratio.price_to_earnings:.1f}" if ratio.price_to_earnings else "N/A"
                roe = f"{ratio.return_on_equity:.1%}" if ratio.return_on_equity else "N/A"
                roa = f"{ratio.return_on_assets:.1%}" if ratio.return_on_assets else "N/A"
                debt_eq = f"{ratio.debt_to_equity:.2f}" if ratio.debt_to_equity else "N/A"
                mcap = f"${ratio.market_cap/1e9:.0f}B" if ratio.market_cap else "N/A"

                print(f"{ratio.ticker:<6} {pe:<6} {roe:<8} {roa:<8} {debt_eq:<8} {mcap}")

    except Exception as e:
        print(f"Error analyzing mega-caps: {e}")


def track_quarterly_growth(client: RESTClient, ticker: str = "AAPL") -> None:
    """Track quarterly revenue and income growth using date filtering."""
    print(f"\n📈 GROWTH TRACKING: {ticker} Quarterly Performance (Last 8 Quarters)")
    print("-" * 70)

    try:
        # Get last 8 quarters of income statements
        income_statements = client.list_income_statements(
            tickers=ticker, timeframe="quarterly", period_end_gte="2022-01-01", limit=8  # From 2022 onwards
        )

        statements = list(income_statements)
        if not statements:
            print(f"No income statements found for {ticker}")
            return

        print(f"{'Period':<12} {'Revenue':<15} {'Revenue Growth':<15} {'Net Income':<15} {'EPS'}")
        print("-" * 80)

        prev_revenue = None
        for stmt in reversed(statements[-8:]):  # Most recent 8 quarters
            if stmt.period_end and stmt.revenues:
                revenue = stmt.revenues
                revenue_growth = ""
                if prev_revenue:
                    growth = ((revenue - prev_revenue) / prev_revenue) * 100
                    revenue_growth = f"{growth:+.1f}%"

                net_income = f"${stmt.net_income_loss/1e6:.0f}M" if stmt.net_income_loss else "N/A"
                eps = f"${stmt.basic_earnings_per_share:.2f}" if stmt.basic_earnings_per_share else "N/A"

                print(f"{stmt.period_end} ${revenue/1e9:8.1f}B {revenue_growth:>12} {net_income:>12} {eps:>8}")
                prev_revenue = revenue

    except Exception as e:
        print(f"Error tracking growth for {ticker}: {e}")


def monitor_short_squeeze_candidates(client: RESTClient) -> None:
    """Find potential short squeeze candidates using short interest data."""
    print("\n🎯 SHORT SQUEEZE MONITORING: High Short Interest Stocks")
    print("-" * 60)

    try:
        # Look for stocks with high days-to-cover (potential squeeze candidates)
        short_interest = client.list_short_interest(
            days_to_cover_gt=7,  # Days to cover > 7 (high squeeze potential)
            avg_daily_volume_gt=1000000,  # Decent volume > 1M shares/day
            settlement_date_gte="2024-01-01",  # Recent data
            limit=15,
        )

        print("Potential Short Squeeze Candidates:")
        print(f"{'Ticker':<8} {'Days to Cover':<15} {'Short Interest':<15} {'Avg Volume':<12} {'Date'}")
        print("-" * 75)

        for si in short_interest:
            if si.ticker and si.days_to_cover:
                short_int = f"{si.short_interest:,}" if si.short_interest else "N/A"
                avg_vol = f"{si.avg_daily_volume:,}" if si.avg_daily_volume else "N/A"

                print(f"{si.ticker:<8} {si.days_to_cover:<15.1f} {short_int:<15} {avg_vol:<12} {si.settlement_date}")

    except Exception as e:
        print(f"Error monitoring short squeeze candidates: {e}")


def analyze_balance_sheet_strength(client: RESTClient) -> None:
    """Analyze balance sheet strength using asset and liability filters."""
    print("\n💪 BALANCE SHEET ANALYSIS: Strong Financial Position")
    print("-" * 60)

    try:
        # Find companies with strong balance sheets
        balance_sheets = client.list_balance_sheets(
            tickers_any_of="AAPL,GOOGL,MSFT,BRK.A,JNJ",  # Blue chip companies
            timeframe="annual",
            period_end_gte="2023-01-01",  # Recent data
            total_assets_gt=100000000000,  # Assets > $100B
            limit=10,
        )

        print("Strong Balance Sheet Companies:")
        print(f"{'Ticker':<8} {'Period':<12} {'Total Assets':<15} {'Cash & Equiv':<15} {'Total Debt'}")
        print("-" * 75)

        for bs in balance_sheets:
            if bs.tickers and bs.period_end:
                ticker = bs.tickers[0] if bs.tickers else "N/A"
                assets = f"${bs.total_assets/1e9:.0f}B" if bs.total_assets else "N/A"
                cash = f"${bs.cash_and_cash_equivalents/1e9:.0f}B" if bs.cash_and_cash_equivalents else "N/A"
                debt = f"${bs.current_debt/1e9:.0f}B" if bs.current_debt else "N/A"

                print(f"{ticker:<8} {bs.period_end} {assets:<15} {cash:<15} {debt}")

    except Exception as e:
        print(f"Error analyzing balance sheets: {e}")


def demonstrate_performance_tips(client: RESTClient) -> None:
    """Demonstrate performance optimization techniques."""
    print("\n⚡ PERFORMANCE TIPS & BEST PRACTICES")
    print("-" * 60)

    print("1. Use specific filters to reduce response size:")
    print("   ✅ client.list_financial_ratios(ticker='AAPL', limit=5)")
    print("   ❌ client.list_financial_ratios()  # Returns too much data")

    print("\n2. Use appropriate limits:")
    print("   ✅ limit=50 for screening, limit=5 for specific analysis")

    print("\n3. Use date filters for recent data:")
    print("   ✅ period_end_gte='2023-01-01' for recent data only")

    print("\n4. Combine filters for targeted results:")
    print("   ✅ Multiple criteria reduce API calls and processing time")

    print("\n5. Cache results when possible:")
    print("   ✅ Store results locally for repeated analysis")


def main():
    """Run all advanced fundamentals examples."""
    # Initialize client
    client = RESTClient()

    print("🚀 ADVANCED FUNDAMENTALS API EXAMPLES")
    print("=" * 60)
    print("💡 Using powerful filter modifiers for sophisticated analysis")
    print()

    # Run all examples
    screen_value_stocks(client)
    analyze_mega_caps(client)
    track_quarterly_growth(client, "AAPL")
    monitor_short_squeeze_candidates(client)
    analyze_balance_sheet_strength(client)
    demonstrate_performance_tips(client)

    print(f"\n{'='*60}")
    print("✅ All examples completed!")
    print("📖 For more examples, see: fundamentals_example.py")
    print("🔗 Migration guide: FUNDAMENTALS_MIGRATION.md")
    print("📚 Documentation: https://polygon-api-client.readthedocs.io/")


if __name__ == "__main__":
    main()
