import itertools
import inspect

from stream_filter import stream_filter


def test_stream_filter_basic():
    def is_even(x):
        return x % 2 == 0

    assert list(stream_filter(range(10), is_even)) == [0, 2, 4, 6, 8]


def test_stream_filter_no_matches():
    def always_false(_):
        return False

    assert list(stream_filter([1, 2, 3], always_false)) == []


def test_stream_filter_accepts_generator_input():
    def is_upper(ch):
        return ch.isupper()

    items = (c for c in "aBcDeF")
    assert list(stream_filter(items, is_upper)) == ["B", "D", "F"]


def test_stream_filter_is_generator_object():
    def p(x):
        return True

    g = stream_filter([1, 2, 3], p)
    assert inspect.isgenerator(g)


def test_stream_filter_limit_stops_after_n_matches():
    def is_even(x):
        return x % 2 == 0

    assert list(stream_filter(range(100), is_even, limit=3)) == [0, 2, 4]


def test_stream_filter_limit_none_same_as_part_a():
    def is_even(x):
        return x % 2 == 0

    assert list(stream_filter(range(10), is_even, limit=None)) == [0, 2, 4, 6, 8]


def test_stream_filter_limit_infinite_iterable():
    def is_multiple_of_7(x):
        return x % 7 == 0

    assert list(stream_filter(itertools.count(), is_multiple_of_7, limit=5)) == [0, 7, 14, 21, 28]


def test_stream_filter_limit_is_lazy_does_not_overconsume():
    class SpyIter:
        def __init__(self, data):
            self._it = iter(data)
            self.pulled = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.pulled += 1
            return next(self._it)

    spy = SpyIter([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def is_even(x):
        return x % 2 == 0

    # Need 2 matches: 2 and 4. Should only pull 1,2,3,4 (4 pulls).
    out = list(stream_filter(spy, is_even, limit=2))
    assert out == [2, 4]
    assert spy.pulled == 4

