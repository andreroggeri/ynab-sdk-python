from dataclasses import dataclass
from typing import Any, Optional

import ynab_sdk_python.utils.parsers as parsers


@dataclass
class Payee:
    id: str
    name: str
    transfer_account_id: Optional[str]
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Payee':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return Payee(id, name, transfer_account_id, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["name"] = parsers.from_str(self.name)
        result["transfer_account_id"] = parsers.from_str(self.transfer_account_id)
        result["deleted"] = parsers.from_bool(self.deleted)
        return result


@dataclass
class Data:
    payee: Payee

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        payee = Payee.from_dict(obj.get("payee"))
        return Data(payee)

    def to_dict(self) -> dict:
        result: dict = {}
        result["payee"] = parsers.to_class(Payee, self.payee)
        return result


@dataclass
class PayeeResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'PayeeResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return PayeeResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
