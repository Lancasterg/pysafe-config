def _str_to_str(value: str) -> str:
    """
    Kind of a pointless function for now as environment variables are read as strings.
    There may be some minute edge case whereby we get to this point and `value` is not a string and therefore this
    function will handle it.

    We could also add validation (against an enum or something) at a later time.

    Args:
        value (str): The string value to convert.

    Returns:
        str: The string representation of the string ;)

    Raises:
        ValueError: If the string cannot be converted to a string

    """
    try:
        return str(value)
    except (ValueError, TypeError) as e:
        raise ValueError(f"{value} cannot be converted into a string") from e
