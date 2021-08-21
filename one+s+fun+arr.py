print("creating array using () function")
from numpy import *
a = ones(5)
print(a)
print("using while loop")
n = len(a)
i = 0
while i<n:
    print(a[i])
    i+=1
print("using for loop")
for i in range(n):
    print(a[i])
