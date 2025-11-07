__all__ = [
    "getenv_bool",
    "getenv_float",
    "getenv_str",
    "getenv_int",
    "getenv_bool_strict",
    "getenv_float_strict",
    "getenv_int_strict",
    "getenv_str_strict",
]


def getenv_bool(
    var_name: str, default: bool | None = None, required: bool = True
) -> bool | None:
    from pysafe_config._getenv_bool import getenv_bool as _getenv_bool_func

    return _getenv_bool_func(var_name, default=default, required=required)


def getenv_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float | None:
    from pysafe_config._getenv_float import getenv_float as _getenv_float_func

    return _getenv_float_func(var_name, default=default, required=required)


def getenv_str(
    var_name: str, default: str | None = None, required: bool = True
) -> str | None:
    from pysafe_config._getenv_str import getenv_str as _getenv_str_func

    return _getenv_str_func(var_name, default=default, required=required)


def getenv_int(
    var_name: str, default: int | None = None, required: bool = True
) -> int | None:
    from pysafe_config._getenv_int import getenv_int as _getenv_int_func

    return _getenv_int_func(var_name, default=default, required=required)


def getenv_bool_strict(var_name: str) -> bool:
    from ._getenv_bool import getenv_bool_strict as _getenv_bool_func

    return _getenv_bool_func(var_name)


def getenv_float_strict(var_name: str) -> float | None:
    from ._getenv_float import getenv_float_strict as _getenv_float_func

    return _getenv_float_func(var_name)


def getenv_str_strict(var_name: str) -> str | None:
    from ._getenv_str import getenv_str_strict as _getenv_str_func

    return _getenv_str_func(var_name)


def getenv_int_strict(var_name: str) -> int | None:
    from ._getenv_int import getenv_int_strict as _getenv_int_func

    return _getenv_int_func(var_name)


# T = TypeVar("T")
#
#
# def getenv_enum(
#     var_name: str, return_type: T, default: float | None = None, required: bool = True
# ) -> T:
#     from ._getenv_enum import getenv_enum as _getenv_enum_func
#     return _getenv_enum_func(var_name, return_type, default=default, required=required)
