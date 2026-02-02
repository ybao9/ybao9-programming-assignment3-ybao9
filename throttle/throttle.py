"""
Problem 2 — Call Throttler Decorator
"""


def throttle(max_calls=5):
    """
    Decorator that limits how many times a function may be called
    with the same arguments.

    Once a call exceeds max_calls for a given argument combination,
    a RuntimeError should be raised.

    The wrapped function must have an attribute:

        wrapped.call_counts

    which maps argument keys to call counts.
    """
    from functools import wraps

    def decorator(func):
        # You may want a dictionary here to track call counts

        counts = {}

        def norm(x):
            return (type(x), x)

        @wraps(func)
        def wrapper(*args, **kwargs):

            norm_args = tuple(norm(a) for a in args)
            norm_items = []
            if kwargs:
                for k, v in sorted(kwargs.items()):
                    norm_items.append((k, norm(v)))
            in_key = norm_args + tuple(norm_items)

            out_key = args
            if kwargs:
                values = []
                for k, v in sorted(kwargs.items()):
                    values.append(v)
                out_key = args + tuple(values)

            if counts.get(in_key, 0) >= max_calls:
                raise RuntimeError

            counts[in_key] = counts.get(in_key, 0) + 1

            wrapper.call_counts[out_key] = counts[in_key]

            return func(*args, **kwargs)

        # Attach call_counts attribute to the wrapped function
        wrapper.call_counts = counts

        return wrapper

    return decorator

