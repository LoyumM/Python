from itertools import combinations

string, k = input().split()
k = int(k)

if 0<k<=len(string):
    for i in range(1, k+1):
        for item in list(combinations(sorted(string), i)):
            print("".join(item))
else:
    print("Try a valid input")