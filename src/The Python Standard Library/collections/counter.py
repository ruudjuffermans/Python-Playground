"""counter.

@see: https://docs.python.org/3/library/collections.html#collections.Counter
@see: https://www.geeksforgeeks.org/defaultdict-in-python/?ref=lbp

A Counter is a dict subclass for counting hashable objects. It is a collection where elements are
stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to
be any integer value including zero or negative counts. The Counter class is similar to bags or
multisets in other languages.
"""

from collections import Counter

a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

x = Counter(a)

print(x)

# pylint: disable=C0206
for i in x.keys():
    print(i, ":", x[i])

x_keys = list(x.keys())
x_values = list(x.values())

print(x_keys)
print(x_values)
