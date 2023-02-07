string, k = input().split()
k = int(k)

from itertools import combinations_with_replacement

for item in list(combinations_with_replacement(sorted(string),k)):
    print(*item,sep="")
