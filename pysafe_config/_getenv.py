import os
from typing import TypeVar, Callable, Any, Mapping

from pysafe_config._getenv_bool import _str_to_bool
from pysafe_config._getenv_float import _str_to_float
from pysafe_config._getenv_int import _str_to_int

T = TypeVar("T", bool, int, float, str)


def str_to_str(val) -> str:
    return str(val)


_CONVERTERS: Mapping[type[bool | int | float | str], Callable[[str], Any]] = {
    bool: _str_to_bool,
    int: _str_to_int,
    float: _str_to_float,
    str: str_to_str,
}


def _getenv_strict(var_name: str, return_type: type[T]) -> T:
    value = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    converter = _CONVERTERS.get(return_type)
    if converter is None:
        raise TypeError(f"Unsupported return type: {return_type}")

    try:
        result = converter(value)
    except ValueError as e:
        raise ValueError(
            f"Value of environment variable '{var_name}' cannot be converted to "
            f"{return_type.__name__}: '{value}'"
        ) from e

    # Here we help MyPy understand the narrowing
    if not isinstance(result, return_type):
        raise TypeError(
            f"Converter for {return_type} returned unexpected type: {type(result)}"
        )

    return result
