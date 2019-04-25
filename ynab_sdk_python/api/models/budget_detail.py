from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional, List

import ynab_sdk_python.utils.parsers as parsers


@dataclass
class Account:
    id: str
    name: str
    type: str
    on_budget: bool
    closed: bool
    note: str
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
        note = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("note"))
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
class Category:
    id: str
    category_group_id: str
    name: str
    hidden: bool
    original_category_group_id: Optional[str]
    note: Optional[str]
    budgeted: int
    activity: int
    balance: int
    goal_type: Optional[str]
    goal_creation_month: Optional[str]
    goal_target: Optional[int]
    goal_target_month: Optional[str]
    goal_percentage_complete: Optional[int]
    deleted: Optional[bool]

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        category_group_id = parsers.from_str(obj.get("category_group_id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_bool(obj.get("hidden"))
        original_category_group_id = parsers.from_union([parsers.from_str, parsers.from_none],
                                                        obj.get("original_category_group_id"))
        note = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("note"))
        budgeted = parsers.from_int(obj.get("budgeted"))
        activity = parsers.from_int(obj.get("activity"))
        balance = parsers.from_int(obj.get("balance"))
        goal_type = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("note"))
        goal_creation_month = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("goal_creation_month"))
        goal_target = parsers.from_union([parsers.from_int, parsers.from_none], obj.get("goal_target"))
        goal_target_month = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("goal_target_month"))
        goal_percentage_complete = parsers.from_union([parsers.from_int, parsers.from_none],
                                                      obj.get("goal_percentage_complete"))
        deleted = parsers.from_bool(obj.get("deleted"))
        return Category(id, category_group_id, name, hidden, original_category_group_id, note, budgeted, activity,
                        balance, goal_type, goal_creation_month, goal_target, goal_target_month,
                        goal_percentage_complete, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["category_group_id"] = parsers.from_str(self.category_group_id)
        result["name"] = parsers.from_str(self.name)
        result["hidden"] = parsers.from_bool(self.hidden)
        result["original_category_group_id"] = parsers.from_str(self.original_category_group_id)
        result["note"] = parsers.from_str(self.note)
        result["budgeted"] = parsers.from_int(self.budgeted)
        result["activity"] = parsers.from_int(self.activity)
        result["balance"] = parsers.from_int(self.balance)
        result["goal_type"] = parsers.from_str(self.goal_type)
        result["goal_creation_month"] = parsers.from_str(self.goal_creation_month)
        result["goal_target"] = parsers.from_int(self.goal_target)
        result["goal_target_month"] = parsers.from_str(self.goal_target_month)
        result["goal_percentage_complete"] = parsers.from_int(self.goal_percentage_complete)
        result["deleted"] = parsers.from_bool(self.deleted)
        return result


@dataclass
class CategoryGroup:
    id: str
    name: str
    hidden: Optional[bool]
    deleted: bool
    transfer_account_id: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> 'CategoryGroup':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_union([parsers.from_bool, parsers.from_none], obj.get("hidden"))
        deleted = parsers.from_bool(obj.get("deleted"))
        transfer_account_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("transfer_account_id"))
        return CategoryGroup(id, name, hidden, deleted, transfer_account_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["name"] = parsers.from_str(self.name)
        result["hidden"] = parsers.from_union([parsers.from_bool, parsers.from_none], self.hidden)
        result["deleted"] = parsers.from_bool(self.deleted)
        result["transfer_account_id"] = parsers.from_union([parsers.from_str, parsers.from_none],
                                                           self.transfer_account_id)
        return result


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
class Month:
    month: str
    note: str
    income: int
    budgeted: int
    activity: int
    to_be_budgeted: int
    age_of_money: Optional[int]
    deleted: bool
    categories: List[Category]

    @staticmethod
    def from_dict(obj: Any) -> 'Month':
        assert isinstance(obj, dict)
        month = parsers.from_str(obj.get("month"))
        note = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("note"))
        income = parsers.from_int(obj.get("income"))
        budgeted = parsers.from_int(obj.get("budgeted"))
        activity = parsers.from_int(obj.get("activity"))
        to_be_budgeted = parsers.from_int(obj.get("to_be_budgeted"))
        age_of_money = parsers.from_union([parsers.from_int, parsers.from_none], obj.get("age_of_money"))
        deleted = parsers.from_bool(obj.get("deleted"))
        categories = parsers.from_list(Category.from_dict, obj.get("categories"))
        return Month(month, note, income, budgeted, activity, to_be_budgeted, age_of_money, deleted, categories)

    def to_dict(self) -> dict:
        result: dict = {}
        result["month"] = parsers.from_str(self.month)
        result["note"] = parsers.from_str(self.note)
        result["income"] = parsers.from_int(self.income)
        result["budgeted"] = parsers.from_int(self.budgeted)
        result["activity"] = parsers.from_int(self.activity)
        result["to_be_budgeted"] = parsers.from_int(self.to_be_budgeted)
        result["age_of_money"] = parsers.from_int(self.age_of_money)
        result["deleted"] = parsers.from_bool(self.deleted)
        result["categories"] = parsers.from_list(lambda x: parsers.to_class(Category, x), self.categories)
        return result


