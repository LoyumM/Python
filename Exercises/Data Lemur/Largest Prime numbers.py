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
    return max(prime_factors)



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False 
    return True 

def largest_prime_factor(target):  
    for i in range(1,target):
        if target%i == 0:
            number = int(target/i)
            if is_prime(number):
                return number
            
print(largest_prime_factor(42))