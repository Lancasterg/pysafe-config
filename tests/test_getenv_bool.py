import pytest

from pysafe_config import getenv_bool


def test_getenv_bool_default_true_unset_required_true(monkeypatch):
    expected = True

    monkeypatch.setenv("ENABLE_DB", "true")

    result = getenv_bool("ENABLE_DB")

    assert result is expected


def test_getenv_bool_default_false_unset_required_true(monkeypatch):
    expected = False

    monkeypatch.setenv("ENABLE_DB", "false")

    result = getenv_bool("ENABLE_DB")

    assert result is expected


def test_getenv_bool_default_none_required_false(monkeypatch):
    expected = None

    result = getenv_bool("ENABLE_DB", required=False)

    assert result is expected


def test_getenv_bool_default_set_required_false(monkeypatch):
    expected = False

    result = getenv_bool("ENABLE_DB", default=False, required=False)

    assert result is expected


def test_getenv_bool_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_bool("ENABLE_DB", default=True, required=True)


def test_getenv_bool_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_bool("ENABLE_DB", required=True)
