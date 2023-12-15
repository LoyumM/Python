def trailing_zeros(n):
    
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n-1)

    n_str = str(factorial(n))
    count = 0
    for char in reversed(n_str):
        if char == '0':
            count += 1
        else:
            break
    return count

print(trailing_zeros(5))
print(trailing_zeros(10))
print(trailing_zeros(130))

# more efficient solution
def trailing_zeroes(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count
