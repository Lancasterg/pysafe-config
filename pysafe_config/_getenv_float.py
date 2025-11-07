import os
import re

_float_pattern = re.compile(r"^[+-]?\d+\.\d+$")


def _str_to_float(value: str) -> float:
    """
    Converts a string value to a float by checking value against a regex.
    
    Args:
        value (str): The string value to convert.

    Returns:
        bool: The float representation of the string.

    Raises:
        ValueError: If the string cannot be converted to a float
    """
    if _float_pattern.match(value.strip()):
        return float(value)
    else:
        raise ValueError(f"Value must be in format 'x.y' '{value}'")


def getenv_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float | None:
    value: str | None = os.getenv(var_name)

    if value is None and required is True:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    elif value is not None:
        try:
            return _str_to_float(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to float '{value}'."
            ) from e
    else:
        return default


def getenv_float_strict(var_name: str) -> float:
    """
    Retrieve the value of an environment variable as a float, and guarantees the
    return type as a float.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        float: The float value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is not set.
    """
    value: str | None = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")
    else:
        try:
            return _str_to_float(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to float '{value}'."
            ) from e
