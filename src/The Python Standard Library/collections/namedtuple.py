"""namedtuple.

@see: https://docs.python.org/3/library/collections.html#collections.namedtuple
@see: https://www.geeksforgeeks.org/namedtuple-in-python/?ref=lbp

In Python, NamedTuple is present inside the collections module. It provides a way to create simple, 
lightweight data structures similar to a class, but without the overhead of defining a full class. 
Like dictionaries, they contain keys that are hashed to a particular value. On the contrary, 
it supports both access from key-value and iteration, the functionality that dictionaries lack.
"""

from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)