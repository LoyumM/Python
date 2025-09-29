def candy_share(a:int, b:int):
    if (a+b) % 2 != 0:
        return -1
        
    operations = 0
    while a != b:
        if a < b:
            b = b - a
            a = 2 * a
        else: 
            a = a - b
            b = 2 * b
        operations += 1
    return operations

# example input
a, b = 7, 1
print(candy_share(a, b))