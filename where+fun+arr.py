''' where function - This function is used to create a new array which contains, returned element chosen any
expression . If the condition is true it express the first else second  '''
from numpy import *
a = array([11,12,40,24])
b = array([22,12,14,15])
result = where(a>b, a, b)   # here only compare the array which one is big it print that array
print(result)