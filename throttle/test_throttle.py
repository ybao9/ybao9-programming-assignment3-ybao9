# tests/test_throttle.py

import pytest

from throttle import throttle


def test_throttle_positional_args_limits_calls():
    @throttle(2)
    def add(a, b):
        add._calls += 1
        return a + b

    add._calls = 0

    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert add._calls == 2

    with pytest.raises(RuntimeError):
        add(1, 2)

    # Do not count failed call as a successful underlying function call
    assert add._calls == 2
    assert add.call_counts[(1, 2)] == 2


def test_throttle_tracks_separate_keys_for_different_args():
    @throttle(2)
    def f(*args, **kwargs):
        f._calls += 1
        return args, kwargs

    f._calls = 0

    f(1)
    f(1)
    with pytest.raises(RuntimeError):
        f(1)

    f(2)
    assert f._calls == 3  # 1,1,2

    assert f.call_counts[(1,)] == 2
    assert f.call_counts[(2,)] == 1


def test_throttle_distinguishes_argument_types():
    @throttle(1)
    def g(x):
        g._calls += 1
        return x

    g._calls = 0

    assert g(3) == 3
    with pytest.raises(RuntimeError):
        g(3)

    assert g(3.0) == 3.0
    with pytest.raises(RuntimeError):
        g(3.0)

    assert g._calls == 2

    assert g.call_counts[(3,)] == 1
    assert g.call_counts[(3.0,)] == 1


def test_throttle_keyword_args_and_ordering():
    @throttle(2)
    def h(*args, **kwargs):
        h._calls += 1
        return args, kwargs

    h._calls = 0

    # same logical kwargs in different order should be treated as the same call signature
    assert h(a=1, b=2) == ((), {"a": 1, "b": 2})
    assert h(b=2, a=1) == ((), {"b": 2, "a": 1})
    assert h._calls == 2

    with pytest.raises(RuntimeError):
        h(a=1, b=2)

    # still only 2 underlying calls
    assert h._calls == 2


def test_throttle_mixed_args_and_kwargs():
    @throttle(1)
    def k(a, b, c=0, d=0):
        k._calls += 1
        return a + b + c + d

    k._calls = 0

    assert k(1, 2, c=3, d=4) == 10
    with pytest.raises(RuntimeError):
        k(1, 2, c=3, d=4)

    assert k(1, 2, c=4, d=4) == 11
    with pytest.raises(RuntimeError):
        k(1, 2, c=4, d=4)

    assert k._calls == 2


def test_throttle_has_call_counts_attr():
    @throttle(2)
    def f(x):
        return x

    assert isinstance(f.call_counts, dict)

