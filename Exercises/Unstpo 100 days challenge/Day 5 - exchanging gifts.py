n, m = map(int, input().split())

received = [0] * (n + 1)
given = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    received[b] += 1
    given[a] += 1

def find_youngest_member(n, received, given):
    for i in range(1, n + 1):
        if received[i] == n - 1 and given[i] == 0:
            return i
    return -1

result = find_youngest_member(n, received, given)
print(result)
