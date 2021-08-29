# Accessing numpy 2D array using while loop in python.
from numpy import *
a = array([[12,13,14,15],
           [45,56,54,34]])
print(a[0])        # it is print the first row
print(a[1])        # it is print the second row
n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print("index",i,j,"=",a[i][j])
        j += 1
    i += 1
    print()