from typing import TypeVar

__all__ = ["getenv_bool", "getenv_float", "getenv_str", "getenv_int", "getenv_enum"]


def getenv_bool(
    var_name: str, default: bool | None = None, required: bool = True
) -> bool | None:
    from ._getenv_bool import getenv_bool as _getenv_bool_func
    return _getenv_bool_func(var_name, default=default, required=required)


def getenv_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float:
    from ._getenv_float import getenv_float as _getenv_float_func
    return _getenv_float_func(var_name, default=default, required=required)


def getenv_str(
    var_name: str, default: str | None = None, required: bool = True
) -> str | None:
    from ._getenv_str import getenv_str as _getenv_str_func
    return _getenv_str_func(var_name, default=default, required=required)


def getenv_int(var_name: str, default: str | None = None, required: bool = True) -> int | None:
    from ._getenv_int import getenv_int as _getenv_int_func
    return _getenv_int_func(var_name, default=default, required=required)


T = TypeVar("T")


def getenv_enum(
    var_name: str, return_type: T, default: float | None = None, required: bool = True
) -> T:
    from ._getenv_enum import getenv_enum as _getenv_enum_func
    return _getenv_enum_func(var_name, return_type, default=default, required=required)
