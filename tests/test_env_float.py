import pytest
from pysafe_config import getenv_float
from pysafe_config._env import _str_to_float


def test_env_float_default_unset_required_true(monkeypatch):
    expected = 12.9

    monkeypatch.setenv("SAMPLING_RATIO", "12.9")

    result = getenv_float("SAMPLING_RATIO")

    assert result == expected


def test_env_float_default_none_required_false(monkeypatch):
    expected = None

    result = getenv_float("SAMPLING_RATIO", required=False)

    assert result is expected


def test_env_float_default_set_required_false(monkeypatch):
    expected = 12.9

    result = getenv_float("SAMPLING_RATIO", default=12.9, required=False)

    assert result == expected


def test_env_float_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_float("SAMPLING_RATIO", default=12.9, required=True)


def test_env_float_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_float("SAMPLING_RATIO", required=True)


def test_env_float_invalid_type_str_raises_exception(monkeypatch):
    monkeypatch.setenv("SAMPLING_RATIO", "a.b")

    with pytest.raises(ValueError):
        _ = getenv_float("SAMPLING_RATIO")


def test_env_float_invalid_type_float_raises_exception(monkeypatch):
    monkeypatch.setenv("SAMPLING_RATIO", "15")

    with pytest.raises(ValueError):
        _ = getenv_float("SAMPLING_RATIO")

