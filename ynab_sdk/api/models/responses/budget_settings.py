from dataclasses import dataclass
from typing import Any

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
        format = parsers.from_str(obj.get("format"))
        return DateFormat(format)


@dataclass
class Settings:
    date_format: DateFormat
    currency_format: CurrencyFormat

    @staticmethod
    def from_dict(obj: Any) -> "Settings":
        assert isinstance(obj, dict)
        date_format = DateFormat.from_dict(obj.get("date_format"))
        currency_format = CurrencyFormat.from_dict(obj.get("currency_format"))
        return Settings(date_format, currency_format)


@dataclass
class Data:
    settings: Settings

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        settings = Settings.from_dict(obj.get("settings"))
        return Data(settings)


@dataclass
class BudgetSettingsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "BudgetSettingsResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return BudgetSettingsResponse(data)
