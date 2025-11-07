import os
from pysafe_config._getenv_float import _str_to_float


def getenv_float_strict(
    var_name: str
) -> float:
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
