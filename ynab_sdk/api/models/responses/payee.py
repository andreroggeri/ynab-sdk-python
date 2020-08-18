from dataclasses import dataclass
from typing import Any, Optional

from ynab_sdk.utils import parsers


@dataclass
class Payee:
    id: str
    name: str
    transfer_account_id: Optional[str]
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> "Payee":
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return Payee(id, name, transfer_account_id, deleted)


@dataclass
class Data:
    payee: Payee

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        payee = Payee.from_dict(obj.get("payee"))
        return Data(payee)


@dataclass
class PayeeResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "PayeeResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return PayeeResponse(data)
