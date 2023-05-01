import numpy as np

n,m = map(int, input().split())
def_arr = []
for i in range(n):
    def_arr.append(list(map(int, input().split())))
arr = np.array(def_arr)

print(np.transpose(arr))
print(arr.flatten())