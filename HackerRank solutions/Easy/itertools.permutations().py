from itertools import permutations
string,k=input().split()
for permutation in sorted(list(permutations(string,int(k)))):
    print("".join(permutation))
    