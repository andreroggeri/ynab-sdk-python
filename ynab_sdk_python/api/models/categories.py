from dataclasses import dataclass
from typing import Any, List, Optional

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
class CategoryGroup:
    id: str
    name: str
    hidden: bool
    deleted: bool
    categories: List[Category]

    @staticmethod
    def from_dict(obj: Any) -> 'CategoryGroup':
        assert isinstance(obj, dict)
        id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_bool(obj.get("hidden"))
        deleted = parsers.from_bool(obj.get("deleted"))
        categories = parsers.from_list(Category.from_dict, obj.get("categories"))
        return CategoryGroup(id, name, hidden, deleted, categories)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = parsers.from_str(self.id)
        result["name"] = parsers.from_str(self.name)
        result["hidden"] = parsers.from_bool(self.hidden)
        result["deleted"] = parsers.from_bool(self.deleted)
        result["categories"] = parsers.from_list(lambda x: parsers.to_class(Category, x), self.categories)
        return result


@dataclass
class Data:
    category_groups: List[CategoryGroup]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        category_groups = parsers.from_list(CategoryGroup.from_dict, obj.get("category_groups"))
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(category_groups, server_knowledge)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category_groups"] = parsers.from_list(lambda x: parsers.to_class(CategoryGroup, x),
                                                      self.category_groups)
        result["server_knowledge"] = parsers.from_int(self.server_knowledge)
        return result


@dataclass
class CategoriesResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'CategoriesResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return CategoriesResponse(data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = parsers.to_class(Data, self.data)
        return result
