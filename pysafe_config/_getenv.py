import os
from typing import TypeVar, Callable, Any, Mapping

T = TypeVar("T", bool, int, float, str)


def str2bool(val: str) -> bool:
    return val.lower() in {"true", "1", "yes", "on"}


def str2float(val: str) -> float:
    return float(val)


def str2int(val: str) -> int:
    return int(val)


def str2str(val: str) -> str:
    return val


_CONVERTERS: Mapping[type[bool | int | float | str], Callable[[str], Any]] = {
    bool: str2bool,
    int: str2int,
    float: str2float,
    str: str2str,
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
