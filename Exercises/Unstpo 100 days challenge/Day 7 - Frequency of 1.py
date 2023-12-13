def count_set_bits(n):
    set_count = 0
    for i in range(1, n + 1):
        set_count += bin(i).count('1')
    return set_count

n = int(input())
print(count_set_bits(n))