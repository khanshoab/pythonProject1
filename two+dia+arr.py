print("accessing one dimensional array using lin space in python")

from numpy import *

a = linspace(1,8,5)
print(a)
print("we also call only one statement")
print(a[3])
print("here we are using for loop")
for element in a:
    print(element)
print("here we can use rnage")
n = len(a)
for i in range(n):
    print('index',i,'=',a[i])

print("we can also using while loop")
i = 0
while i<n:
    print(a[i])
    i+=1