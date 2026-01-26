# tests/test_comprehensions.py

from comprehensions import even_squares, word_lengths, remove_private


def test_even_squares_basic():
    assert even_squares([1, 2, 3, 4, 5, 6]) == [4, 16, 36]


def test_even_squares_empty():
    assert even_squares([]) == []


def test_even_squares_all_odds():
    assert even_squares([1, 3, 5, 7]) == []


def test_even_squares_negatives_and_zero():
    assert even_squares([-3, -2, -1, 0, 1, 2]) == [4, 0, 4]


def test_word_lengths_basic():
    assert word_lengths(["cat", "elephant", "dog"]) == {"cat": 3, "elephant": 8, "dog": 3}


def test_word_lengths_empty():
    assert word_lengths([]) == {}


def test_word_lengths_duplicates_last_wins_same_length():
    # dict keys must be unique; duplicates should not create extra entries
    assert word_lengths(["hi", "hi", "hello"]) == {"hi": 2, "hello": 5}


def test_remove_private_basic():
    assert remove_private({"a": 1, "_temp": 4, "b": 2}) == {"a": 1, "b": 2}


def test_remove_private_only_private():
    assert remove_private({"_": 1, "_a": 2, "__x": 3}) == {}


def test_remove_private_does_not_mutate_original():
    d = {"a": 1, "_x": 2}
    out = remove_private(d)
    assert out == {"a": 1}
    assert d == {"a": 1, "_x": 2}

