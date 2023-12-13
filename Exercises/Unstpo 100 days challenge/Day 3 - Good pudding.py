def is_good_pudding(num):
    num_str = str(num)
    reversed_num = str(int(num_str[::-1]))[::-1]
    return num_str == reversed_num
    
n = int(input())
results = []
for _ in range(n):
    num = int(input())
    results.append(is_good_pudding(num))

for result in results:
    if result:
        print("1")
    else:
        print("0")