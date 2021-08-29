# Creating two dimensional array using zeros () function.
from numpy import *
a = zeros((3,2), dtype=int)
''' print(a)
print(a[1][0])
for row in a:
    for col in row:
        print(col)
    print() '''
# with index using for loop
n = len(a)
print(n)
for i in range(n):
    for j in range(len(a[i])):
        print("index",i,j,a[i][j])
    print()
# using while loop

from numpy import *
b = zeros((3,3), dtype=int)
m = len(b)
print(m)
o = 0
while o < m:
    k = 0
    while j < len(b[o]):
        print("index",o,j,b[j][k])
        j += 1
    o += 1
    print()
