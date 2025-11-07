import os
import re

from pysafe_config._getenv_int import _str_to_int


def getenv_int_strict(
    var_name: str
) -> int:
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
