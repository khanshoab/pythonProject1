# Getting input from user in numpy one dimensional array for loop python

from numpy import *
n = int(input("enter the number of the elements: "))
a = zeros(n,dtype=int)

for i in range(len(a)):
    s = input("enter the element: ")
    a[i] = s
print(a)

for i in range(len(a)):
    print(a[i])

# Note: you can use different  method like one etc.