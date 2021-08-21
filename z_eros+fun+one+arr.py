print("create array with all zeros")
from numpy import *
a = zeros(5)
print(a)
print("using for loop")
n = len(a)
i = 0
while i < n:
    print(a[i])
    i+=1
print("using while loop")
for i in range (n):
    print(a[i])
