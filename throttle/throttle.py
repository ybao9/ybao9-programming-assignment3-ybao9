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

    def decorator(func):
        # You may want a dictionary here to track call counts

        counts = {}
        typed_counts = {}
        
        def wrapper(*args, **kwargs):

            if kwargs:
                key = (args, tuple(sorted(kwargs.items())))
            else:
                key = args

            typed_args = tuple((type(a), a) for a in args)
            if kwargs:
                typed_kwargs = tuple((k, type(v), v) for k, v in sorted(kwargs.items()))
                typed_key = (typed_args, typed_kwargs)
            else:
                typed_key = typed_args

            if typed_key not in typed_counts:
                typed_counts[typed_key] = 0

            if key not in counts:
                counts[key] = 0

            if typed_counts[typed_key] >= max_calls:
                raise RuntimeError

            typed_counts[typed_key] = typed_counts[typed_key] + 1
            counts[key] = counts[key] + 1
            
            return func(*args, **kwargs)

        wrapper.call_counts = counts

        # Attach call_counts attribute to the wrapped function
        # Example:
        # wrapper.call_counts = {}

        return wrapper

    return decorator

