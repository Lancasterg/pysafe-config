import os
import re

_int_pattern = re.compile(r"^[+-]?\d+$")


def _str_to_int(value: str) -> int:
    """
    Converts a string value to an integer by checking value against a regex.

    Args:
        value (str): The string value to convert.

    Returns:
        int: The integer representation of the string.

    Raises:
        ValueError: If the string cannot be converted to an integer
    """
    if _int_pattern.match(value.strip()):
        return int(value)
    else:
        raise ValueError(f"Value must be valid integer '{value}'")


def getenv_int(
    var_name: str, default: int | None = None, required: bool = True
) -> int | None:
    """
    Get the value of an environment variable specified by `var_name`, returned as an integer.

    If the environment variable is not set:
      - If `required` is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If `required` is False, the function returns the default value, which may be
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

    value: str | None = os.getenv(var_name)

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
    Get the value of an environment variable specified by `var_name`, returned as an integer.

    Enforces the return type of integer, the variable is always required otherwise an
    exception is raised

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        int: The integer value of the environment variable.

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
