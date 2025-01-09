from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from ...modelclass import modelclass


@modelclass
@dataclass
class DataPoint:
    """Represents a single numeric or textual data point in the financials."""

    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    derived_from: Optional[List[str]] = None
    formula: Optional[str] = None
    source: Optional[Dict[str, str]] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "DataPoint":
        if not d:
            return DataPoint()
        return DataPoint(
            label=d.get("label"),
            order=d.get("order"),
            unit=d.get("unit"),
            value=d.get("value"),
            derived_from=d.get("derived_from"),
            formula=d.get("formula"),
            source=d.get("source"),
            xpath=d.get("xpath"),
        )


@dataclass
@modelclass
class BalanceSheet:
    assets: Optional[DataPoint] = None
    current_assets: Optional[DataPoint] = None
    cash: Optional[DataPoint] = None
    accounts_receivable: Optional[DataPoint] = None
    inventory: Optional[DataPoint] = None
    prepaid_expenses: Optional[DataPoint] = None
    other_current_assets: Optional[DataPoint] = None
    noncurrent_assets: Optional[DataPoint] = None
    long_term_investments: Optional[DataPoint] = None
    fixed_assets: Optional[DataPoint] = None
    intangible_assets: Optional[DataPoint] = None
    noncurrent_prepaid_expense: Optional[DataPoint] = None
    other_noncurrent_assets: Optional[DataPoint] = None
    liabilities: Optional[DataPoint] = None
    current_liabilities: Optional[DataPoint] = None
    accounts_payable: Optional[DataPoint] = None
    interest_payable: Optional[DataPoint] = None
    wages: Optional[DataPoint] = None
    other_current_liabilities: Optional[DataPoint] = None
    noncurrent_liabilities: Optional[DataPoint] = None
    long_term_debt: Optional[DataPoint] = None
    other_noncurrent_liabilities: Optional[DataPoint] = None
    commitments_and_contingencies: Optional[DataPoint] = None
    redeemable_noncontrolling_interest: Optional[DataPoint] = None
    redeemable_noncontrolling_interest_common: Optional[DataPoint] = None
    redeemable_noncontrolling_interest_other: Optional[DataPoint] = None
    redeemable_noncontrolling_interest_preferred: Optional[DataPoint] = None
    equity: Optional[DataPoint] = None
    equity_attributable_to_noncontrolling_interest: Optional[DataPoint] = None
    equity_attributable_to_parent: Optional[DataPoint] = None
    temporary_equity: Optional[DataPoint] = None
    temporary_equity_attributable_to_parent: Optional[DataPoint] = None
    liabilities_and_equity: Optional[DataPoint] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "BalanceSheet":
        if not d:
            return BalanceSheet()
        return BalanceSheet(
            assets=DataPoint.from_dict(d.get("assets")),
            current_assets=DataPoint.from_dict(d.get("current_assets")),
            cash=DataPoint.from_dict(d.get("cash")),
            accounts_receivable=DataPoint.from_dict(d.get("accounts_receivable")),
            inventory=DataPoint.from_dict(d.get("inventory")),
            prepaid_expenses=DataPoint.from_dict(d.get("prepaid_expenses")),
            other_current_assets=DataPoint.from_dict(d.get("other_current_assets")),
            noncurrent_assets=DataPoint.from_dict(d.get("noncurrent_assets")),
            long_term_investments=DataPoint.from_dict(d.get("long_term_investments")),
            fixed_assets=DataPoint.from_dict(d.get("fixed_assets")),
            intangible_assets=DataPoint.from_dict(d.get("intangible_assets")),
            noncurrent_prepaid_expense=DataPoint.from_dict(
                d.get("noncurrent_prepaid_expense")
            ),
            other_noncurrent_assets=DataPoint.from_dict(
                d.get("other_noncurrent_assets")
            ),
            liabilities=DataPoint.from_dict(d.get("liabilities")),
            current_liabilities=DataPoint.from_dict(d.get("current_liabilities")),
            accounts_payable=DataPoint.from_dict(d.get("accounts_payable")),
            interest_payable=DataPoint.from_dict(d.get("interest_payable")),
            wages=DataPoint.from_dict(d.get("wages")),
            other_current_liabilities=DataPoint.from_dict(
                d.get("other_current_liabilities")
            ),
            noncurrent_liabilities=DataPoint.from_dict(d.get("noncurrent_liabilities")),
            long_term_debt=DataPoint.from_dict(d.get("long_term_debt")),
            other_noncurrent_liabilities=DataPoint.from_dict(
                d.get("other_noncurrent_liabilities")
            ),
            commitments_and_contingencies=DataPoint.from_dict(
                d.get("commitments_and_contingencies")
            ),
            redeemable_noncontrolling_interest=DataPoint.from_dict(
                d.get("redeemable_noncontrolling_interest")
            ),
            redeemable_noncontrolling_interest_common=DataPoint.from_dict(
                d.get("redeemable_noncontrolling_interest_common")
            ),
            redeemable_noncontrolling_interest_other=DataPoint.from_dict(
                d.get("redeemable_noncontrolling_interest_other")
            ),
            redeemable_noncontrolling_interest_preferred=DataPoint.from_dict(
                d.get("redeemable_noncontrolling_interest_preferred")
            ),
            equity=DataPoint.from_dict(d.get("equity")),
            equity_attributable_to_noncontrolling_interest=DataPoint.from_dict(
                d.get("equity_attributable_to_noncontrolling_interest")
            ),
            equity_attributable_to_parent=DataPoint.from_dict(
                d.get("equity_attributable_to_parent")
            ),
            temporary_equity=DataPoint.from_dict(d.get("temporary_equity")),
            temporary_equity_attributable_to_parent=DataPoint.from_dict(
                d.get("temporary_equity_attributable_to_parent")
            ),
            liabilities_and_equity=DataPoint.from_dict(d.get("liabilities_and_equity")),
        )


