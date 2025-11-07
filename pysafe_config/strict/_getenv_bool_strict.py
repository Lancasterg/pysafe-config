import os
from pysafe_config._getenv_bool import _str_to_bool


def getenv_bool_strict(
    var_name: str
) -> bool:
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
