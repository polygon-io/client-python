from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from ...modelclass import modelclass


@modelclass
@dataclass
class BalanceSheet:
    """Represents a balance sheet record from the new /stocks/financials/v1/balance-sheets endpoint."""

    accounts_payable: Optional[float] = None
    accrued_and_other_current_liabilities: Optional[float] = None
    accumulated_other_comprehensive_income: Optional[float] = None
    additional_paid_in_capital: Optional[float] = None
    cash_and_equivalents: Optional[float] = None
    cik: Optional[str] = None
    commitments_and_contingencies: Optional[float] = None
    common_stock: Optional[float] = None
    debt_current: Optional[float] = None
    deferred_revenue_current: Optional[float] = None
    fiscal_quarter: Optional[int] = None
    fiscal_year: Optional[int] = None
    goodwill: Optional[float] = None
    intangible_assets_net: Optional[float] = None
    inventories: Optional[float] = None
    long_term_debt_and_capital_lease_obligations: Optional[float] = None
    noncontrolling_interest: Optional[float] = None
    other_assets: Optional[float] = None
    other_current_assets: Optional[float] = None
    other_equity: Optional[float] = None
    other_noncurrent_liabilities: Optional[float] = None
    period_end: Optional[str] = None
    preferred_stock: Optional[float] = None
    property_plant_equipment_net: Optional[float] = None
    receivables: Optional[float] = None
    retained_earnings_deficit: Optional[float] = None
    short_term_investments: Optional[float] = None
    tickers: Optional[List[str]] = None
    timeframe: Optional[str] = None
    total_assets: Optional[float] = None
    total_current_assets: Optional[float] = None
    total_current_liabilities: Optional[float] = None
    total_equity: Optional[float] = None
    total_equity_attributable_to_parent: Optional[float] = None
    total_liabilities: Optional[float] = None
    total_liabilities_and_equity: Optional[float] = None
    treasury_stock: Optional[float] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "BalanceSheet":
        if not d:
            return BalanceSheet()
        return BalanceSheet(
            accounts_payable=d.get("accounts_payable"),
            accrued_and_other_current_liabilities=d.get("accrued_and_other_current_liabilities"),
            accumulated_other_comprehensive_income=d.get("accumulated_other_comprehensive_income"),
            additional_paid_in_capital=d.get("additional_paid_in_capital"),
            cash_and_equivalents=d.get("cash_and_equivalents"),
            cik=d.get("cik"),
            commitments_and_contingencies=d.get("commitments_and_contingencies"),
            common_stock=d.get("common_stock"),
            debt_current=d.get("debt_current"),
            deferred_revenue_current=d.get("deferred_revenue_current"),
            fiscal_quarter=d.get("fiscal_quarter"),
            fiscal_year=d.get("fiscal_year"),
            goodwill=d.get("goodwill"),
            intangible_assets_net=d.get("intangible_assets_net"),
            inventories=d.get("inventories"),
            long_term_debt_and_capital_lease_obligations=d.get("long_term_debt_and_capital_lease_obligations"),
            noncontrolling_interest=d.get("noncontrolling_interest"),
            other_assets=d.get("other_assets"),
            other_current_assets=d.get("other_current_assets"),
            other_equity=d.get("other_equity"),
            other_noncurrent_liabilities=d.get("other_noncurrent_liabilities"),
            period_end=d.get("period_end"),
            preferred_stock=d.get("preferred_stock"),
            property_plant_equipment_net=d.get("property_plant_equipment_net"),
            receivables=d.get("receivables"),
            retained_earnings_deficit=d.get("retained_earnings_deficit"),
            short_term_investments=d.get("short_term_investments"),
            tickers=d.get("tickers"),
            timeframe=d.get("timeframe"),
            total_assets=d.get("total_assets"),
            total_current_assets=d.get("total_current_assets"),
            total_current_liabilities=d.get("total_current_liabilities"),
            total_equity=d.get("total_equity"),
            total_equity_attributable_to_parent=d.get("total_equity_attributable_to_parent"),
            total_liabilities=d.get("total_liabilities"),
            total_liabilities_and_equity=d.get("total_liabilities_and_equity"),
            treasury_stock=d.get("treasury_stock"),
        )


