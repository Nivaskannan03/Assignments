import numpy as np
list1 = []
for i in range(int(input())):
    li=list(map(float,input().split()))
    list1.append(li)
arr=np.array(list1)
r=np.linalg.det(arr)
print(round(r,2))