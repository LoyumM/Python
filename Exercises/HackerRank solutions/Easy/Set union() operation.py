m = int(input())
eng = set(map(int, input().split()))
n = int(input())
frn = set(map(int, input().split()))

both = eng.union(frn)
print(len(both))