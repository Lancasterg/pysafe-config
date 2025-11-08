from pysafe_config._getenv import _getenv_strict, _getenv


__all__ = [
    "getenv_bool",
    "getenv_float",
    "getenv_str",
    "getenv_int",
    "getenv_bool_strict",
    "getenv_float_strict",
    "getenv_int_strict",
    "getenv_str_strict",
]


def getenv_bool(
    var_name: str, default: bool | None = None, required: bool = True
) -> bool | None:
    """
    Get the value of an environment variable specified by `var_name`, returned as a boolean.

    Valid boolean strings are case-insensitive.
    Acceptable values are:

        | True values | False values |
        |--------------|--------------|
        | "true"       | "false"      |
        | "1"          | "0"          |
        | "yes"        | "no"         |
        | "y"          | "n"          |
        | "on"         | "off"        |
        | "enable"     | "disable"    |
        | "enabled"    | "disabled"   |
        | "t"          | "f"          |

    If the environment variable is not set:
      - If `required` is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If `required` is False, the function returns the default value, which may be
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
        TypeError: If the environment variable is set but cannot be converted to a boolean.
        RuntimeError: If the environment variable is required but not set.
    """
    from pysafe_config._helper_bool import _str_to_bool

    return _getenv(var_name, bool, _str_to_bool, default=default, required=required)


def getenv_float(
    var_name: str, default: float | None = None, required: bool = True
) -> float | None:
    """
    Get the value of an environment variable specified by `var_name`, returned as a float.

    If the environment variable is not set:
      - If `required` is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If `required` is False, the function returns the default value, which may be
        None if no default is provided.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        default (float | None, optional): The value to return if the environment variable
            is not set and required is False. Defaults to None.
        required (bool, optional): Whether the environment variable is mandatory. If True
            and the variable is not set, a RuntimeError is raised. Defaults to True.

    Returns:
        float | None: The string value of the environment variable, or the default if
        the variable is missing and not required.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is required but not set.
    """
    from pysafe_config._helper_float import _str_to_float

    return _getenv(var_name, float, _str_to_float, default=default, required=required)


def getenv_str(
    var_name: str, default: str | None = None, required: bool = True
) -> str | None:
    """
    Get the value of an environment variable specified by `var_name`, returned as a string.

    If the environment variable is not set:
      - If `required` is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If required is False, the function returns the default value, which may be
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
    from pysafe_config._helper_str import _str_to_str

    return _getenv(var_name, str, _str_to_str, default=default, required=required)


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

    from pysafe_config._helper_int import _str_to_int

    return _getenv(var_name, int, _str_to_int, default=default, required=required)


def getenv_bool_strict(var_name: str) -> bool:
    """
    Get the value of an environment variable, guaranteeing the return type as a boolean.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        bool: The boolean value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is not set.
    """
    from ._helper_bool import _str_to_bool

    return _getenv_strict(var_name, bool, _str_to_bool)


def getenv_float_strict(var_name: str) -> float:
    """
    Get the value of an environment variable, guaranteeing the return type as a float.

    A single decimal point is required in the variable value otherwise a TypeError will be raised

    Valid float strings must not:
        - Have any whitespace
        - Contain any non-numeric characters other than a
          plus or minus sign at the beginning of the number
          and a decimal point to separate the whole and fractional
          part of the number.


    Some valid examples of integer strings are
        - "50.2"
        - "-0.0"
        - "+1000.5"
        - "-99.0"

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        float: The float value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a float.
        RuntimeError: If the environment variable is not set.
    """
    from ._helper_float import _str_to_float

    return _getenv_strict(var_name, float, _str_to_float)


def getenv_str_strict(var_name: str) -> str:
    """
    Get the value of an environment variable, guaranteeing the return type as a string.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The string value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is not set.
    """
    from ._helper_str import _str_to_str

    return _getenv_strict(var_name, str, _str_to_str)


def getenv_int_strict(var_name: str) -> int:
    """
    Get the value of an environment variable, guaranteeing the return type as an integer.

    Valid integer strings must not:
        - Have any whitespace
        - Contain any non-numeric characters other than a
          plus or minus sign at the beginning of the number

    Some valid examples of integer strings are
        - "100"
        - "1"
        - "-50"
        - "+1000"

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        integer: The integer value of the environment variable.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to an integer.
        RuntimeError: If the environment variable is not set.
    """
    from ._helper_int import _str_to_int

    return _getenv_strict(var_name, int, _str_to_int)
