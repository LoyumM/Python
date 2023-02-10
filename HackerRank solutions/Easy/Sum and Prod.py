import numpy as np

N, M = map(int, input().split())
my_array = [list(map(int, input().split())) for _ in range(N)]

print(np.product(np.sum(my_array, axis = 0)))