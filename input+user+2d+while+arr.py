# Input from user in numpy 2D array using while loop.
from numpy import *
m = int(input("Enter the no of rows: "))
n = int(input("Enter the no of columns: "))
a = zeros((m, n), dtype=int)
print(a)

u = len(a)
print(u)
i = 0
while i < u :
    j = 0
    while j < len(a[i]) :
        x = int(input("Enter the element: "))
        a[i][j] = x
        j += 1
    i += 1
# display code
i = 0
while i < u :
    j = 0
    while j < len(a[i]) :
        print("index",i,j,"=",a[i][j])
        j += 1
    i += 1
print(a)