import pytest

from pysafe_config._internal._helpers import _str_to_str


def test_str_to_str_valid():
    value = "slugs"
    expected = "slugs"

    assert _str_to_str(value) == expected


class NoStringsHere:
    def __str__(self):
        raise TypeError("Not stringable!")


def test_str_to_str_invalid():
    with pytest.raises(TypeError):
        _str_to_str(NoStringsHere())
