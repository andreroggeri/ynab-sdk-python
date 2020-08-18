import datetime
from typing import Any, Callable, List, Type, TypeVar, cast

import dateutil.parser

T = TypeVar("T")


def from_str(x: Any, nullable=False) -> str:
    try:
        assert isinstance(x, str)
    except AssertionError as ex:
        if nullable:
            return from_none(x)
        else:
            raise ex
    return x


def from_int(x: Any, nullable=False) -> int:
    try:
        assert isinstance(x, int) and not isinstance(x, bool)
    except AssertionError as ex:
        if nullable:
            return from_none(x)
        else:
            raise ex
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False
