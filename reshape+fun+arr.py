# This function is used to change the shape of the array.
# We also convert 1D ,2D ,3D array and vice versa.
# And new array have the same number of the element as original array.

# 1D to 3D
from numpy import *
a = array([1,2,3,4,5,6,7,8,9,10,11,12])
b = reshape(a, (2, 2, 3))
# (2=no array , 2=no rows , 3=no col)
print(a)
print(b)

# 1D to 3D
from numpy import *
k = array([1,2,3,4,5,6,7,8,9,10,11,12])
j = reshape(a, (2, 3, 2))
# (2=no rows , 3=no col)
print(k)
print(j)
# 2D to 1D
from numpy import *
e = array([[1,2,3], [4,5,6]])
f = reshape(e, (6))
print(e)
print(f)
# Using flatten function
from numpy import *
g = array([[1,2,3], [4,5,6]])
l = g.flatten()
print(g)
print(l)
