"""
Problem 3 — stream_filter
"""


def stream_filter(items, predicate, limit=None):
    """
    Generator that yields items from `items` for which predicate(item) is True.

    - items: an iterable (may be a generator, may be infinite)
    - predicate: a function returning True/False
    - limit: if None, yield all matches; otherwise stop after yielding `limit` matches

    Must be implemented as a generator function using yield.
    Must be lazy: do not convert `items` to a list.
    """
    count = 0

    for item in items:
        
        if predicate(item):
            yield item
            count += 1

            if limit is not None and count >= limit:
                return