@modelclass
@dataclass
class CashFlowStatement:
    """Represents a cash flow statement record from the new /stocks/financials/v1/cash-flow-statements endpoint."""

    cash_from_operating_activities_continuing_operations: Optional[float] = None
    change_in_cash_and_equivalents: Optional[float] = None
    change_in_other_operating_assets_and_liabilities_net: Optional[float] = None
    cik: Optional[str] = None
    depreciation_depletion_and_amortization: Optional[float] = None
    dividends: Optional[float] = None
    effect_of_currency_exchange_rate: Optional[float] = None
    fiscal_quarter: Optional[int] = None
    fiscal_year: Optional[int] = None
    income_loss_from_discontinued_operations: Optional[float] = None
    long_term_debt_issuances_repayments: Optional[float] = None
    net_cash_from_financing_activities: Optional[float] = None
    net_cash_from_financing_activities_continuing_operations: Optional[float] = None
    net_cash_from_financing_activities_discontinued_operations: Optional[float] = None
    net_cash_from_investing_activities: Optional[float] = None
    net_cash_from_investing_activities_continuing_operations: Optional[float] = None
    net_cash_from_investing_activities_discontinued_operations: Optional[float] = None
    net_cash_from_operating_activities: Optional[float] = None
    net_cash_from_operating_activities_discontinued_operations: Optional[float] = None
    net_income: Optional[float] = None
    noncontrolling_interests: Optional[float] = None
    other_cash_adjustments: Optional[float] = None
    other_financing_activities: Optional[float] = None
    other_investing_activities: Optional[float] = None
    other_operating_activities: Optional[float] = None
    period_end: Optional[str] = None
    purchase_of_property_plant_and_equipment: Optional[float] = None
    sale_of_property_plant_and_equipment: Optional[float] = None
    short_term_debt_issuances_repayments: Optional[float] = None
    tickers: Optional[List[str]] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "CashFlowStatement":
        if not d:
            return CashFlowStatement()
        return CashFlowStatement(
            cash_from_operating_activities_continuing_operations=d.get("cash_from_operating_activities_continuing_operations"),
            change_in_cash_and_equivalents=d.get("change_in_cash_and_equivalents"),
            change_in_other_operating_assets_and_liabilities_net=d.get("change_in_other_operating_assets_and_liabilities_net"),
            cik=d.get("cik"),
            depreciation_depletion_and_amortization=d.get("depreciation_depletion_and_amortization"),
            dividends=d.get("dividends"),
            effect_of_currency_exchange_rate=d.get("effect_of_currency_exchange_rate"),
            fiscal_quarter=d.get("fiscal_quarter"),
            fiscal_year=d.get("fiscal_year"),
            income_loss_from_discontinued_operations=d.get("income_loss_from_discontinued_operations"),
            long_term_debt_issuances_repayments=d.get("long_term_debt_issuances_repayments"),
            net_cash_from_financing_activities=d.get("net_cash_from_financing_activities"),
            net_cash_from_financing_activities_continuing_operations=d.get("net_cash_from_financing_activities_continuing_operations"),
            net_cash_from_financing_activities_discontinued_operations=d.get("net_cash_from_financing_activities_discontinued_operations"),
            net_cash_from_investing_activities=d.get("net_cash_from_investing_activities"),
            net_cash_from_investing_activities_continuing_operations=d.get("net_cash_from_investing_activities_continuing_operations"),
            net_cash_from_investing_activities_discontinued_operations=d.get("net_cash_from_investing_activities_discontinued_operations"),
            net_cash_from_operating_activities=d.get("net_cash_from_operating_activities"),
            net_cash_from_operating_activities_discontinued_operations=d.get("net_cash_from_operating_activities_discontinued_operations"),
            net_income=d.get("net_income"),
            noncontrolling_interests=d.get("noncontrolling_interests"),
            other_cash_adjustments=d.get("other_cash_adjustments"),
            other_financing_activities=d.get("other_financing_activities"),
            other_investing_activities=d.get("other_investing_activities"),
            other_operating_activities=d.get("other_operating_activities"),
            period_end=d.get("period_end"),
            purchase_of_property_plant_and_equipment=d.get("purchase_of_property_plant_and_equipment"),
            sale_of_property_plant_and_equipment=d.get("sale_of_property_plant_and_equipment"),
            short_term_debt_issuances_repayments=d.get("short_term_debt_issuances_repayments"),
            tickers=d.get("tickers"),
            timeframe=d.get("timeframe"),
        )


