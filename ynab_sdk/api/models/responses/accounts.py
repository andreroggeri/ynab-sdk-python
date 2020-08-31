from dataclasses import dataclass
from typing import Any, List, Optional

from ynab_sdk.utils import parsers


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
    transfer_payee_id: Optional[str]
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> "Account":
        assert isinstance(obj, dict)
        account_id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        account_type = parsers.from_str(obj.get("type"))
        on_budget = parsers.from_bool(obj.get("on_budget"))
        closed = parsers.from_bool(obj.get("closed"))
        note = parsers.from_str(obj.get("note"), True)
        balance = parsers.from_int(obj.get("balance"))
        cleared_balance = parsers.from_int(obj.get("cleared_balance"))
        uncleared_balance = parsers.from_int(obj.get("uncleared_balance"))
        transfer_payee_id = parsers.from_str(obj.get("transfer_payee_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return Account(
            account_id,
            name,
            account_type,
            on_budget,
            closed,
            note,
            balance,
            cleared_balance,
            uncleared_balance,
            transfer_payee_id,
            deleted,
        )


@dataclass
class Data:
    accounts: List[Account]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        accounts = parsers.from_list(Account.from_dict, obj.get("accounts"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(accounts, server_knowledge)


@dataclass
class AccountsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "AccountsResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return AccountsResponse(data)
