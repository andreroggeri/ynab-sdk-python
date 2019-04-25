from dataclasses import dataclass
from typing import Any, Optional

import ynab_sdk_python.utils.parsers as parsers


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
    deleted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        category_group_id = parsers.from_str(obj.get("category_group_id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_bool(obj.get("hidden"))
        original_category_group_id = parsers.from_str(obj.get("original_category_group_id"), True)
        note = parsers.from_str(obj.get("note"), True)
        budgeted = parsers.from_int(obj.get("budgeted"))
        activity = parsers.from_int(obj.get("activity"))
        balance = parsers.from_int(obj.get("balance"))
        goal_type = parsers.from_str(obj.get("goal_type"), True)
        goal_creation_month = parsers.from_str(obj.get("goal_creation_month"), True)
        goal_target = parsers.from_int(obj.get("goal_target"), True)
        goal_target_month = parsers.from_str(obj.get("goal_target_month"), True)
        goal_percentage_complete = parsers.from_int(obj.get("goal_percentage_complete"), True)
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
class Data:
    category: Category

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        category = Category.from_dict(obj.get("category"))
        return Data(category)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category"] = parsers.to_class(Category, self.category)
        return result


@dataclass
class CategoryResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'CategoryResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return CategoryResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
