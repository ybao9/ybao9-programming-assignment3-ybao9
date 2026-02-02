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
            if isinstance(x, float):
                return ("float", x)
            if isinstance(x, bool):
                return ("bool", x)
            return x
      
        @wraps(func)
        def wrapper(*args, **kwargs):
            norm_args = tuple(norm(a) for a in args)

            if kwargs:
                norm_kwargs = tuple((k, norm(v)) for k, v in sorted(kwargs.items()))
                key = norm_args + norm_kwargs
            else:
                key = norm_args

            if counts.get(key, 0) >= max_calls:
                raise RuntimeError

            counts[key] = counts.get(key, 0) + 1
            return func(*args, **kwargs)

        # Attach call_counts attribute to the wrapped function
        wrapper.call_counts = counts

        return wrapper

    return decorator

