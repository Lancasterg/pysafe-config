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
    value = value.lower()
    if value in _true_values:
        return True
    if value in _false_values:
        return False

    raise ValueError(f"Expected {', '.join(_true_values | _false_values)}")


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


def getenv_bool_strict(var_name: str) -> bool:
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
