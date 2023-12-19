"""chainmap.

@see: https://docs.python.org/3/library/collections.html#chainmap-objects
@see: https://www.geeksforgeeks.org/chainmap-in-python/?ref=lbp

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

The class can be used to simulate nested scopes and is useful in templating.
"""

import collections 
  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap using map 
print ("All the ChainMap contents are : ") 
print (chain.maps) 
  
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
  
# printing chainMap using map 
print ("Displaying new ChainMap : ") 
print (chain1.maps) 
  
# displaying value associated with b before reversing 
print ("Value associated with b before reversing is : ",end="") 
print (chain1['b']) 
  
# reversing the ChainMap 
chain1.maps = reversed(chain1.maps) 
  
# displaying value associated with b after reversing 
print ("Value associated with b after reversing is : ",end="") 
print (chain1['b']) 