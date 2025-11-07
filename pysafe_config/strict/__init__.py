# from typing import TypeVar

__all__ = ["getenv_bool_strict", "_getenv_float_strict", "_getenv_int_strict", "_getenv_str_strict"]


def getenv_bool_strict(
    var_name: str
) -> bool:
    from ._getenv_bool_strict import getenv_bool_strict as _getenv_bool_func

    return _getenv_bool_func(var_name)


def getenv_float(
    var_name: str
) -> float | None:
    from ._getenv_float_strict import getenv_float_strict as _getenv_float_func

    return _getenv_float_func(var_name)


def getenv_str(
    var_name: str
) -> str | None:
    from ._getenv_str_strict import getenv_str_strict as _getenv_str_func

    return _getenv_str_func(var_name)


def getenv_int(
    var_name: str
) -> int | None:
    from ._getenv_int_strict import getenv_int_strict as _getenv_int_func

    return _getenv_int_func(var_name)
