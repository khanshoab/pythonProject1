# Slicing on 2D array
# Slicing on array used to retrieve a piece of the array that contain a group of element.
from numpy import *
n = array([[11,12,13],
           [21,22,23],
           [31,32,33]])
print("Original array")
print(n)
print(n[2])

print("0th row all columns")
a = n[0, :]
print(a)

print("all row 0th column")
a = n[:, 0]
print(a)
for i in a:
    print(i)

print()
# for 11 printing
a = n[0:1, 1:3]
print(a)

print()
# for 34 printing
a = n[2:4, 3:4]
print(a)

# for printing 12,13 and 22,23
print()
a = n[0:2, 1:3]
print(a)
