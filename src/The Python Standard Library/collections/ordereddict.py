"""ordereddict.

@see: https://docs.python.org/3/library/collections.html#ordereddict-objects
@see: https://www.geeksforgeeks.org/ordereddict-in-python/?ref=lbp

Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to
ordering operations. They have become less important now that the built-in dict class gained the
ability to remember insertion order (this new behavior became guaranteed in Python 3.7).
"""

from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4

for key, value in od.items():
    print(key, value)
