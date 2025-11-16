import pytest

from pysafe_config import getenv_bool

from typing import get_overloads, get_type_hints
from inspect import isfunction


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


def test_getenv_bool_matches_annotations():
    """
    # TODO: do this first, too tired to figure it out now
    Slightly redundant test as we have type linting for this exact reason,
    but interesting if nothing else.

    We still need to run linting in the ci pipeline anyways:
        - Issue #3 https://github.com/Lancasterg/pysafe-config/issues/3
    """
    expected_num_overloads = 3
    result_overloads = get_overloads(getenv_bool)

    assert len(result_overloads) == expected_num_overloads

    # Test last overloaded function as this should be concrete
    result_concrete = result_overloads[-1]
    assert result_concrete is getenv_bool

    # for func in result_overloads:
    #   check return types, arg types etc
