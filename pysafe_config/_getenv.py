import os
from typing import Callable, Literal, TypeVar, overload

T = TypeVar("T")

_allowed_types = [bool, int, float, str]


@overload
def _getenv(
    var_name: str,
    return_type: type[T],
    helper_function: Callable[[str], T],
    default: T | None = None,
    required: Literal[True] = True,
) -> T: ...
@overload
def _getenv(
    var_name: str,
    return_type: type[T],
    helper_function: Callable[[str], T],
    default: T | None = None,
    required: Literal[False] = False,
) -> T | None: ...
@overload
def _getenv(
    var_name: str,
    return_type: type[T],
    helper_function: Callable[[str], T],
    default: T | None = ...,
    required: bool = ...,
) -> T | None: ...
def _getenv(
    var_name: str,
    return_type: type[T],
    helper_function: Callable[[str], T],
    default: T | None = None,
    required: bool = False,
) -> T | None:
    """
    The function gets the value of an environment variable specified by `var_name` and
    coerces the object into `return_type` via the use of a helper function.

    If the environment variable is not set:
      - If `required` is True, a RuntimeError is raised indicating that the variable
        is mandatory.
      - If `required` is False, the function returns the default value, which may be
        None if no default is provided.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        default (type[T] | None, optional): The value to return if the environment variable
            is not set and required is False. Defaults to None.
        required (bool, optional): Whether the environment variable is mandatory. If True
            and the variable is not set, a RuntimeError is raised. Defaults to False.

    Returns:
        T | None: The value of the environment variable coerced into a `return_type` type, or
                  `default` if the variable is missing and not required.

    Raises:
        TypeError: If the environment variable is set but cannot be converted to a string.
        RuntimeError: If the environment variable is required but not set.
        TypeError: If `return_type` is not in the `allowed_types` set.
                   This may be updated in a future version to include Enums.
    """
    value: str | None = os.getenv(var_name)

    if value is None and required is True:
        raise RuntimeError(f"Missing required environment variable '{var_name}'.")

    elif value is not None and return_type not in _allowed_types:
        raise TypeError(
            f"return_type '{return_type}' "
            f"must be on of [{', '.join([item.__name__ for item in _allowed_types])}]"
        )

    elif value is not None:
        try:
            return helper_function(value)
        except ValueError as e:
            raise ValueError(
                f"Value of environment variable '{var_name}' cannot be converted to {return_type.__name__} '{value}'."
            ) from e
    else:
        return default
