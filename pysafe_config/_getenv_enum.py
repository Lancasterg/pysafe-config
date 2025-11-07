import os
from enum import Enum
from typing import TypeVar

T = TypeVar("T")


def getenv_enum(
    var_name: str, return_type: T, default: float | None = None, required: bool = True
) -> T:
    value: str = os.getenv(var_name)

    if not isinstance(return_type, Enum):
        raise TypeError(f"'return_type' must be Enum '{return_type}'.")

    if value is None and required is True:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    return T
