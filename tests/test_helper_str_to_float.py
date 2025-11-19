import pytest

from pysafe_config._internal._helpers import _str_to_float


@pytest.mark.parametrize(
    "value, expected",
    [
        # Standard decimal numbers
        ("1.0", 1.0),
        ("0.111111", 0.111111),
        ("10000.2", 10000.2),
        ("-3.14", -3.14),
        ("+2.5", 2.5),
        # With surrounding whitespace (strip should handle)
        ("  3.14  ", 3.14),
        ("\t-2.0\n", -2.0),
        # Zero variants
        ("0.0", 0.0),
        ("-0.0", -0.0),
        ("+0.0", 0.0),
    ],
)
def test_str_to_float_valid(value, expected):
    assert _str_to_float(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        # Integers only — missing decimal point
        "0",
        "42",
        "-7",
        "+99",
        # Empty or whitespace only
        "",
        " ",
        "\t\n",
        # Invalid punctuation
        ".",
        "1.2.3",
        "1..0",
        "..1",
        ".1.",
        "--1.0",
        "+-1.0",
        # Leading dot (no digits before .)
        ".5",
        "-.25",
        "+.9",
        # Trailing dot (no digits after .)
        "5.",
        "-42.",
        "+0.",
        # Non-numeric content
        "abc",
        "1a",
        "1,000",
        "1 000",
        "1_000",
        # Scientific notation (not supported)
        "1e3",
        "-2E-3",
        "+1E+6",
        # Special float names
        "NaN",
        "inf",
        "-inf",
        "+inf",
    ],
)
def test_str_to_float_invalid(value):
    with pytest.raises(ValueError):
        _str_to_float(value)
