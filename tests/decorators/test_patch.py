"""Tests for the `ook.decorators.patch` function."""

from types import FunctionType

from ook.decorators import patch


def test_exists():
    """`patch` function exists"""
    assert isinstance(patch, FunctionType)
