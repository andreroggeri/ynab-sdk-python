from dataclasses import dataclass
from typing import Any

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
        result: dict = {}
        result["iso_code"] = parsers.from_str(self.iso_code)
        result["example_format"] = parsers.from_str(self.example_format)
        result["decimal_digits"] = parsers.from_int(self.decimal_digits)
        result["decimal_separator"] = parsers.from_str(self.decimal_separator)
        result["symbol_first"] = parsers.from_bool(self.symbol_first)
        result["group_separator"] = parsers.from_str(self.group_separator)
        result["currency_symbol"] = parsers.from_str(self.currency_symbol)
        result["display_symbol"] = parsers.from_bool(self.display_symbol)
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
        result: dict = {}
        result["format"] = parsers.from_str(self.format)
        return result


@dataclass
class Settings:
    date_format: DateFormat
    currency_format: CurrencyFormat

    @staticmethod
    def from_dict(obj: Any) -> 'Settings':
        assert isinstance(obj, dict)
        date_format = DateFormat.from_dict(obj.get("date_format"))
        currency_format = CurrencyFormat.from_dict(obj.get("currency_format"))
        return Settings(date_format, currency_format)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date_format"] = parsers.to_class(DateFormat, self.date_format)
        result["currency_format"] = parsers.to_class(CurrencyFormat, self.currency_format)
        return result


@dataclass
class Data:
    settings: Settings

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        settings = Settings.from_dict(obj.get("settings"))
        return Data(settings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["settings"] = parsers.to_class(Settings, self.settings)
        return result


@dataclass
class BudgetSettingsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BudgetSettingsResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return BudgetSettingsResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
