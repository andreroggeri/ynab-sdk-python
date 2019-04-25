from dataclasses import dataclass
from typing import Any, List, Optional

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
    payees: List[Payee]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        payees = parsers.from_list(Payee.from_dict, obj.get("payees"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(payees, server_knowledge)

    def to_dict(self) -> dict:
        result: dict = {}
        result["payees"] = parsers.from_list(lambda x: parsers.to_class(Payee, x), self.payees)
        result["server_knowledge"] = parsers.from_int(self.server_knowledge)
        return result


@dataclass
class PayeesResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'PayeesResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return PayeesResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
