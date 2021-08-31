# Input from user in two 2D array using for loop in python
from numpy import *
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
a = zeros((m,n), dtype=int)

u = len(a)
print(a)
for i in range(u):
    for j in range (len(a[i])):
        x = input("Enter the element: ")
        a[i][j] = x
# with index
for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
print(a)

# without index
for r in a:
    for c in r:
        print(c)

print(a)