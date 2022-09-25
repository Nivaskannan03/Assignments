import numpy as np
n, m = list(map(int, input().split()))
lists = []
for i in range(n):
    lists.append(input().split())
lists = np.array(lists, int)
list1 = np.mean(lists , axis = 1)
list2 = np.var(lists, axis = 0)
list3 = np.std(lists)
list3 = round(list3,11 )
print(list1, list2, list3, sep = "\n")
