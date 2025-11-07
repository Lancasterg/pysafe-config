import pytest

from pysafe_config import getenv_str, getenv_str_strict


def test_getenv_str_default_unset_required_true(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = getenv_str("MY_API_KEY")

    assert result == expected


def test_getenv_str_default_none_required_false(monkeypatch):
    expected = None

    result = getenv_str("MY_API_KEY", required=False)

    assert result is expected


def test_getenv_str_default_set_required_false(monkeypatch):
    expected = "super_secret_string"

    result = getenv_str("MY_API_KEY", default="super_secret_string", required=False)

    assert result == expected


def test_getenv_str_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_str("MY_API_KEY", default="super_secret_string", required=True)


def test_getenv_str_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_str("MY_API_KEY", required=True)


def test_getenv_str_strict_set(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = getenv_str_strict("MY_API_KEY")

    assert result == expected


def test_getenv_str_strict_unset_raises_exception():
    with pytest.raises(RuntimeError):
        _ = getenv_str_strict("MY_API_KEY")
