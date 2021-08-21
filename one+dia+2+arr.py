print("using log space in array")

from numpy import *
a = logspace(1,2,3)
print(a)
print("using for loop")
n = len(a)
for i in range(n):
    print(a[i])
print("using while loop")


