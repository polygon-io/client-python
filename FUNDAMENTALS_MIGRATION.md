# Fundamentals API Migration Guide

## 🚨 Important Changes

The single `/vX/reference/financials` endpoint has been **deprecated** and replaced with 6 specialized endpoints for better performance and more focused data access.

### What's Changed

| Old (Deprecated) | New (Recommended) |
|------------------|-------------------|
| `client.vx.list_stock_financials()` | **6 separate methods** (see below) |
| Single endpoint with complex filtering | Dedicated endpoints optimized for specific data types |
| Complex response structure | Streamlined, focused response models |

### New Fundamentals Endpoints

1. **Balance Sheets** → `client.list_balance_sheets()`
2. **Cash Flow Statements** → `client.list_cash_flow_statements()`
3. **Income Statements** → `client.list_income_statements()`
4. **Financial Ratios** → `client.list_financial_ratios()`
5. **Short Interest** → `client.list_short_interest()`
6. **Short Volume** → `client.list_short_volume()`

## Migration Examples

### Before (Deprecated)
```python
from polygon import RESTClient

client = RESTClient(api_key="your_api_key")

# Old way - deprecated
financials = client.vx.list_stock_financials(
    ticker="AAPL",
    timeframe="quarterly",
    limit=10
)
```

### After (New)
### After (New)

```python
from polygon import RESTClient

client = RESTClient(api_key="your_api_key")

# New way - methods available directly on client (recommended)
balance_sheets = client.list_balance_sheets(
    tickers="AAPL",
    timeframe="quarterly", 
    limit=10
)

# Get cash flow statements
cash_flows = client.list_cash_flow_statements(
    tickers="AAPL",
    timeframe="quarterly",
    limit=10
)

# Get income statements  
income_statements = client.list_income_statements(
    tickers="AAPL",
    timeframe="quarterly",
    limit=10
)

# Get financial ratios
ratios = client.list_financial_ratios(
    ticker="AAPL",
    limit=10
)

# Get short interest data
short_interest = client.list_short_interest(
    ticker="AAPL",
    limit=10
)

# Get short volume data
short_volume = client.list_short_volume(
    ticker="AAPL",
    limit=10
)

# Clean, direct access with powerful filter modifiers!

# Example with filter modifiers
balance_sheets = client.list_balance_sheets(
    tickers="AAPL",
    period_end_gte="2023-01-01",  # From 2023 onwards
    fiscal_year_lte=2024          # Up to 2024
)

# Advanced filtering for financial ratios
ratios = client.list_financial_ratios(
    price_gt=100.0,              # Stock price > $100
    market_cap_gte=10000000000,  # Market cap >= $10B
    price_to_earnings_lt=25.0    # P/E ratio < 25
)

## Key Benefits of New API

### 1. **Better Performance**
- Smaller, focused responses
- Faster query times
- Reduced bandwidth usage

### 2. **Cleaner Data Models**
- Each endpoint has its own optimized model
- No more complex nested structures
- Better type safety and IDE support

### 3. **More Specific Filtering**
- Tailored query parameters for each data type
- Better filtering capabilities
- More intuitive parameter names

### 4. **Enhanced Features**
- Support for Trailing Twelve Months (TTM) data
- Better date range filtering
- More comprehensive ratio calculations

## Query Parameters

### Common Parameters (most endpoints)
- `cik` - Central Index Key (CIK)
- `tickers` - Ticker symbol(s)
- `period_end` - Reporting period end date (YYYY-MM-DD)
- `fiscal_year` - Fiscal year
- `fiscal_quarter` - Fiscal quarter (1, 2, 3, or 4)
- `timeframe` - Period type: "quarterly", "annual", "trailing_twelve_months"
- `limit` - Number of results (default: 100, max: 50,000)
- `sort` - Sort field and direction

### Ratios-Specific Parameters
- `ticker` - Stock ticker (required for ratios)
- `price` - Stock price filter
- `market_cap` - Market capitalization filter
- `price_to_earnings` - P/E ratio filter
- And many more financial metrics...

### Short Interest/Volume Parameters
- `ticker` - Stock ticker
- `settlement_date` / `date` - Specific dates
- Volume and ratio-specific filters

## Response Models

### Balance Sheet Fields
- `total_assets`, `total_liabilities`, `total_equity`
- `cash_and_equivalents`, `receivables`, `inventories`
- `long_term_debt_and_capital_lease_obligations`
- And more...

### Cash Flow Fields
- `net_cash_from_operating_activities`
- `net_cash_from_investing_activities` 
- `net_cash_from_financing_activities`
- `change_in_cash_and_equivalents`
- And more...

### Income Statement Fields
- `revenue`, `cost_of_revenue`, `gross_profit`
- `operating_income`, `net_income_loss_attributable_common_shareholders`
- `basic_earnings_per_share`, `diluted_earnings_per_share`
- And more...

### Financial Ratios Fields
- `price_to_earnings`, `price_to_book`, `price_to_sales`
- `debt_to_equity`, `current_ratio`, `quick_ratio`
- `return_on_assets`, `return_on_equity`
- `enterprise_value`, `ev_to_ebitda`
- And more...

### Short Interest Fields
- `short_interest` - Total shares sold short
- `avg_daily_volume` - Average daily trading volume
- `days_to_cover` - Estimated days to cover positions

### Short Volume Fields
- `short_volume` - Daily short sale volume
- `total_volume` - Total daily volume
- `short_volume_ratio` - Percentage short sold
- Exchange-specific volume breakdowns

## Complete Example

See `examples/rest/fundamentals_example.py` for a comprehensive example showing all endpoints.

## Backward Compatibility

The old `VXClient` is still available for backward compatibility but will show deprecation warnings:

```python
# Still works but shows warnings
financials = client.vx.list_stock_financials(ticker="AAPL")
```

**Migration Timeline:**
- ✅ **Now**: New fundamentals API available
- ⚠️ **Current**: Old API deprecated with warnings  
- 🚫 **Future**: Old API will be removed

## Need Help?

- Check `examples/rest/fundamentals_example.py` for usage examples
- Review the API documentation at https://polygon.io/docs/
- All new endpoints follow the same patterns as existing Polygon APIs

---

**Ready to migrate?** Start with one endpoint at a time and gradually move all your code to the new fundamentals API! 🚀