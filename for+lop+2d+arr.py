# Accessing 2D dimensional array for loop
# using without index
from numpy import *
a = array([[10,22,13,12,11],
           [45,34,24,33,23]])
for row in a:
    for col in row:
        print(col)
    print()
# using index
from numpy import *
b = array([[1,2,3,5],
           [6,7,9,10]])
m = len(b)

for i in range(m):
    for j in range(len(b[i])):
        print(b[i][j])
        print()