from dataclasses import dataclass
from typing import Any, List, Optional

from ynab_sdk.utils import parsers


@dataclass
class Category:
    category_id: str
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
    def from_dict(obj: Any) -> "Category":
        assert isinstance(obj, dict)
        category_id = parsers.from_str(obj.get("id"))
        category_group_id = parsers.from_str(obj.get("category_group_id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_bool(obj.get("hidden"))
        original_category_group_id = parsers.from_str(
            obj.get("original_category_group_id"), True
        )
        note = parsers.from_str(obj.get("note"), True)
        budgeted = parsers.from_int(obj.get("budgeted"))
        activity = parsers.from_int(obj.get("activity"))
        balance = parsers.from_int(obj.get("balance"))
        goal_type = parsers.from_str(obj.get("goal_type"), True)
        goal_creation_month = parsers.from_str(obj.get("goal_creation_month"), True)
        goal_target = parsers.from_int(obj.get("goal_target"), True)
        goal_target_month = parsers.from_str(obj.get("goal_target_month"), True)
        goal_percentage_complete = parsers.from_int(
            obj.get("goal_percentage_complete"), True
        )
        deleted = parsers.from_bool(obj.get("deleted"))
        return Category(
            category_id,
            category_group_id,
            name,
            hidden,
            original_category_group_id,
            note,
            budgeted,
            activity,
            balance,
            goal_type,
            goal_creation_month,
            goal_target,
            goal_target_month,
            goal_percentage_complete,
            deleted,
        )


@dataclass
class CategoryGroup:
    category_group_id: str
    name: str
    hidden: bool
    deleted: bool
    categories: List[Category]

    @staticmethod
    def from_dict(obj: Any) -> "CategoryGroup":
        assert isinstance(obj, dict)
        category_group_id = parsers.from_str(obj.get("id"))
        name = parsers.from_str(obj.get("name"))
        hidden = parsers.from_bool(obj.get("hidden"))
        deleted = parsers.from_bool(obj.get("deleted"))
        categories = parsers.from_list(Category.from_dict, obj.get("categories"))
        return CategoryGroup(category_group_id, name, hidden, deleted, categories)


@dataclass
class Data:
    category_groups: List[CategoryGroup]
    server_knowledge: int

    @staticmethod
    def from_dict(obj: Any) -> "Data":
        assert isinstance(obj, dict)
        category_groups = parsers.from_list(
            CategoryGroup.from_dict, obj.get("category_groups")
        )
        server_knowledge = parsers.from_int(obj.get("server_knowledge"))
        return Data(category_groups, server_knowledge)


@dataclass
class CategoriesResponse:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> "CategoriesResponse":
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        return CategoriesResponse(data)
