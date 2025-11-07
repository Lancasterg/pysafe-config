import pytest
from pysafe_config import env_int
from pysafe_config._env import _str_to_int


def test_env_int_default_unset_required_true(monkeypatch):
    expected = 15

    monkeypatch.setenv("NUM_BATCHES", "15")

    result = env_int("NUM_BATCHES")

    assert result == expected


def test_env_int_default_none_required_false(monkeypatch):
    expected = None

    result = env_int("NUM_BATCHES", required=False)

    assert result is expected


def test_env_int_default_set_required_false(monkeypatch):
    expected = 15

    result = env_int("NUM_BATCHES", default=15, required=False)

    assert result == expected


def test_env_int_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = env_int("NUM_BATCHES", default=15, required=True)


def test_env_int_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = env_int("NUM_BATCHES", required=True)


def test_env_int_invalid_type_str_raises_exception(monkeypatch):
    monkeypatch.setenv("NUM_BATCHES", "hello")

    with pytest.raises(ValueError):
        _ = env_int("NUM_BATCHES")


def test_env_int_invalid_type_float_raises_exception(monkeypatch):
    monkeypatch.setenv("NUM_BATCHES", "1.0")

    with pytest.raises(ValueError):
        _ = env_int("NUM_BATCHES")


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