@dataclass
@modelclass
class CashFlowStatement:
    net_cash_flow_from_operating_activities: Optional[DataPoint] = None
    net_cash_flow_from_operating_activities_continuing: Optional[DataPoint] = None
    net_cash_flow_from_operating_activities_discontinued: Optional[DataPoint] = None
    net_cash_flow_from_investing_activities: Optional[DataPoint] = None
    net_cash_flow_from_investing_activities_continuing: Optional[DataPoint] = None
    net_cash_flow_from_investing_activities_discontinued: Optional[DataPoint] = None
    net_cash_flow_from_financing_activities: Optional[DataPoint] = None
    net_cash_flow_from_financing_activities_continuing: Optional[DataPoint] = None
    net_cash_flow_from_financing_activities_discontinued: Optional[DataPoint] = None
    exchange_gains_losses: Optional[DataPoint] = None
    net_cash_flow: Optional[DataPoint] = None
    net_cash_flow_continuing: Optional[DataPoint] = None
    net_cash_flow_discontinued: Optional[DataPoint] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "CashFlowStatement":
        if not d:
            return CashFlowStatement()
        return CashFlowStatement(
            net_cash_flow_from_operating_activities=DataPoint.from_dict(
                d.get("net_cash_flow_from_operating_activities")
            ),
            net_cash_flow_from_operating_activities_continuing=DataPoint.from_dict(
                d.get("net_cash_flow_from_operating_activities_continuing")
            ),
            net_cash_flow_from_operating_activities_discontinued=DataPoint.from_dict(
                d.get("net_cash_flow_from_operating_activities_discontinued")
            ),
            net_cash_flow_from_investing_activities=DataPoint.from_dict(
                d.get("net_cash_flow_from_investing_activities")
            ),
            net_cash_flow_from_investing_activities_continuing=DataPoint.from_dict(
                d.get("net_cash_flow_from_investing_activities_continuing")
            ),
            net_cash_flow_from_investing_activities_discontinued=DataPoint.from_dict(
                d.get("net_cash_flow_from_investing_activities_discontinued")
            ),
            net_cash_flow_from_financing_activities=DataPoint.from_dict(
                d.get("net_cash_flow_from_financing_activities")
            ),
            net_cash_flow_from_financing_activities_continuing=DataPoint.from_dict(
                d.get("net_cash_flow_from_financing_activities_continuing")
            ),
            net_cash_flow_from_financing_activities_discontinued=DataPoint.from_dict(
                d.get("net_cash_flow_from_financing_activities_discontinued")
            ),
            exchange_gains_losses=DataPoint.from_dict(d.get("exchange_gains_losses")),
            net_cash_flow=DataPoint.from_dict(d.get("net_cash_flow")),
            net_cash_flow_continuing=DataPoint.from_dict(
                d.get("net_cash_flow_continuing")
            ),
            net_cash_flow_discontinued=DataPoint.from_dict(
                d.get("net_cash_flow_discontinued")
            ),
        )


