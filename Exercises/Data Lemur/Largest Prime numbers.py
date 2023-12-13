def largest_prime_factor(target):
    factors = []
    prime_factors = []
    for i in range(2,target):
        if target % i == 0:
            factors.append(i)
    for j in factors:
        is_prime = True
        for k in range(2, j):
            if j % k == 0:
                is_prime = False
            break
        if is_prime and j > 1:
            prime_factors.append(j)
    return max(list(set(prime_factors)))



def largest_prime_factor(target):
    max_prime_factor = 1

    while target % 2 == 0:
        max_prime_factor = 2
        target //= 2

    for i in range(3, int(target**0.5) + 1, 2):
        while target % i == 0:
            max_prime_factor = i
            target //= i

    if target > 2:
        max_prime_factor = target

    return max_prime_factor