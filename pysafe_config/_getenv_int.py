import os
import re

_int_pattern = re.compile(r"^[+-]?\d+$")


def _str_to_int(value: str) -> int:
    if _int_pattern.match(value.strip()):
        return int(value)
    else:
        raise ValueError(f"Value must be valid integer '{value}'")


def getenv_int(
    var_name: str, default: int | None = None, required: bool = True
) -> int | None:
    """
    Retrieve the value of an environment variable as an integer, with optional default
    and enforcement of required presence.

    This function looks up the environment variable specified by var_name. If the
    variable is set, its value is converted to a string and returned. If it cannot
    be converted to a string, a TypeError is raised.

    If the environment variable is not set:
      - If required is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If required` is False, the function returns the default value, which may be
        None if no default is provided.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        default (int | None, optional): The value to return if the environment variable
            is not set and required is False. Defaults to None.
        required (bool, optional): Whether the environment variable is mandatory. If True
            and the variable is not set, a RuntimeError is raised. Defaults to True.

    Returns:
        int | None: The string value of the environment variable, or the default if
        the variable is missing and not required.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is required but not set.
    """

    value = os.getenv(var_name)

    if value is None and required:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    elif value is not None:
        try:
            return _str_to_int(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to integer '{value}'."
            ) from e
    else:
        return default


def getenv_int_strict(var_name: str) -> int:
    """
    Retrieve the value of an environment variable as a float, and guarantees the
    return type as an float.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        float: The integer value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is not set.
    """
    value: str | None = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")
    else:
        try:
            return _str_to_int(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to integer '{value}'."
            ) from e
