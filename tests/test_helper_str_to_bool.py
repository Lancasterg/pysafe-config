import pytest

from pysafe_config._helper_bool import _str_to_bool


@pytest.mark.parametrize(
    "value, expected",
    [
        ("true", True),
        ("1", True),
        ("yes", True),
        ("y", True),
        ("on", True),
        ("enable", True),
        ("enabled", True),
        ("t", True),
        ("false", False),
        ("0", False),
        ("no", False),
        ("n", False),
        ("off", False),
        ("disable", False),
        ("disabled", False),
        ("f", False),
    ],
)
def test_str_to_bool(value: str, expected: bool):
    assert _str_to_bool(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("TRUE", True),
        ("1", True),
        ("YES", True),
        ("Y", True),
        ("ON", True),
        ("ENABLE", True),
        ("ENABLED", True),
        ("T", True),
        ("FALSE", False),
        ("0", False),
        ("NO", False),
        ("N", False),
        ("OFF", False),
        ("DISABLE", False),
        ("DISABLED", False),
        ("F", False),
    ],
)
def test_str_to_bool_upper(value: str, expected: bool):
    assert _str_to_bool(value) == expected


def test_str_to_bool_invalid_value_raise_error():

    with pytest.raises(ValueError):
        _str_to_bool("this is true, but not succinct enough")
