import os
import re


_float_pattern = re.compile(r"^[+-]?\d+\.\d+$")
_int_pattern = re.compile(r"^[+-]?\d+$")

_true_values: set[str] = {
    "true",
    "1",
    "yes",
    "y",
    "on",
    "enable",
    "enabled",
    "t",
}

_false_values: set[str] = {
    "false",
    "0",
    "no",
    "n",
    "off",
    "disable",
    "disabled",
    "f",
}


def _str_to_float(value: str) -> float:
    if _float_pattern.match(value.strip()):
        return float(value)
    else:
        raise ValueError(f"Value must be in format 'x.y' {value}")


def _str_to_bool(value: str) -> bool:
    value = value.lower()
    if value in _true_values:
        return True
    if value in _false_values:
        return False

    raise ValueError(f"Expected {', '.join(_true_values | _false_values)}")


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
                f"Value of environment variable '{var_name}' cannot be converted to integer {value}."
            ) from e
    else:
        return default


def getenv_str(
    var_name: str, default: str | None = None, required: bool = True
) -> str | None:
    """
    Retrieve the value of an environment variable as a string, with optional default
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

    value: str = os.getenv(var_name)

    if value is None and required:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")
    elif value is not None:
        try:
            # os.getenv returns a str so this cast to str is not strictly needed
            return str(value)
        except TypeError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to integer {value}."
            ) from e
    else:
        return default


def getenv_bool(
    var_name: str, default: bool | None = None, required: bool = True
) -> bool | None:

    value = os.getenv(var_name)

    if value is None and required:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    if value is not None:
        try:
            return _str_to_bool(value.lower())
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to integer '{value}'\nValue must be in format 'x.y'"
            ) from e
    else:
        return default


def getenv_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float:
    value: str = os.getenv(var_name)

    if value is None and required is True:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    elif value is not None:
        try:
            return _str_to_float(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to float {value}."
            ) from e
    else:
        return default
