"""deque.

@see: https://docs.python.org/3/library/collections.html#deque-objects
@see: https://www.geeksforgeeks.org/deque-in-python/?ref=lbp

Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is
preferred over a list in the cases where we need quicker append and pop operations from both
the ends of the container, as deque provides an O(1) time complexity for append and pop
operations as compared to a list that provides O(n) time complexity.
"""

import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)