@modelclass
@dataclass
class IncomeStatement:
    """Represents an income statement record from the new /stocks/financials/v1/income-statements endpoint."""

    basic_earnings_per_share: Optional[float] = None
    basic_shares_outstanding: Optional[float] = None
    cik: Optional[str] = None
    consolidated_net_income_loss: Optional[float] = None
    cost_of_revenue: Optional[float] = None
    depreciation_depletion_amortization: Optional[float] = None
    diluted_earnings_per_share: Optional[float] = None
    diluted_shares_outstanding: Optional[float] = None
    discontinued_operations: Optional[float] = None
    ebitda: Optional[float] = None
    equity_in_affiliates: Optional[float] = None
    extraordinary_items: Optional[float] = None
    fiscal_quarter: Optional[int] = None
    fiscal_year: Optional[int] = None
    gross_profit: Optional[float] = None
    income_before_income_taxes: Optional[float] = None
    income_taxes: Optional[float] = None
    interest_expense: Optional[float] = None
    interest_income: Optional[float] = None
    net_income_loss_attributable_common_shareholders: Optional[float] = None
    noncontrolling_interest: Optional[float] = None
    operating_income: Optional[float] = None
    other_income_expense: Optional[float] = None
    other_operating_expenses: Optional[float] = None
    period_end: Optional[str] = None
    preferred_stock_dividends_declared: Optional[float] = None
    research_development: Optional[float] = None
    revenue: Optional[float] = None
    selling_general_administrative: Optional[float] = None
    tickers: Optional[List[str]] = None
    timeframe: Optional[str] = None
    total_operating_expenses: Optional[float] = None
    total_other_income_expense: Optional[float] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "IncomeStatement":
        if not d:
            return IncomeStatement()
        return IncomeStatement(
            basic_earnings_per_share=d.get("basic_earnings_per_share"),
            basic_shares_outstanding=d.get("basic_shares_outstanding"),
            cik=d.get("cik"),
            consolidated_net_income_loss=d.get("consolidated_net_income_loss"),
            cost_of_revenue=d.get("cost_of_revenue"),
            depreciation_depletion_amortization=d.get("depreciation_depletion_amortization"),
            diluted_earnings_per_share=d.get("diluted_earnings_per_share"),
            diluted_shares_outstanding=d.get("diluted_shares_outstanding"),
            discontinued_operations=d.get("discontinued_operations"),
            ebitda=d.get("ebitda"),
            equity_in_affiliates=d.get("equity_in_affiliates"),
            extraordinary_items=d.get("extraordinary_items"),
            fiscal_quarter=d.get("fiscal_quarter"),
            fiscal_year=d.get("fiscal_year"),
            gross_profit=d.get("gross_profit"),
            income_before_income_taxes=d.get("income_before_income_taxes"),
            income_taxes=d.get("income_taxes"),
            interest_expense=d.get("interest_expense"),
            interest_income=d.get("interest_income"),
            net_income_loss_attributable_common_shareholders=d.get("net_income_loss_attributable_common_shareholders"),
            noncontrolling_interest=d.get("noncontrolling_interest"),
            operating_income=d.get("operating_income"),
            other_income_expense=d.get("other_income_expense"),
            other_operating_expenses=d.get("other_operating_expenses"),
            period_end=d.get("period_end"),
            preferred_stock_dividends_declared=d.get("preferred_stock_dividends_declared"),
            research_development=d.get("research_development"),
            revenue=d.get("revenue"),
            selling_general_administrative=d.get("selling_general_administrative"),
            tickers=d.get("tickers"),
            timeframe=d.get("timeframe"),
            total_operating_expenses=d.get("total_operating_expenses"),
            total_other_income_expense=d.get("total_other_income_expense"),
        )


