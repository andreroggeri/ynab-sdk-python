from dataclasses import dataclass
from typing import Any, List, Optional

from ynab_sdk.utils import parsers


@dataclass
class Subtransaction:
    id: str
    transaction_id: str
    amount: int
    memo: Optional[str]
    payee_id: Optional[str]
    category_id: Optional[str]
    transfer_account_id: Optional[str]
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> "Subtransaction":
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        transaction_id = parsers.from_str(obj.get("transaction_id"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"), True)
        payee_id = parsers.from_str(obj.get("payee_id"), True)
        category_id = parsers.from_str(obj.get("category_id"), True)
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return Subtransaction(
            id,
            transaction_id,
            amount,
            memo,
            payee_id,
            category_id,
            transfer_account_id,
            deleted,
        )


@dataclass
class Transaction:
    id: str
    date: str
    amount: int
    memo: Optional[str]
    cleared: str
    approved: bool
    flag_color: Optional[str]
    account_id: str
    payee_id: Optional[str]
    category_id: Optional[str]
    transfer_account_id: str
    transfer_transaction_id: Optional[str]
    matched_transaction_id: Optional[str]
    import_id: Optional[str]
    deleted: bool
    account_name: str
    payee_name: Optional[str]
    category_name: Optional[str]
    subtransactions: List[Subtransaction]

    @staticmethod
    def from_dict(obj: Any) -> "Transaction":
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        date = parsers.from_str(obj.get("date"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"), True)
        cleared = parsers.from_str(obj.get("cleared"))
        approved = parsers.from_bool(obj.get("approved"))
        flag_color = parsers.from_str(obj.get("flag_color"), True)
        account_id = parsers.from_str(obj.get("account_id"))
        payee_id = parsers.from_str(obj.get("payee_id"), True)
        category_id = parsers.from_str(obj.get("category_id"), True)
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        transfer_transaction_id = parsers.from_str(
            obj.get("transfer_transaction_id"), True
        )
        matched_transaction_id = parsers.from_str(
            obj.get("matched_transaction_id"), True
        )
        import_id = parsers.from_str(obj.get("import_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        account_name = parsers.from_str(obj.get("account_name"))
        payee_name = parsers.from_str(obj.get("payee_name"), True)
        category_name = parsers.from_str(obj.get("category_name"), True)
        subtransactions = parsers.from_list(
            Subtransaction.from_dict, obj.get("subtransactions")
        )
        return Transaction(
            id,
            date,
            amount,
            memo,
            cleared,
            approved,
            flag_color,
            account_id,
            payee_id,
            category_id,
            transfer_account_id,
            transfer_transaction_id,
            matched_transaction_id,
            import_id,
            deleted,
            account_name,
            payee_name,
            category_name,
            subtransactions,
        )


@dataclass
class Data:
    transactions: List[Transaction]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        transactions = parsers.from_list(Transaction.from_dict, obj.get("transactions"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(transactions, server_knowledge)


@dataclass
class TransactionsResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "TransactionsResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return TransactionsResponse(data)
