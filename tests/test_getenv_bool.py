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
def test_getenv_bool_passes_validation(value, expected, monkeypatch):
    monkeypatch.setenv("ENABLE_WORMS", value)

    result = getenv_bool("ENABLE_WORMS")
    assert result == expected


def test_getenv_bool_default_set_required_true_raises_exception(monkeypatch):
    with pytest.raises(ValueError):
        _ = getenv_bool("ENABLE_DB", default=False, required=False)


def test_getenv_bool_default_set_required_false(monkeypatch):
    monkeypatch.setenv("ENABLE_DB", "False")
    expected = False
    result = getenv_bool("ENABLE_DB", default=True, required=True)

    assert result is expected


def test_getenv_bool_default_unset_required_true_raises_exception(monkeypatch):
    with pytest.raises(RuntimeError):
        _ = getenv_bool("ENABLE_DB", required=True)
