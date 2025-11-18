import pytest

from pysafe_config import getenv_str


def test_getenv_str_default_unset_required_true(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = getenv_str("MY_API_KEY")

    assert result == expected


def test_getenv_str_default_none_required_false(monkeypatch):
    expected = None

    result = getenv_str("MY_API_KEY", required=False)

    assert result is expected


def test_getenv_str_default_set_required_true(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = getenv_str("MY_API_KEY", required=True)

    assert result == expected


def test_getenv_str_default_set_required_false_raises_exception(monkeypatch):
    with pytest.raises(ValueError):
        _ = getenv_str("MY_API_KEY", default="super_secret_string", required=False)


def test_getenv_str_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_str("MY_API_KEY", required=True)
