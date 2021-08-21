from numpy import *
stu_roll = array([11,12,13,14])
stu_roll[1] = 15
n = len(stu_roll)
for i in range(n):
    print('index',i,'=',stu_roll[i])