@dataclass
class PayeeLocation:
    id: str
    payee_id: str
    latitude: str
    longitude: str
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'PayeeLocation':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        payee_id = parsers.from_str(obj.get("payee_id"))
        latitude = parsers.from_str(obj.get("latitude"))
        longitude = parsers.from_str(obj.get("longitude"))
        deleted = parsers.from_bool(obj.get("deleted"))
        return PayeeLocation(id, payee_id, latitude, longitude, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["payee_id"] = parsers.from_str(self.payee_id)
        result["latitude"] = parsers.from_str(self.latitude)
        result["longitude"] = parsers.from_str(self.longitude)
        result["deleted"] = parsers.from_bool(self.deleted)
        return result


@dataclass
class Subtransaction:
    id: str
    scheduled_transaction_id: Optional[str]
    amount: int
    memo: str
    payee_id: str
    category_id: str
    transfer_account_id: str
    deleted: bool
    transaction_id: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Subtransaction':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        scheduled_transaction_id = parsers.from_union([parsers.from_str, parsers.from_none],
                                                      obj.get("scheduled_transaction_id"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"), True)
        payee_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("payee_id"))
        category_id = parsers.from_str(obj.get("category_id"))
        transfer_account_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("transfer_account_id"))
        deleted = parsers.from_bool(obj.get("deleted"))
        transaction_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("transaction_id"))
        return Subtransaction(id, scheduled_transaction_id, amount, memo, payee_id, category_id, transfer_account_id,
                              deleted, transaction_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["scheduled_transaction_id"] = parsers.from_union([parsers.from_str, parsers.from_none],
                                                                self.scheduled_transaction_id)
        result["amount"] = parsers.from_int(self.amount)
        result["memo"] = parsers.from_str(self.memo)
        result["payee_id"] = parsers.from_str(self.payee_id)
        result["category_id"] = parsers.from_str(self.category_id)
        result["transfer_account_id"] = parsers.from_str(self.transfer_account_id)
        result["deleted"] = parsers.from_bool(self.deleted)
        result["transaction_id"] = parsers.from_union([parsers.from_str, parsers.from_none], self.transaction_id)
        return result


@dataclass
class ScheduledTransaction:
    id: str
    date_first: str
    date_next: str
    frequency: str
    amount: int
    memo: str
    flag_color: str
    account_id: str
    payee_id: str
    category_id: str
    transfer_account_id: str
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduledTransaction':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        date_first = parsers.from_str(obj.get("date_first"))
        date_next = parsers.from_str(obj.get("date_next"))
        frequency = parsers.from_str(obj.get("frequency"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_str(obj.get("memo"))
        flag_color = parsers.from_str(obj.get("flag_color"), True)
        account_id = parsers.from_str(obj.get("account_id"))
        payee_id = parsers.from_str(obj.get("payee_id"))
        category_id = parsers.from_str(obj.get("category_id"))
        transfer_account_id = parsers.from_str(obj.get("transfer_account_id"), True)
        deleted = parsers.from_bool(obj.get("deleted"))
        return ScheduledTransaction(id, date_first, date_next, frequency, amount, memo, flag_color, account_id,
                                    payee_id, category_id, transfer_account_id, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["date_first"] = parsers.from_str(self.date_first)
        result["date_next"] = parsers.from_str(self.date_next)
        result["frequency"] = parsers.from_str(self.frequency)
        result["amount"] = parsers.from_int(self.amount)
        result["memo"] = parsers.from_str(self.memo)
        result["flag_color"] = parsers.from_str(self.flag_color)
        result["account_id"] = parsers.from_str(self.account_id)
        result["payee_id"] = parsers.from_str(self.payee_id)
        result["category_id"] = parsers.from_str(self.category_id)
        result["transfer_account_id"] = parsers.from_str(self.transfer_account_id)
        result["deleted"] = parsers.from_bool(self.deleted)
        return result


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
    payee_id: str
    category_id: str
    transfer_account_id: Optional[str]
    transfer_transaction_id: Optional[str]
    matched_transaction_id: Optional[str]
    import_id: str
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Transaction':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        date = parsers.from_str(obj.get("date"))
        amount = parsers.from_int(obj.get("amount"))
        memo = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("memo"))
        cleared = parsers.from_str(obj.get("cleared"))
        approved = parsers.from_bool(obj.get("approved"))
        flag_color = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("flag_color"))
        account_id = parsers.from_str(obj.get("account_id"))
        payee_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("payee_id"))
        category_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("category_id"))
        transfer_account_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("transfer_account_id"))
        transfer_transaction_id = parsers.from_union([parsers.from_str, parsers.from_none],
                                                     obj.get("transfer_transaction_id"))
        matched_transaction_id = parsers.from_union([parsers.from_str, parsers.from_none],
                                                    obj.get("matched_transaction_id"))
        import_id = parsers.from_union([parsers.from_str, parsers.from_none], obj.get("import_id"))
        deleted = parsers.from_bool(obj.get("deleted"))
        return Transaction(id, date, amount, memo, cleared, approved, flag_color, account_id, payee_id, category_id,
                           transfer_account_id, transfer_transaction_id, matched_transaction_id, import_id, deleted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["date"] = parsers.from_str(self.date)
        result["amount"] = parsers.from_int(self.amount)
        result["memo"] = parsers.from_str(self.memo)
        result["cleared"] = parsers.from_str(self.cleared)
        result["approved"] = parsers.from_bool(self.approved)
        result["flag_color"] = parsers.from_str(self.flag_color)
        result["account_id"] = parsers.from_str(self.account_id)
        result["payee_id"] = parsers.from_str(self.payee_id)
        result["category_id"] = parsers.from_str(self.category_id)
        result["transfer_account_id"] = parsers.from_str(self.transfer_account_id)
        result["transfer_transaction_id"] = parsers.from_str(self.transfer_transaction_id)
        result["matched_transaction_id"] = parsers.from_str(self.matched_transaction_id)
        result["import_id"] = parsers.from_str(self.import_id)
        result["deleted"] = parsers.from_bool(self.deleted)
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
    accounts: List[Account]
    payees: List[CategoryGroup]
    payee_locations: List[PayeeLocation]
    category_groups: List[CategoryGroup]
    categories: List[Category]
    months: List[Month]
    transactions: List[Transaction]
    subtransactions: List[Subtransaction]
    scheduled_transactions: List[ScheduledTransaction]
    scheduled_subtransactions: List[Subtransaction]

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
        accounts = parsers.from_list(Account.from_dict, obj.get("accounts"))
        payees = parsers.from_list(CategoryGroup.from_dict, obj.get("payees"))
        payee_locations = parsers.from_list(PayeeLocation.from_dict, obj.get("payee_locations"))
        category_groups = parsers.from_list(CategoryGroup.from_dict, obj.get("category_groups"))
        categories = parsers.from_list(Category.from_dict, obj.get("categories"))
        months = parsers.from_list(Month.from_dict, obj.get("months"))
        transactions = parsers.from_list(Transaction.from_dict, obj.get("transactions"))
        subtransactions = parsers.from_list(Subtransaction.from_dict, obj.get("subtransactions"))
        scheduled_transactions = parsers.from_list(ScheduledTransaction.from_dict, obj.get("scheduled_transactions"))
        scheduled_subtransactions = parsers.from_list(Subtransaction.from_dict, obj.get("scheduled_subtransactions"))
        return Budget(id, name, last_modified_on, first_month, last_month, date_format, currency_format, accounts,
                      payees, payee_locations, category_groups, categories, months, transactions, subtransactions,
                      scheduled_transactions, scheduled_subtransactions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["name"] = parsers.from_str(self.name)
        result["last_modified_on"] = self.last_modified_on.isoformat()
        result["first_month"] = parsers.from_str(self.first_month)
        result["last_month"] = parsers.from_str(self.last_month)
        result["date_format"] = parsers.to_class(DateFormat, self.date_format)
        result["currency_format"] = parsers.to_class(CurrencyFormat, self.currency_format)
        result["accounts"] = parsers.from_list(lambda x: parsers.to_class(Account, x), self.accounts)
        result["payees"] = parsers.from_list(lambda x: parsers.to_class(CategoryGroup, x), self.payees)
        result["payee_locations"] = parsers.from_list(lambda x: parsers.to_class(PayeeLocation, x),
                                                      self.payee_locations)
        result["category_groups"] = parsers.from_list(lambda x: parsers.to_class(CategoryGroup, x),
                                                      self.category_groups)
        result["categories"] = parsers.from_list(lambda x: parsers.to_class(Category, x), self.categories)
        result["months"] = parsers.from_list(lambda x: parsers.to_class(Month, x), self.months)
        result["transactions"] = parsers.from_list(lambda x: parsers.to_class(Transaction, x), self.transactions)
        result["subtransactions"] = parsers.from_list(lambda x: parsers.to_class(Subtransaction, x),
                                                      self.subtransactions)
        result["scheduled_transactions"] = parsers.from_list(lambda x: parsers.to_class(ScheduledTransaction, x),
                                                             self.scheduled_transactions)
        result["scheduled_subtransactions"] = parsers.from_list(lambda x: parsers.to_class(Subtransaction, x),
                                                                self.scheduled_subtransactions)
        return result


@dataclass
class Data:
    budget: Budget
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        budget = Budget.from_dict(obj.get("budget"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(budget, server_knowledge)

    def to_dict(self) -> dict:
        result: dict = {}
        result["budget"] = parsers.to_class(Budget, self.budget)
        result["server_knowledge"] = parsers.from_int(self.server_knowledge)
        return result


@dataclass
class BudgetDetailResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BudgetDetailResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return BudgetDetailResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
