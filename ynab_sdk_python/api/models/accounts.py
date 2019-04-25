from dataclasses import dataclass
from typing import Any, List, Optional

import ynab_sdk_python.utils.parsers as parsers


@dataclass
class Account:
    id: str
    name: str
    type: str
    on_budget: bool
    closed: bool
    note: Optional[str]
    balance: int
    cleared_balance: int
    uncleared_balance: int
    transfer_payee_id: str
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Account':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        type = parsers.from_str(obj.get("type"))
        on_budget = parsers.from_bool(obj.get("on_budget"))
        closed = parsers.from_bool(obj.get("closed"))
        note = parsers.from_str(obj.get("note"), True)
        balance = parsers.from_int(obj.get("balance"))
        cleared_balance = parsers.from_int(obj.get("cleared_balance"))
        uncleared_balance = parsers.from_int(obj.get("uncleared_balance"))
        transfer_payee_id = parsers.from_str(obj.get("transfer_payee_id"))
        deleted = parsers.from_bool(obj.get("deleted"))
        return Account(id, name, type, on_budget, closed, note, balance, cleared_balance, uncleared_balance,
                       transfer_payee_id, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["name"] = parsers.from_str(self.name)
        result["type"] = parsers.from_str(self.type)
        result["on_budget"] = parsers.from_bool(self.on_budget)
        result["closed"] = parsers.from_bool(self.closed)
        result["note"] = parsers.from_str(self.note)
        result["balance"] = parsers.from_int(self.balance)
        result["cleared_balance"] = parsers.from_int(self.cleared_balance)
        result["uncleared_balance"] = parsers.from_int(self.uncleared_balance)
        result["transfer_payee_id"] = parsers.from_str(self.transfer_payee_id)
        result["deleted"] = parsers.from_bool(self.deleted)
        return result


@dataclass
class Data:
    accounts: List[Account]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        accounts = parsers.from_list(Account.from_dict, obj.get("accounts"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(accounts, server_knowledge)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accounts"] = parsers.from_list(lambda x: parsers.to_class(Account, x), self.accounts)
        result["server_knowledge"] = parsers.from_int(self.server_knowledge)
        return result


@dataclass
class AccountsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'AccountsResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return AccountsResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