@modelclass
@dataclass
class FinancialRatios:
    """Represents financial ratios from the new /stocks/financials/v1/ratios endpoint."""

    average_volume: Optional[float] = None
    cash: Optional[float] = None
    cik: Optional[str] = None
    current: Optional[float] = None
    date: Optional[str] = None
    debt_to_equity: Optional[float] = None
    dividend_yield: Optional[float] = None
    earnings_per_share: Optional[float] = None
    enterprise_value: Optional[float] = None
    ev_to_ebitda: Optional[float] = None
    ev_to_sales: Optional[float] = None
    free_cash_flow: Optional[float] = None
    market_cap: Optional[float] = None
    price: Optional[float] = None
    price_to_book: Optional[float] = None
    price_to_cash_flow: Optional[float] = None
    price_to_earnings: Optional[float] = None
    price_to_free_cash_flow: Optional[float] = None
    price_to_sales: Optional[float] = None
    quick: Optional[float] = None
    return_on_assets: Optional[float] = None
    return_on_equity: Optional[float] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "FinancialRatios":
        if not d:
            return FinancialRatios()
        return FinancialRatios(
            average_volume=d.get("average_volume"),
            cash=d.get("cash"),
            cik=d.get("cik"),
            current=d.get("current"),
            date=d.get("date"),
            debt_to_equity=d.get("debt_to_equity"),
            dividend_yield=d.get("dividend_yield"),
            earnings_per_share=d.get("earnings_per_share"),
            enterprise_value=d.get("enterprise_value"),
            ev_to_ebitda=d.get("ev_to_ebitda"),
            ev_to_sales=d.get("ev_to_sales"),
            free_cash_flow=d.get("free_cash_flow"),
            market_cap=d.get("market_cap"),
            price=d.get("price"),
            price_to_book=d.get("price_to_book"),
            price_to_cash_flow=d.get("price_to_cash_flow"),
            price_to_earnings=d.get("price_to_earnings"),
            price_to_free_cash_flow=d.get("price_to_free_cash_flow"),
            price_to_sales=d.get("price_to_sales"),
            quick=d.get("quick"),
            return_on_assets=d.get("return_on_assets"),
            return_on_equity=d.get("return_on_equity"),
            ticker=d.get("ticker"),
        )


@modelclass
@dataclass
class ShortInterest:
    """Represents short interest data from the new /stocks/v1/short-interest endpoint."""

    avg_daily_volume: Optional[int] = None
    days_to_cover: Optional[float] = None
    settlement_date: Optional[str] = None
    short_interest: Optional[int] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "ShortInterest":
        if not d:
            return ShortInterest()
        return ShortInterest(
            avg_daily_volume=d.get("avg_daily_volume"),
            days_to_cover=d.get("days_to_cover"),
            settlement_date=d.get("settlement_date"),
            short_interest=d.get("short_interest"),
            ticker=d.get("ticker"),
        )


@modelclass
@dataclass
class ShortVolume:
    """Represents short volume data from the new /stocks/v1/short-volume endpoint."""

    adf_short_volume: Optional[int] = None
    adf_short_volume_exempt: Optional[int] = None
    date: Optional[str] = None
    exempt_volume: Optional[int] = None
    nasdaq_carteret_short_volume: Optional[int] = None
    nasdaq_carteret_short_volume_exempt: Optional[int] = None
    nasdaq_chicago_short_volume: Optional[int] = None
    nasdaq_chicago_short_volume_exempt: Optional[int] = None
    non_exempt_volume: Optional[int] = None
    nyse_short_volume: Optional[int] = None
    nyse_short_volume_exempt: Optional[int] = None
    short_volume: Optional[int] = None
    short_volume_ratio: Optional[float] = None
    ticker: Optional[str] = None
    total_volume: Optional[int] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "ShortVolume":
        if not d:
            return ShortVolume()
        return ShortVolume(
            adf_short_volume=d.get("adf_short_volume"),
            adf_short_volume_exempt=d.get("adf_short_volume_exempt"),
            date=d.get("date"),
            exempt_volume=d.get("exempt_volume"),
            nasdaq_carteret_short_volume=d.get("nasdaq_carteret_short_volume"),
            nasdaq_carteret_short_volume_exempt=d.get("nasdaq_carteret_short_volume_exempt"),
            nasdaq_chicago_short_volume=d.get("nasdaq_chicago_short_volume"),
            nasdaq_chicago_short_volume_exempt=d.get("nasdaq_chicago_short_volume_exempt"),
            non_exempt_volume=d.get("non_exempt_volume"),
            nyse_short_volume=d.get("nyse_short_volume"),
            nyse_short_volume_exempt=d.get("nyse_short_volume_exempt"),
            short_volume=d.get("short_volume"),
            short_volume_ratio=d.get("short_volume_ratio"),
            ticker=d.get("ticker"),
            total_volume=d.get("total_volume"),
        )
