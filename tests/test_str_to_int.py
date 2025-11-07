import pytest

from pysafe_config._getenv_int import _str_to_int


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0", 0),
        ("42", 42),
        ("-17", -17),
        ("+99", 99),
        ("123456", 123456),
        ("-0", 0),
        ("+0", 0),
        ("  42  ", 42),  # whitespace allowed
        ("\t-7\n", -7),
    ],
)
def test_str_to_int_valid(value, expected):
    assert _str_to_int(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "",  # empty
        " ",  # whitespace only
        "42.0",  # decimal
        "-3.14",  # negative float
        "+2.5",  # positive float
        ".5",  # leading dot
        "5.",  # trailing dot
        "abc",  # non-numeric
        "1a",  # mixed
        "1 000",  # spaces inside
        "1_000",  # underscores
        "+-42",  # invalid sign
        "--7",  # invalid sign
        "+",  # only plus
        "-",  # only minus
        "NaN",  # special float name
        "inf",  # special float name
    ],
)
def test_str_to_int_invalid(value):
    with pytest.raises(ValueError):
        _str_to_int(value)
