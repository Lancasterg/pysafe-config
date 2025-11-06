import pytest
from pysafe_config import env_int


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


def test_env_int_invalid_type_raises_exception(monkeypatch):
    monkeypatch.setenv("NUM_BATCHES", "hello")

    with pytest.raises(TypeError):
        _ = env_int("NUM_BATCHES")
