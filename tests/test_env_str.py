import pytest
from pysafe_config import env_str


def test_env_str_default_unset_required_true(monkeypatch):
    expected = "super_secret_string"

    monkeypatch.setenv("MY_API_KEY", "super_secret_string")

    result = env_str("MY_API_KEY")

    assert result == expected


def test_env_str_default_none_required_false(monkeypatch):
    expected = None

    result = env_str("MY_API_KEY", required=False)

    assert result is expected


def test_env_str_default_set_required_false(monkeypatch):
    expected = "super_secret_string"

    result = env_str("MY_API_KEY", default="super_secret_string", required=False)

    assert result == expected


def test_env_str_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = env_str("MY_API_KEY", default="super_secret_string", required=True)


def test_env_str_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = env_str("MY_API_KEY", required=True)
