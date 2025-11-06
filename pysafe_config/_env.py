import os
import sys
from typing import TypeVar

T = TypeVar("T")


def env_any(var_name: str, return_type: T) -> T:
    value = os.getenv(var_name)

    try:
        pass

    except TypeError:
        raise EnvironmentError(
            f"Environment variable '{var_name}' cannot be validated."
        )

    return T


def str2bool(value: str) -> bool:
    _true_set = {"yes", "true", "t", "y", "1"}
    _false_set = {"no", "false", "f", "n", "0"}

    if isinstance(value, str):
        value = value.lower()
        if value in _true_set:
            return True
        if value in _false_set:
            return False

    raise ValueError('Expected "%s"' % '", "'.join(_true_set | _false_set))


def env_int(var_name: str, default: int | None = None, required: bool = True) -> int:
    """Get an integer environment variable.

    Args:
        var_name (str): The name of the environment variable.
        default (int, optional): The default value if the variable is not set. Defaults to 0.
        required: (bool, optional):

    Returns:
        int: The value of the environment variable as an integer.
    """
    try:
        value = int(os.getenv(var_name))

    except TypeError:
        raise EnvironmentError(
            f"Environment variable '{var_name}' cannot be converted to integer."
        )

    if value is None:
        if required:
            if default is not None:
                return default
            raise EnvironmentError(
                f"Environment variable '{var_name}' is required but not set."
            )

    return value


def env_str(var_name: str, default: str | None = None, required: bool = True) -> str:
    """Get a string environment variable.

    Args:
        var_name (str): The name of the environment variable.
        default (str, optional): The default value if the variable is not set. Defaults to "".

    Returns:
        str: The value of the environment variable as a string.
    """
    try:
        value = str(os.getenv(var_name))

    except TypeError:
        raise EnvironmentError(
            f"Environment variable '{var_name}' cannot be converted to string."
        )

    if value is None:
        if required:
            if default is not None:
                return default
            raise EnvironmentError(
                f"Environment variable '{var_name}' is required but not set."
            )

    return value


def env_bool(var_name: str, default: bool | None = None, required: bool = True) -> bool:
    """Get a boolean environment variable.

    Args:
        var_name (str): The name of the environment variable.
        default (bool, optional): The default value if the variable is not set. Defaults to False.

    Returns:
        bool: The value of the environment variable as a boolean.
    """
    try:
        value = str2bool(os.getenv(var_name))

    except TypeError:
        raise EnvironmentError(
            f"Environment variable '{var_name}' cannot be converted to boolean."
        )

    if value is None:
        if required:
            if default is not None:
                return default
            raise EnvironmentError(
                f"Environment variable '{var_name}' is required but not set."
            )

    return value


def env_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float:
    """Get a float environment variable.

    Args:
        var_name (str): The name of the environment variable.
        default (float, optional): The default value if the variable is not set. Defaults to 0.0.

    Returns:
        float: The value of the environment variable as a float.
    """
    try:
        value = float(os.getenv(var_name))

    except TypeError:
        raise EnvironmentError(
            f"Environment variable '{var_name}' cannot be converted to float."
        )

    if value is None:
        if required:
            if default is not None:
                return default
            raise EnvironmentError(
                f"Environment variable '{var_name}' is required but not set."
            )

    return value
