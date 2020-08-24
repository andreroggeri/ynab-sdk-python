from dataclasses import dataclass
from datetime import datetime
from typing import Any, List

from ynab_sdk.utils import parsers


@dataclass
class CurrencyFormat:
    iso_code: str
    example_format: str
    decimal_digits: int
    decimal_separator: str
    symbol_first: bool
    group_separator: str
    currency_symbol: str
    display_symbol: bool

    @staticmethod
    def from_dict(obj: Any) -> "CurrencyFormat":
        assert isinstance(obj, dict)
        iso_code = parsers.from_str(obj.get("iso_code"))
        example_format = parsers.from_str(obj.get("example_format"))
        decimal_digits = parsers.from_int(obj.get("decimal_digits"))
        decimal_separator = parsers.from_str(obj.get("decimal_separator"))
        symbol_first = parsers.from_bool(obj.get("symbol_first"))
        group_separator = parsers.from_str(obj.get("group_separator"))
        currency_symbol = parsers.from_str(obj.get("currency_symbol"))
        display_symbol = parsers.from_bool(obj.get("display_symbol"))
        return CurrencyFormat(
            iso_code,
            example_format,
            decimal_digits,
            decimal_separator,
            symbol_first,
            group_separator,
            currency_symbol,
            display_symbol,
        )


@dataclass
class DateFormat:
    format: str

    @staticmethod
    def from_dict(obj: Any) -> "DateFormat":
        assert isinstance(obj, dict)
        date_format = parsers.from_str(obj.get("format"))
        return DateFormat(date_format)


@dataclass
class Budget:
    budget_id: str
    name: str
    last_modified_on: datetime
    first_month: str
    last_month: str
    date_format: DateFormat
    currency_format: CurrencyFormat

    @staticmethod
    def from_dict(obj: Any) -> "Budget":
        assert isinstance(obj, dict)
        budget_id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        last_modified_on = parsers.from_datetime(obj.get("last_modified_on"))
        first_month = parsers.from_str(obj.get("first_month"))
        last_month = parsers.from_str(obj.get("last_month"))
        date_format = DateFormat.from_dict(obj.get("date_format"))
        currency_format = CurrencyFormat.from_dict(obj.get("currency_format"))
        return Budget(
            budget_id,
            name,
            last_modified_on,
            first_month,
            last_month,
            date_format,
            currency_format,
        )


@dataclass
class Data:
    budgets: List[Budget]

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        budgets = parsers.from_list(Budget.from_dict, obj.get("budgets"))
        return Data(budgets)


@dataclass
class BudgetSummaryResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "BudgetSummaryResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return BudgetSummaryResponse(data)
