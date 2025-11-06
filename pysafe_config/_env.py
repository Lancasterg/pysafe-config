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


def env_str(var_name: str, default: str | None = None, required: bool = True) -> str | None:
    """
    Retrieve the value of an environment variable as a string, with optional default
    and enforcement of required presence.

    This function looks up the environment variable specified by `var_name`. If the
    variable is set, its value is converted to a string and returned. If it cannot
    be converted to a string, a TypeError is raised.

    If the environment variable is not set:
      - If required is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If required` is False, the function returns the default value, which may be
        None if no default is provided.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        default (str | None, optional): The value to return if the environment variable
            is not set and required is False. Defaults to None.
        required (bool, optional): Whether the environment variable is mandatory. If True
            and the variable is not set, a RuntimeError is raised. Defaults to True.

    Returns:
        str | None: The string value of the environment variable, or the default if
        the variable is missing and not required.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is required but not set.
    """

    value = os.getenv(var_name)
    if value is not None:
        try:
            return str(value)
        except TypeError as e:
            raise TypeError(
                f"Value of environment variable '{var_name}' cannot be converted to integer {value}."
            ) from e

    if required:
        raise RuntimeError(
            f"Missing required environment variable '{var_name}'."
        )

    return default



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
