# Accessing 2D array using ones () function
from numpy import *
a = ones((3 , 2), dtype=int)
print(a)
# without index number
for i in a:
    for c in a:
        print(c)
    print()
# with index number
from numpy import *
b = ones((2 , 3), dtype=int)
n = len(b)
for i in range(n):
    for j in range(len(a[i])):
        print("index",i,j,"=",a[i][j])
    print()

# using while loop
from  numpy import *
d = ones((4 , 4),dtype=int)
m = len(d)
v = 0
while v < m:
    k = 0
    while k < len(d[v]):
        print("index",v,k,"=",d[v][k])
        k += 1
    v += 1
    print()