from typing import Optional, Dict
from ...modelclass import modelclass


@modelclass
class DataPoint:
    "Represents a single financial data point."
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    derived_from: Optional[list] = None
    formula: Optional[str] = None
    source: Optional[dict] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
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


@modelclass
class ExchangeGainsLosses:
    "Contains exchange gains losses data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ExchangeGainsLosses(**d)


@modelclass
class NetCashFlow:
    "Contains net cash flow data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return NetCashFlow(**d)


@modelclass
class NetCashFlowFromFinancingActivities:
    "Contains net cash flow from financing activities data for a cash flow statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return NetCashFlowFromFinancingActivities(**d)


@modelclass
class CashFlowStatement:
    "Contains cash flow statement data."
    exchange_gains_losses: Optional[ExchangeGainsLosses] = None
    net_cash_flow: Optional[NetCashFlow] = None
    net_cash_flow_from_financing_activities: Optional[
        NetCashFlowFromFinancingActivities
    ] = None

    @staticmethod
    def from_dict(d):
        return CashFlowStatement(
            exchange_gains_losses=(
                None
                if "exchange_gains_losses" not in d
                else ExchangeGainsLosses.from_dict(d["exchange_gains_losses"])
            ),
            net_cash_flow=(
                None
                if "net_cash_flow" not in d
                else NetCashFlow.from_dict(d["net_cash_flow"])
            ),
            net_cash_flow_from_financing_activities=(
                None
                if "net_cash_flow_from_financing_activities" not in d
                else NetCashFlowFromFinancingActivities.from_dict(
                    d["net_cash_flow_from_financing_activities"]
                )
            ),
        )


@modelclass
class ComprehensiveIncomeLoss:
    "Contains comprehensive income loss data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncomeLoss(**d)


@modelclass
class ComprehensiveIncomeLossAttributableToParent:
    "Contains comprehensive income loss attributable to parent data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncomeLossAttributableToParent(**d)


@modelclass
class OtherComprehensiveIncomeLoss:
    "Contains other comprehensive income loss data for comprehensive income."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OtherComprehensiveIncomeLoss(**d)


@modelclass
class ComprehensiveIncome:
    "Contains comprehensive income data."
    comprehensive_income_loss: Optional[ComprehensiveIncomeLoss] = None
    comprehensive_income_loss_attributable_to_parent: Optional[
        ComprehensiveIncomeLossAttributableToParent
    ] = None
    other_comprehensive_income_loss: Optional[OtherComprehensiveIncomeLoss] = None

    @staticmethod
    def from_dict(d):
        return ComprehensiveIncome(
            comprehensive_income_loss=(
                None
                if "comprehensive_income_loss" not in d
                else ComprehensiveIncomeLoss.from_dict(d["comprehensive_income_loss"])
            ),
            comprehensive_income_loss_attributable_to_parent=(
                None
                if "comprehensive_income_loss_attributable_to_parent" not in d
                else ComprehensiveIncomeLossAttributableToParent.from_dict(
                    d["comprehensive_income_loss_attributable_to_parent"]
                )
            ),
            other_comprehensive_income_loss=(
                None
                if "other_comprehensive_income_loss" not in d
                else OtherComprehensiveIncomeLoss.from_dict(
                    d["other_comprehensive_income_loss"]
                )
            ),
        )


@modelclass
class BasicEarningsPerShare:
    "Contains basic earning per share data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return BasicEarningsPerShare(**d)


@modelclass
class CostOfRevenue:
    "Contains cost of revenue data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return CostOfRevenue(**d)


@modelclass
class GrossProfit:
    "Contains gross profit data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return GrossProfit(**d)


@modelclass
class OperatingExpenses:
    "Contains operating expenses data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OperatingExpenses(**d)


@modelclass
class Revenues:
    "Contains revenues data for an income statement."
    formula: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    xpath: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Revenues(**d)


@modelclass
class IncomeStatement:
    "Contains income statement data."
    basic_earnings_per_share: Optional[BasicEarningsPerShare] = None
    cost_of_revenue: Optional[CostOfRevenue] = None
    gross_profit: Optional[GrossProfit] = None
    operating_expenses: Optional[OperatingExpenses] = None
    revenues: Optional[Revenues] = None

    @staticmethod
    def from_dict(d):
        return IncomeStatement(
            basic_earnings_per_share=(
                None
                if "basic_earnings_per_share" not in d
                else BasicEarningsPerShare.from_dict(d["basic_earnings_per_share"])
            ),
            cost_of_revenue=(
                None
                if "cost_of_revenue" not in d
                else CostOfRevenue.from_dict(d["cost_of_revenue"])
            ),
            gross_profit=(
                None
                if "gross_profit" not in d
                else GrossProfit.from_dict(d["gross_profit"])
            ),
            operating_expenses=(
                None
                if "operating_expenses" not in d
                else OperatingExpenses.from_dict(d["operating_expenses"])
            ),
            revenues=None if "revenues" not in d else Revenues.from_dict(d["revenues"]),
        )


@modelclass
class Financials:
    """
    Contains data for:
      - balance_sheet
      - cash_flow_statement
      - comprehensive_income
      - income_statement
    Each is a dict of { 'SomeTag': DataPoint }, e.g. { 'NetIncomeLoss': DataPoint(...) }
    """

    balance_sheet: Optional[dict] = None
    cash_flow_statement: Optional[dict] = None
    comprehensive_income: Optional[dict] = None
    income_statement: Optional[dict] = None

    @staticmethod
    def from_dict(d):
        def parse_statement(x):
            if not x or not isinstance(x, dict):
                return None
            return {k: DataPoint.from_dict(v) for k, v in x.items()}

        return Financials(
            balance_sheet=parse_statement(d.get("balance_sheet")),
            cash_flow_statement=parse_statement(d.get("cash_flow_statement")),
            comprehensive_income=parse_statement(d.get("comprehensive_income")),
            income_statement=parse_statement(d.get("income_statement")),
        )


@modelclass
class StockFinancial:
    """
    StockFinancial contains historical financial data for a stock ticker.
    """

    # Existing fields (unchanged):
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
    def from_dict(d):
        """
        Create a StockFinancial, preserving all old behavior, but also pulling out
        a few commonly used fields from the income_statement and comprehensive_income
        so they can be accessed directly at the top level.
        """
        sf = StockFinancial(
            cik=d.get("cik"),
            company_name=d.get("company_name"),
            end_date=d.get("end_date"),
            filing_date=d.get("filing_date"),
            financials=(
                Financials.from_dict(d["financials"]) if "financials" in d else None
            ),
            fiscal_period=d.get("fiscal_period"),
            fiscal_year=d.get("fiscal_year"),
            source_filing_file_url=d.get("source_filing_file_url"),
            source_filing_url=d.get("source_filing_url"),
            start_date=d.get("start_date"),
        )

        return sf
