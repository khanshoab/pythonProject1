# view method : it is to construct a new view of array with same data type of existing array.
# new and existing array will share different memory location .
# if new array get modified then will also be modified as then in both the array will be mirror image.

from numpy import *
a = array([12,13,14,15])
b = a.view()
a[1] = 40
b[3] = 50
print(a)
print(b)
print(a,id(a))
print(b,id(b))

# copy method : this method is used to create a copy of an existing array.
# if the new array modified the existing array will not be effected.
# both the array is independent

from numpy import*
a = array([12,23,45,56])
b = copy(a)
a[1] = 70
b[2] = 80
print(a)
print(b)
print(a,id(a))
print(b,id(b))