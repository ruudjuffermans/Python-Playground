"""userstring.

@see: https://docs.python.org/3/library/collections.html#userstring-objects
@see: https://www.geeksforgeeks.org/collections-userstring-in-python/?ref=lbp

Strings are the arrays of bytes representing Unicode characters. However, Python does not support
the character data type. A character is a string of length one.
"""

from collections import UserString


D = 12344

# Creating an UserDict
userS = UserString(D)
print(userS.data)


# Creating an empty UserDict
userS = UserString("")
print(userS.data)
