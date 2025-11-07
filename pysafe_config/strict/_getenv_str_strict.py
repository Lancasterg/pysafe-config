import os


def getenv_str_strict(
    var_name: str
) -> str:
    value: str | None = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")
    else:
        try:
            # os.getenv returns a str so this cast to str is not strictly needed
            return str(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to string '{value}'."
            ) from e

