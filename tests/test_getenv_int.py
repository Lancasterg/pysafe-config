import pytest

from pysafe_config import getenv_int, getenv_int_strict


def test_getenv_int_default_unset_required_true(monkeypatch):
    expected = 15

    monkeypatch.setenv("NUM_BATCHES", "15")

    result = getenv_int("NUM_BATCHES")

    assert result == expected


def test_getenv_int_default_none_required_false(monkeypatch):
    expected = None

    result = getenv_int("NUM_BATCHES", required=False)

    assert result is expected


def test_getenv_int_default_set_required_false(monkeypatch):
    expected = 15

    result = getenv_int("NUM_BATCHES", default=15, required=False)

    assert result == expected


def test_getenv_int_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_int("NUM_BATCHES", default=15, required=True)


def test_getenv_int_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_int("NUM_BATCHES", required=True)


def test_getenv_int_invalid_type_str_raises_exception(monkeypatch):
    monkeypatch.setenv("NUM_BATCHES", "hello")

    with pytest.raises(ValueError):
        _ = getenv_int("NUM_BATCHES")


def test_getenv_int_invalid_type_float_raises_exception(monkeypatch):
    monkeypatch.setenv("NUM_BATCHES", "1.0")

    with pytest.raises(ValueError):
        _ = getenv_int("NUM_BATCHES")


def test_getenv_int_strict_set(monkeypatch):
    expected = 100

    monkeypatch.setenv("NUM_BATCHES", "100")

    result = getenv_int_strict("NUM_BATCHES")

    assert result == expected


def test_getenv_int_strict_invalid_var_raises_exception(monkeypatch):

    monkeypatch.setenv("NUM_BATCHES", "15.3")

    with pytest.raises(ValueError):
        _ = getenv_int_strict("NUM_BATCHES")


def test_getenv_float_strict_unset_raises_exception(monkeypatch):

    with pytest.raises(RuntimeError):
        _ = getenv_int_strict("NUM_BATCHES")


