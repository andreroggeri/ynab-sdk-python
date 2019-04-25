from dataclasses import dataclass
from datetime import datetime
from typing import Any, List

import ynab_sdk_python.utils.parsers as parsers


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
    def from_dict(obj: Any) -> 'CurrencyFormat':
        assert isinstance(obj, dict)
        iso_code = parsers.from_str(obj.get("iso_code"))
        example_format = parsers.from_str(obj.get("example_format"))
        decimal_digits = parsers.from_int(obj.get("decimal_digits"))
        decimal_separator = parsers.from_str(obj.get("decimal_separator"))
        symbol_first = parsers.from_bool(obj.get("symbol_first"))
        group_separator = parsers.from_str(obj.get("group_separator"))
        currency_symbol = parsers.from_str(obj.get("currency_symbol"))
        display_symbol = parsers.from_bool(obj.get("display_symbol"))
        return CurrencyFormat(iso_code, example_format, decimal_digits, decimal_separator, symbol_first,
                              group_separator, currency_symbol, display_symbol)

    def to_dict(self) -> dict:
        result: dict = {
            "iso_code": parsers.from_str(self.iso_code),
            "example_format": parsers.from_str(self.example_format),
            "decimal_digits": parsers.from_int(self.decimal_digits),
            "decimal_separator": parsers.from_str(self.decimal_separator),
            "symbol_first": parsers.from_bool(self.symbol_first),
            "group_separator": parsers.from_str(self.group_separator),
            "currency_symbol": parsers.from_str(self.currency_symbol),
            "display_symbol": parsers.from_bool(self.display_symbol)
        }
        return result


@dataclass
class DateFormat:
    format: str

    @staticmethod
    def from_dict(obj: Any) -> 'DateFormat':
        assert isinstance(obj, dict)
        format = parsers.from_str(obj.get("format"))
        return DateFormat(format)

    def to_dict(self) -> dict:
        result: dict = {"format": parsers.from_str(self.format)}
        return result


@dataclass
class Budget:
    id: str
    name: str
    last_modified_on: datetime
    first_month: str
    last_month: str
    date_format: DateFormat
    currency_format: CurrencyFormat

    @staticmethod
    def from_dict(obj: Any) -> 'Budget':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        last_modified_on = parsers.from_datetime(obj.get("last_modified_on"))
        first_month = parsers.from_str(obj.get("first_month"))
        last_month = parsers.from_str(obj.get("last_month"))
        date_format = DateFormat.from_dict(obj.get("date_format"))
        currency_format = CurrencyFormat.from_dict(obj.get("currency_format"))
        return Budget(id, name, last_modified_on, first_month, last_month, date_format, currency_format)

    def to_dict(self) -> dict:
        result: dict = {
            "id": parsers.from_str(self.id),
            "name": parsers.from_str(self.name),
            "last_modified_on": self.last_modified_on.isoformat(),
            "first_month": parsers.from_str(self.first_month),
            "last_month": parsers.from_str(self.last_month),
            "date_format": parsers.to_class(DateFormat, self.date_format),
            "currency_format": parsers.to_class(CurrencyFormat, self.currency_format)
        }
        return result


@dataclass
class Data:
    budgets: List[Budget]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        budgets = parsers.from_list(Budget.from_dict, obj.get("budgets"))
        return Data(budgets)

    def to_dict(self) -> dict:
        result: dict = {"budgets": parsers.from_list(lambda x: parsers.to_class(Budget, x), self.budgets)}
        return result


@dataclass
class BudgetSummaryResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BudgetSummaryResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return BudgetSummaryResponse(data)

    def to_dict(self) -> dict:
        result: dict = {"data": parsers.to_class(Data, self.data)}
        return result
