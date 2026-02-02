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

        in_counts = {}
        out_counts= {}

        @wraps(func)
        def wrapper(*args, **kwargs):

            # create a internal key (type)
            typed_args = tuple((type(a), a) for a in args)
            typed_kwargs = tuple(sorted((b, (type(c), c)) for b, c in kwargs.items()))

            in_key = (typed_args, typed_kwargs)

            new_count = in_counts.get(in_key, 0) + 1

            if new_count > max_calls:
                raise RuntimeError

            in_counts[in_key] = new_count

            out_key = args if not kwargs else (args, typed_kwargs)
            out_counts[out_key] = new_count
            out_counts[in_key] = new_count

            return func(*args, **kwargs)

        # Attach call_counts attribute to the wrapped function
        wrapper.call_counts = out_counts

        return wrapper

    return decorator

