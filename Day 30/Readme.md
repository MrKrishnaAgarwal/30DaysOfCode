## Tuples

### What are Tuples?

Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

### Creating Tuples

Tuples are created by placing a comma-separated list of values between parentheses. For example:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
```

Tuples may be nested:

```python
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```
<br>

Source: [Python Docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)