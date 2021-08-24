# any function - This function returns true, if any one element of the iterable is True.
# if iterable is empty then returns False.
from numpy import *
a = array([1,3,4,5,6])
b = array([2,13,14,15,66])
result = a == b       # Here we can apply any operator
print(any(result))   # If any one element is match then it give True otherwise False
print(all(result))   # All the element should be match then it give True otherwise False
