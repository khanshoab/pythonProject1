print("creating array using a_rang e () function ")

from numpy import *
a = arange(2,10,3)
print(a)
print("using for loop")
n = len(a)
for i in range (n):
    print(a[i])
print("using while loop")
i = 0
while i<n:
    print(a[i])
    i+=1