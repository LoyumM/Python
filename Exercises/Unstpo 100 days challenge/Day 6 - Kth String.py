n, k = map(int, input().split())
original_string = input()
reverse_string = original_string[::-1]
print(reverse_string[k-1])