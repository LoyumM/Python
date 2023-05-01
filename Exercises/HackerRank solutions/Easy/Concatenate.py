import numpy as np

N,M,P  = map(int,input().split())

array_1 = np.array([list(map(int, input().split())) for _ in range(N)])
array_2 = np.array([list(map(int, input().split())) for _ in range(M)])

print(np.concatenate((array_1, array_2), axis = 0))