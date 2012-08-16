"""Tests for the `ook.decorators.patch` function."""

try:
    reload
except NameError:
    from imp import reload  # pylint: disable=E0611,W0622

import itertools

from types import FunctionType

from ook import patch
from ook.decorators import PY_VERSION
from ook.util import Version

import tests.decorators.examples

from tests import VERSION_ARGS


@patch(itertools, 2.5)
def combinations(iterable, r):  # pylint: disable=C0103
    """Return successive r-length combinations of elements in the iterable."""
    # From <http://docs.python.org/release/2.6/library/itertools.html>.
    # Yes, I'm using `ook.patch()` to test itself. Meta, no?
    pool = tuple(iterable)
    n = len(pool)  # pylint: disable=C0103
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1  # pylint: disable=W0631
        for j in range(i + 1, r):  # pylint: disable=W0631
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def test_exists():
    """`ook.patch` function exists"""
    assert isinstance(patch, FunctionType)


def test_undecorated():
    """`tests.decorators.examples.example()` returns 'undecorated'"""
    reload(tests.decorators.examples)
    assert tests.decorators.examples.example() == "undecorated"


def test_no_args():
    """`ook.patch` function replaces existing `example` fuinction"""
    reload(tests.decorators.examples)

    @patch(tests.decorators.examples)
    def example():
        """Do nothing."""
        pass

    assert tests.decorators.examples.example == example
    assert tests.decorators.examples.example() is None


def check_version_args(*args):
    """`ook.patch` function respects version arguments"""
    reload(tests.decorators.examples)

    @patch(tests.decorators.examples, *args)
    def example():
        """Return a version argument."""
        return args

    if PY_VERSION in map(Version, args):
        assert tests.decorators.examples.example == example
        assert tests.decorators.examples.example() == args
    else:
        assert tests.decorators.examples.example != example
        assert tests.decorators.examples.example() == "undecorated"


def test_version_args():
    """`ook.patch` function respects groups of version arguments"""
    for nargs in range(1, len(VERSION_ARGS) + 1):
        # pylint: disable=E1101
        for args in itertools.combinations(VERSION_ARGS, nargs):
            yield (check_version_args,) + tuple(args)
