m = int(input())
eng = set(map(int, input().split()))
n = int(input())
frn = set(map(int, input().split()))

print(len(eng.difference(frn)))