@dataclass
@modelclass
class ComprehensiveIncome:
    comprehensive_income_loss: Optional[DataPoint] = None
    comprehensive_income_loss_attributable_to_noncontrolling_interest: Optional[
        DataPoint
    ] = None
    comprehensive_income_loss_attributable_to_parent: Optional[DataPoint] = None
    other_comprehensive_income_loss: Optional[DataPoint] = None
    other_comprehensive_income_loss_attributable_to_noncontrolling_interest: Optional[
        DataPoint
    ] = None
    other_comprehensive_income_loss_attributable_to_parent: Optional[DataPoint] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "ComprehensiveIncome":
        if not d:
            return ComprehensiveIncome()
        return ComprehensiveIncome(
            comprehensive_income_loss=DataPoint.from_dict(
                d.get("comprehensive_income_loss")
            ),
            comprehensive_income_loss_attributable_to_noncontrolling_interest=DataPoint.from_dict(
                d.get(
                    "comprehensive_income_loss_attributable_to_noncontrolling_interest"
                )
            ),
            comprehensive_income_loss_attributable_to_parent=DataPoint.from_dict(
                d.get("comprehensive_income_loss_attributable_to_parent")
            ),
            other_comprehensive_income_loss=DataPoint.from_dict(
                d.get("other_comprehensive_income_loss")
            ),
            other_comprehensive_income_loss_attributable_to_noncontrolling_interest=DataPoint.from_dict(
                d.get(
                    "other_comprehensive_income_loss_attributable_to_noncontrolling_interest"
                )
            ),
            other_comprehensive_income_loss_attributable_to_parent=DataPoint.from_dict(
                d.get("other_comprehensive_income_loss_attributable_to_parent")
            ),
        )


