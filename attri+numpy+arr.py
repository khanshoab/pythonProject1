# n dim :  This attribute represents the no. of  dimensional or axes of the array.
# shape : This attribute represent the shape of the array
# size : This attribute represent the total no. of the element in the array.
# item size : This attribute represent memory size of the array element in the array.
# bytes: This attribute represent the total no. of the bytes occupied by an array.
# d type : This attribute represent the datatype of the array.

from numpy import *
a = array([12,13,14,15,16])
b = array([[21,12,32,43], [34,12,32,43]])
print()
# n dim attribute
print("1D array ndim:",a.ndim)
print("2D array ndim:",b.ndim)
print()
# shape attribute
# for 1d array shape element in the row
# for 2d array shape specifies no. of row and column in each row
print("1D array shape:",a.shape)
print("2D array shape:",b.shape)
print()
# size attribute
print("1D array size:",a.size)
print("2D array size:",b.size)
print()
# item size attribute
print("1D array size:",a.itemsize)
print("2D array size:",b.itemsize)
print()
# dtype attribute
print("1D array size:",a.dtype)
print("2D array size:",b.dtype)
print()
# nbytes attribute
print("1D array size:",a.nbytes)
print("2D array size:",b.nbytes)
print()
