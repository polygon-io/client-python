# 🚀 Fundamentals API Examples

This directory contains comprehensive examples for using Polygon's new Fundamentals API. The new API replaces the deprecated `VXClient` with 6 specialized, high-performance endpoints.

## 📁 Example Files

### 🆕 New Fundamentals API (Recommended)

| File | Description | Level |
|------|-------------|-------|
| `fundamentals_example.py` | **Start here!** Basic usage of all 6 endpoints | Beginner |
| `fundamentals_modifiers_demo.py` | Filter modifiers and parameter examples | Intermediate |
| `fundamentals_advanced_filtering.py` | Advanced screening and analysis strategies | Advanced |

### ⚠️ Legacy Examples (Deprecated)

| File | Description | Status |
|------|-------------|--------|
| `stocks-stock_financials.py` | Old VXClient usage (shows migration) | **DEPRECATED** |
| `financials.py` | Mixed old/new examples | **UPDATED** |

## 🎯 Quick Start

```python
from polygon import RESTClient

client = RESTClient(api_key="your_api_key")

# Balance Sheets - Clean and direct!
balance_sheets = client.list_balance_sheets(tickers="AAPL", limit=5)
for sheet in balance_sheets:
    print(f"Assets: ${sheet.total_assets:,.0f}")

# Financial Ratios with filtering
ratios = client.list_financial_ratios(
    ticker="AAPL", 
    price_to_earnings_lt=20,  # P/E < 20
    limit=5
)
```

## 🔍 Advanced Filtering Examples

The new API supports powerful filtering with these modifiers:

- `.gt` / `.gte` - Greater than / Greater than or equal
- `.lt` / `.lte` - Less than / Less than or equal  
- `.any_of` - Match any of (comma-separated values)
- `.all_of` - Match all of (for arrays)

```python
# Value stock screening
value_stocks = client.list_financial_ratios(
    price_to_earnings_gt=0,      # Positive P/E
    price_to_earnings_lt=15,     # P/E < 15 (undervalued)
    dividend_yield_gt=0.02,      # Dividend yield > 2%
    market_cap_gt=1000000000,    # Market cap > $1B
    limit=20
)

# Multi-ticker analysis
mega_caps = client.list_financial_ratios(
    ticker_any_of="AAPL,GOOGL,MSFT,AMZN,TSLA"
)

# Date range filtering
recent_statements = client.list_income_statements(
    tickers="AAPL",
    period_end_gte="2023-01-01",
    period_end_lt="2024-01-01"
)
```

## 📊 Available Endpoints

| Method | Endpoint | Use Case |
|--------|----------|----------|
| `list_balance_sheets()` | Balance sheet data | Assets, liabilities, equity analysis |
| `list_cash_flow_statements()` | Cash flow data | Operating, investing, financing cash flows |
| `list_income_statements()` | Income statement data | Revenue, expenses, profitability |
| `list_financial_ratios()` | Financial ratios | Valuation, profitability, efficiency metrics |
| `list_short_interest()` | Short interest data | Short squeeze analysis, sentiment |
| `list_short_volume()` | Daily short volume | Short selling activity tracking |

## 🚨 Migration from VXClient

**Before (Deprecated):**
```python
# OLD - Shows deprecation warnings
financials = client.vx.list_stock_financials(ticker="AAPL")
```

**After (Modern):**
```python
# NEW - Fast, focused, and clean
balance_sheets = client.list_balance_sheets(tickers="AAPL")
income_statements = client.list_income_statements(tickers="AAPL")
ratios = client.list_financial_ratios(ticker="AAPL")
```

## 🎓 Learning Path

1. **Start**: Run `fundamentals_example.py` to see basic usage
2. **Learn**: Explore `fundamentals_modifiers_demo.py` for filtering
3. **Master**: Study `fundamentals_advanced_filtering.py` for complex strategies
4. **Migrate**: Check `stocks-stock_financials.py` for migration examples

## 🔗 Resources

- **📖 Documentation**: [Fundamentals API Docs](https://polygon-api-client.readthedocs.io/en/latest/Fundamentals.html)
- **🔄 Migration Guide**: `../FUNDAMENTALS_MIGRATION.md`
- **🏠 Main README**: `../README.md`
- **📊 Live Examples**: All examples work with real API keys

## ⚡ Performance Tips

1. **Use specific filters** to reduce response size
2. **Set appropriate limits** (5-50 for most use cases)
3. **Filter by date** for recent data only
4. **Combine multiple filters** for targeted results
5. **Use `.any_of`** for multi-ticker analysis

## 🛠️ Running Examples

```bash
# Set your API key
export POLYGON_API_KEY="your_api_key_here"

# Run basic examples
python examples/rest/fundamentals_example.py

# Run advanced filtering
python examples/rest/fundamentals_advanced_filtering.py

# Test migration (shows deprecation warnings)
python examples/rest/stocks-stock_financials.py
```

## ✅ Benefits of New API

- 🚀 **Faster**: Smaller, focused responses
- 🎯 **Cleaner**: Dedicated endpoints for each data type  
- 🔍 **Powerful**: Advanced filtering capabilities
- 📝 **Better Docs**: Comprehensive parameter documentation
- 🛡️ **Type Safe**: Better IDE support and error catching
- 🔧 **Maintainable**: Easier to extend and maintain

**Happy coding with the new Fundamentals API! 🎉**