@dataclass
@modelclass
class IncomeStatement:
    revenues: Optional[DataPoint] = None
    benefits_costs_expenses: Optional[DataPoint] = None
    cost_of_revenue: Optional[DataPoint] = None
    cost_of_revenue_goods: Optional[DataPoint] = None
    cost_of_revenue_services: Optional[DataPoint] = None
    costs_and_expenses: Optional[DataPoint] = None
    gross_profit: Optional[DataPoint] = None
    gain_loss_on_sale_properties_net_tax: Optional[DataPoint] = None
    nonoperating_income_loss: Optional[DataPoint] = None
    operating_expenses: Optional[DataPoint] = None
    selling_general_and_administrative_expenses: Optional[DataPoint] = None
    depreciation_and_amortization: Optional[DataPoint] = None
    research_and_development: Optional[DataPoint] = None
    other_operating_expenses: Optional[DataPoint] = None
    operating_income_loss: Optional[DataPoint] = None
    other_operating_income_expenses: Optional[DataPoint] = None
    income_loss_before_equity_method_investments: Optional[DataPoint] = None
    income_loss_from_continuing_operations_after_tax: Optional[DataPoint] = None
    income_loss_from_continuing_operations_before_tax: Optional[DataPoint] = None
    income_loss_from_discontinued_operations_net_of_tax: Optional[DataPoint] = None
    income_loss_from_discontinued_operations_net_of_tax_adjustment_to_prior_year_gain_loss_on_disposal: Optional[
        DataPoint
    ] = None
    income_loss_from_discontinued_operations_net_of_tax_during_phase_out: Optional[
        DataPoint
    ] = None
    income_loss_from_discontinued_operations_net_of_tax_gain_loss_on_disposal: Optional[
        DataPoint
    ] = None
    income_loss_from_discontinued_operations_net_of_tax_provision_for_gain_loss_on_disposal: Optional[
        DataPoint
    ] = None
    income_loss_from_equity_method_investments: Optional[DataPoint] = None
    income_tax_expense_benefit: Optional[DataPoint] = None
    income_tax_expense_benefit_current: Optional[DataPoint] = None
    income_tax_expense_benefit_deferred: Optional[DataPoint] = None
    interest_and_debt_expense: Optional[DataPoint] = None
    interest_and_dividend_income_operating: Optional[DataPoint] = None
    interest_expense_operating: Optional[DataPoint] = None
    interest_income_expense_after_provision_for_losses: Optional[DataPoint] = None
    interest_income_expense_operating_net: Optional[DataPoint] = None
    noninterest_expense: Optional[DataPoint] = None
    noninterest_income: Optional[DataPoint] = None
    provision_for_loan_lease_and_other_losses: Optional[DataPoint] = None
    net_income_loss: Optional[DataPoint] = None
    net_income_loss_attributable_to_noncontrolling_interest: Optional[DataPoint] = None
    net_income_loss_attributable_to_nonredeemable_noncontrolling_interest: Optional[
        DataPoint
    ] = None
    net_income_loss_attributable_to_parent: Optional[DataPoint] = None
    net_income_loss_attributable_to_redeemable_noncontrolling_interest: Optional[
        DataPoint
    ] = None
    net_income_loss_available_to_common_stockholders_basic: Optional[DataPoint] = None
    participating_securities_distributed_and_undistributed_earnings_loss_basic: (
        Optional[DataPoint]
    ) = (None)
    undistributed_earnings_loss_allocated_to_participating_securities_basic: Optional[
        DataPoint
    ] = None
    preferred_stock_dividends_and_other_adjustments: Optional[DataPoint] = None
    basic_earnings_per_share: Optional[DataPoint] = None
    diluted_earnings_per_share: Optional[DataPoint] = None
    basic_average_shares: Optional[DataPoint] = None
    diluted_average_shares: Optional[DataPoint] = None
    common_stock_dividends: Optional[DataPoint] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "IncomeStatement":
        if not d:
            return IncomeStatement()
        return IncomeStatement(
            revenues=DataPoint.from_dict(d.get("revenues")),
            benefits_costs_expenses=DataPoint.from_dict(
                d.get("benefits_costs_expenses")
            ),
            cost_of_revenue=DataPoint.from_dict(d.get("cost_of_revenue")),
            cost_of_revenue_goods=DataPoint.from_dict(d.get("cost_of_revenue_goods")),
            cost_of_revenue_services=DataPoint.from_dict(
                d.get("cost_of_revenue_services")
            ),
            costs_and_expenses=DataPoint.from_dict(d.get("costs_and_expenses")),
            gross_profit=DataPoint.from_dict(d.get("gross_profit")),
            gain_loss_on_sale_properties_net_tax=DataPoint.from_dict(
                d.get("gain_loss_on_sale_properties_net_tax")
            ),
            nonoperating_income_loss=DataPoint.from_dict(
                d.get("nonoperating_income_loss")
            ),
            operating_expenses=DataPoint.from_dict(d.get("operating_expenses")),
            selling_general_and_administrative_expenses=DataPoint.from_dict(
                d.get("selling_general_and_administrative_expenses")
            ),
            depreciation_and_amortization=DataPoint.from_dict(
                d.get("depreciation_and_amortization")
            ),
            research_and_development=DataPoint.from_dict(
                d.get("research_and_development")
            ),
            other_operating_expenses=DataPoint.from_dict(
                d.get("other_operating_expenses")
            ),
            operating_income_loss=DataPoint.from_dict(d.get("operating_income_loss")),
            other_operating_income_expenses=DataPoint.from_dict(
                d.get("other_operating_income_expenses")
            ),
            income_loss_before_equity_method_investments=DataPoint.from_dict(
                d.get("income_loss_before_equity_method_investments")
            ),
            income_loss_from_continuing_operations_after_tax=DataPoint.from_dict(
                d.get("income_loss_from_continuing_operations_after_tax")
            ),
            income_loss_from_continuing_operations_before_tax=DataPoint.from_dict(
                d.get("income_loss_from_continuing_operations_before_tax")
            ),
            income_loss_from_discontinued_operations_net_of_tax=DataPoint.from_dict(
                d.get("income_loss_from_discontinued_operations_net_of_tax")
            ),
            income_loss_from_discontinued_operations_net_of_tax_adjustment_to_prior_year_gain_loss_on_disposal=DataPoint.from_dict(
                d.get(
                    "income_loss_from_discontinued_operations_net_of_tax_adjustment_to_prior_year_gain_loss_on_disposal"
                )
            ),
            income_loss_from_discontinued_operations_net_of_tax_during_phase_out=DataPoint.from_dict(
                d.get(
                    "income_loss_from_discontinued_operations_net_of_tax_during_phase_out"
                )
            ),
            income_loss_from_discontinued_operations_net_of_tax_gain_loss_on_disposal=DataPoint.from_dict(
                d.get(
                    "income_loss_from_discontinued_operations_net_of_tax_gain_loss_on_disposal"
                )
            ),
            income_loss_from_discontinued_operations_net_of_tax_provision_for_gain_loss_on_disposal=DataPoint.from_dict(
                d.get(
                    "income_loss_from_discontinued_operations_net_of_tax_provision_for_gain_loss_on_disposal"
                )
            ),
            income_loss_from_equity_method_investments=DataPoint.from_dict(
                d.get("income_loss_from_equity_method_investments")
            ),
            income_tax_expense_benefit=DataPoint.from_dict(
                d.get("income_tax_expense_benefit")
            ),
            income_tax_expense_benefit_current=DataPoint.from_dict(
                d.get("income_tax_expense_benefit_current")
            ),
            income_tax_expense_benefit_deferred=DataPoint.from_dict(
                d.get("income_tax_expense_benefit_deferred")
            ),
            interest_and_debt_expense=DataPoint.from_dict(
                d.get("interest_and_debt_expense")
            ),
            interest_and_dividend_income_operating=DataPoint.from_dict(
                d.get("interest_and_dividend_income_operating")
            ),
            interest_expense_operating=DataPoint.from_dict(
                d.get("interest_expense_operating")
            ),
            interest_income_expense_after_provision_for_losses=DataPoint.from_dict(
                d.get("interest_income_expense_after_provision_for_losses")
            ),
            interest_income_expense_operating_net=DataPoint.from_dict(
                d.get("interest_income_expense_operating_net")
            ),
            noninterest_expense=DataPoint.from_dict(d.get("noninterest_expense")),
            noninterest_income=DataPoint.from_dict(d.get("noninterest_income")),
            provision_for_loan_lease_and_other_losses=DataPoint.from_dict(
                d.get("provision_for_loan_lease_and_other_losses")
            ),
            net_income_loss=DataPoint.from_dict(d.get("net_income_loss")),
            net_income_loss_attributable_to_noncontrolling_interest=DataPoint.from_dict(
                d.get("net_income_loss_attributable_to_noncontrolling_interest")
            ),
            net_income_loss_attributable_to_nonredeemable_noncontrolling_interest=DataPoint.from_dict(
                d.get(
                    "net_income_loss_attributable_to_nonredeemable_noncontrolling_interest"
                )
            ),
            net_income_loss_attributable_to_parent=DataPoint.from_dict(
                d.get("net_income_loss_attributable_to_parent")
            ),
            net_income_loss_attributable_to_redeemable_noncontrolling_interest=DataPoint.from_dict(
                d.get(
                    "net_income_loss_attributable_to_redeemable_noncontrolling_interest"
                )
            ),
            net_income_loss_available_to_common_stockholders_basic=DataPoint.from_dict(
                d.get("net_income_loss_available_to_common_stockholders_basic")
            ),
            participating_securities_distributed_and_undistributed_earnings_loss_basic=DataPoint.from_dict(
                d.get(
                    "participating_securities_distributed_and_undistributed_earnings_loss_basic"
                )
            ),
            undistributed_earnings_loss_allocated_to_participating_securities_basic=DataPoint.from_dict(
                d.get(
                    "undistributed_earnings_loss_allocated_to_participating_securities_basic"
                )
            ),
            preferred_stock_dividends_and_other_adjustments=DataPoint.from_dict(
                d.get("preferred_stock_dividends_and_other_adjustments")
            ),
            basic_earnings_per_share=DataPoint.from_dict(
                d.get("basic_earnings_per_share")
            ),
            diluted_earnings_per_share=DataPoint.from_dict(
                d.get("diluted_earnings_per_share")
            ),
            basic_average_shares=DataPoint.from_dict(d.get("basic_average_shares")),
            diluted_average_shares=DataPoint.from_dict(d.get("diluted_average_shares")),
            common_stock_dividends=DataPoint.from_dict(d.get("common_stock_dividends")),
        )


