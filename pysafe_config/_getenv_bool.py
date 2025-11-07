import os

#
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


def _str_to_bool(value: str) -> bool:
    """
    Converts a string value to a boolean.

    Checks if the input string (case-insensitive) is present in a set of
    true or false values. If it matches a true value, it returns
    True. If it matches a false value, it returns False.

    Args:
        value (str): The string value to convert.

    Returns:
        bool: The boolean representation of the string.

    Raises:
        ValueError: If the string cannot be converted to a boolean (i.e., it's not
                    in the true or false value sets).
    """
    value = value.lower()
    if value in _true_values:
        return True
    if value in _false_values:
        return False

    raise ValueError(f"Expected {', '.join(_true_values | _false_values)}")


def getenv_bool(
    var_name: str, default: bool | None = None, required: bool = True
) -> bool | None:
    """
    Retrieve the value of an environment variable as a boolean, with optional default
    and enforcement of required presence.

    This function looks up the environment variable specified by var_name. If the
    variable is set, its value is converted to a boolean using `_str_to_bool`.
    If it cannot be converted to a boolean, a ValueError is raised.

    If the environment variable is not set:
      - If required is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If required is False, the function returns the default value, which may be
        None if no default is provided.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        default (bool | None, optional): The value to return if the environment variable
            is not set and required is False. Defaults to None.
        required (bool, optional): Whether the environment variable is mandatory. If True
            and the variable is not set, a RuntimeError is raised. Defaults to True.

    Returns:
        bool | None: The boolean value of the environment variable, or the default if
        the variable is missing and not required.

    Raises:
        ValueError: If the environment variable is set but cannot be converted to a boolean.
        RuntimeError: If the environment variable is required but not set.
    """

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


def getenv_bool_strict(var_name: str) -> bool:
    """
    Retrieve the value of an environment variable as a boolean, and guarantees the
    return type as a boolean.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        bool: The boolean value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is not set.
    """
    value: str | None = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")
    else:
        try:
            return _str_to_bool(value.lower())
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to boolean '{value}'"
            ) from e
