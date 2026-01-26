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

        def wrapper(*args, **kwargs):
            pass

        # Attach call_counts attribute to the wrapped function
        # Example:
        # wrapper.call_counts = {}

        return wrapper

    return decorator

