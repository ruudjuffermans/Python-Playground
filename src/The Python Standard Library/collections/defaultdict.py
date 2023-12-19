"""defaultdict.

@see: https://docs.python.org/3/library/collections.html#collections.defaultdict
@see: https://www.geeksforgeeks.org/defaultdict-in-python/?ref=lbp

Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a
sub-class of the dictionary class that returns a dictionary-like object. The functionality of
both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises
a KeyError. It provides a default value for the key that does not exists.
"""

from collections import defaultdict


# pylint: disable=C0116
def default_factory():
    return -1


d = defaultdict(default_factory)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
