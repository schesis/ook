"""Tests for the `ook.decorators.patch` function."""

try:
    reload
except NameError:
    from imp import reload  # pylint: disable=redefined-builtin

import itertools

from ook import patch
from ook.decorators import PY_VERSION
from ook.util import Version

import tests.examples

from tests import VERSION_ARGS


def test_undecorated():
    """`tests.examples.basic()` returns 'undecorated'"""
    reload(tests.examples)
    assert tests.examples.basic() == "undecorated"


def check_version_args(kwargs, *args):
    """`ook.patch` function respects version arguments"""
    reload(tests.examples)

    @patch(tests.examples, *args, **kwargs)
    def basic():
        """Return version arguments."""
        return args, kwargs

    ge_min = ("min" not in kwargs) or (PY_VERSION >= Version(kwargs["min"]))
    le_max = ("max" not in kwargs) or (PY_VERSION <= Version(kwargs["max"]))
    matches_specified = (not args) or (PY_VERSION in map(Version, args))
    if matches_specified and ge_min and le_max:
        assert tests.examples.basic == basic
        assert tests.examples.basic() == (args, kwargs)
    else:
        assert tests.examples.basic != basic
        assert tests.examples.basic() == "undecorated"


def test_version_args():
    """`ook.patch` function respects groups of version arguments"""
    for nargs in range(len(VERSION_ARGS) + 1):
        # pylint: disable=no-member
        for args in itertools.combinations(VERSION_ARGS, nargs):
            kwargs = {}
            for keys in ([], ["min"], ["max"], ["min", "max"]):
                for key in keys:
                    for value in VERSION_ARGS:
                        kwargs[key] = value
                yield (check_version_args, kwargs) + tuple(args)
