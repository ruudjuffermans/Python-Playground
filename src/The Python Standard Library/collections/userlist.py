"""userlist.

@see: https://docs.python.org/3/library/collections.html#userlist-objects
@see: https://www.geeksforgeeks.org/collections-userlist-in-python/?ref=lbp

This class acts as a wrapper around list objects. It is a useful base class for your own list-like classes which 
can inherit from them and override existing methods or add new ones. In this way, one can add new behaviors to lists.

The need for this class has been partially supplanted by the ability to subclass directly from list; 
however, this class can be easier to work with because the underlying list is accessible as an attribute.
"""

from collections import UserList
 
 
L = [1, 2, 3, 4]
 
# Creating a userlist
userL = UserList(L)
print(userL.data)
 
 
# Creating empty userlist
userL = UserList()
print(userL.data)
