[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mutIaKVj)
# Programming Assignment 3

This assignment provides practice with:

• Using comprehensions  
• Functions as objects and closures   
• Generator functions and lazy iteration  
• Decomposing large problems into helper functions  


---

## Problem 1 — Comprehensions

In this problem you will practice using list and dictionary comprehensions.

You may use:

- list comprehensions
- dictionary comprehensions

You may **not** use:

- `for` loops
- `while` loops

---

### Part A — Squares of Even Numbers

Write a function:

```
def even_squares(nums):
    pass
```

that returns a list containing the square of every even number in `nums`.

---

#### Example

```
even_squares([1, 2, 3, 4, 5, 6])
```

returns:

```
[4, 16, 36]
```

---

### Part B — Word Length Dictionary

Write a function:

```
def word_lengths(words):
    pass
```

that returns a dictionary mapping each word to its length.

---

#### Example

```
word_lengths(["cat", "elephant", "dog"])
```

returns:

```
{"cat": 3, "elephant": 8, "dog": 3}
```

---

### Part C — Remove Private Keys

Write a function:

```
def remove_private(data):
    pass
```

that returns a new dictionary containing only entries whose keys do NOT start with `'_'`.

---

#### Example

```
remove_private({"a": 1, "_temp": 4, "b": 2})
```

returns:

```
{"a": 1, "b": 2}
```

---

To test this problem:

```
uv run pytest comprehensions
```

---

## Problem 2 — Call Throttler Decorator

In many systems, functions are “throttled” to prevent excessive usage.

Your task is to write a decorator:

```
throttle(max_calls=5)
```

that wraps a function and limits how many times it may be called with the same arguments.

---

### Behavior

- The wrapped function should accept arbitrary positional and keyword arguments (*args and **kwargs).
- For each unique set of arguments, track how many times it has been called.
- If a call exceeds `max_calls` for that argument combination:
    - Raise a `RuntimeError`
- Otherwise:
    - Call the function normally and return the result.

---

### Additional Requirements

- Different argument types must be tracked separately  
  (for example: `f(3)` and `f(3.0)` are distinct)

- Add a property to the wrapped function:

```
wrapped.call_counts
```

which is a dictionary mapping argument keys to call counts.

---

### Example

```
@throttle(2)
def greet(name):
    print(f"Hello {name}")
    return name

greet("Alice")   # works
greet("Alice")   # works
greet("Alice")   # raises RuntimeError

greet("Bob")     # works
```

After these calls:

```
print(greet.call_counts)
```

Possible output:

```
{("Alice",): 2, ("Bob",): 1}
```

---

To test this problem:

```
uv run pytest throttle
```

---

## Problem 3 — `stream_filter`

In this problem, you will build a generator that processes a stream of values one at a time and selectively produces output based on a condition. This style of programming is useful when working with large datasets or infinite sequences, where it is impractical to store all values in memory at once.


Implement the following generator function:

```
def stream_filter(items, predicate, limit=None):
    pass
```

### Part A — Basic Filtering

- `items` is an iterable (it may be a generator).
- `predicate` is a function that returns `True` or `False`.

The function should:

- observe items one at a time from `items`
- yield only those items for which:

```
predicate(item) is True
```

Example:

```
def is_even(x):
    return x % 2 == 0

list(stream_filter(range(10), is_even))
# [0, 2, 4, 6, 8]
```

---

### Part B — Optional Limit

The parameter `limit` controls how many matching items are yielded.

- If `limit` is `None`, behave exactly like Part A.
- If `limit` is an integer, stop after yielding `limit` matching items.
- Do not continue consuming items from `items` after the limit is reached.

Notes:

- `limit` counts matching items that are yielded, not total inputs observed.
- Your function must work with infinite iterables (such as `itertools.count()`).
- Your function must be lazy: do not convert `items` to a list.

Example:

```
import itertools

def is_multiple_of_7(x):
    return x % 7 == 0

list(stream_filter(itertools.count(), is_multiple_of_7, limit=5))
# [0, 7, 14, 21, 28]
```

To run the tests for this problem:

```
uv run pytest stream_filter
```
