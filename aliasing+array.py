# Aliasing means it give the existing object.
# it does not copying.
from numpy import *
a = array([10,20,30,40])
b = a
print(a)
print(b)
print("a",id(a))
print("b",id(b))
# Both a and b take the same memory id.