@dataclass
@modelclass
class Financials:
    """
    Contains data for:
      - balance_sheet (BalanceSheet)
      - cash_flow_statement (CashFlowStatement)
      - comprehensive_income (ComprehensiveIncome)
      - income_statement (IncomeStatement)
    """

    balance_sheet: Optional[BalanceSheet] = None
    cash_flow_statement: Optional[CashFlowStatement] = None
    comprehensive_income: Optional[ComprehensiveIncome] = None
    income_statement: Optional[IncomeStatement] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "Financials":
        if not d:
            return Financials()
        return Financials(
            balance_sheet=BalanceSheet.from_dict(d.get("balance_sheet")),
            cash_flow_statement=CashFlowStatement.from_dict(
                d.get("cash_flow_statement")
            ),
            comprehensive_income=ComprehensiveIncome.from_dict(
                d.get("comprehensive_income")
            ),
            income_statement=IncomeStatement.from_dict(d.get("income_statement")),
        )


@dataclass
@modelclass
class StockFinancial:
    """
    StockFinancial contains historical financial data for a stock ticker.
    The 'financials' attribute references an instance of Financials
    which has typed sub-statements.
    """

    cik: Optional[str] = None
    company_name: Optional[str] = None
    end_date: Optional[str] = None
    filing_date: Optional[str] = None
    financials: Optional[Financials] = None
    fiscal_period: Optional[str] = None
    fiscal_year: Optional[str] = None
    source_filing_file_url: Optional[str] = None
    source_filing_url: Optional[str] = None
    start_date: Optional[str] = None

    @staticmethod
    def from_dict(d: Optional[Dict[str, Any]]) -> "StockFinancial":
        if not d:
            return StockFinancial()
        return StockFinancial(
            cik=d.get("cik"),
            company_name=d.get("company_name"),
            end_date=d.get("end_date"),
            filing_date=d.get("filing_date"),
            financials=Financials.from_dict(d.get("financials", {})),
            fiscal_period=d.get("fiscal_period"),
            fiscal_year=d.get("fiscal_year"),
            source_filing_file_url=d.get("source_filing_file_url"),
            source_filing_url=d.get("source_filing_url"),
            start_date=d.get("start_date"),
        )
