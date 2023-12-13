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