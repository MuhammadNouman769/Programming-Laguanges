
from email import iterators


def check_type(obj):
    if hasattr(obj, "__iter__") and hasattr(obj, "__next__"):
        return "Iterator"
    elif hasattr(obj, "__iter__"):
        return "Iterable (Not Iterator)"
    else:
        return "Neither"


tests = [[1, 2], "hello", iter([1, 2]), 10, {1: 2}, range(5)]
for t in tests:
    print(repr(t), "->", check_type(t))
    
        