def factorial(n):
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number you want to calculate the factorial of: "))
print(factorial(n))