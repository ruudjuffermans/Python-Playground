"""userdict.

@see: https://docs.python.org/3/library/collections.html#userdict-objects
@see: https://www.geeksforgeeks.org/collections-userdict-in-python/?ref=lbp

Python supports a dictionary like a container called UserDict present in the collections module.
This class acts as a wrapper class around the dictionary objects. This class is useful when one
wants to create a dictionary of their own with some modified functionality or with some new
functionality. It can be considered as a way of adding new behaviors to the dictionary.
This class takes a dictionary instance as an argument and simulates a dictionary that is kept
in a regular dictionary. The dictionary is accessible by the data attribute of this class.
"""

from collections import UserDict


D = {"a": 1, "b": 2, "c": 3}

# Creating an UserDict
userD = UserDict(D)
print(userD.data)


# Creating an empty UserDict
userD = UserDict()
print(userD.data)
