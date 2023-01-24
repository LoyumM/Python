no_of_test = int(input())

for _  in range(no_of_test):
    item_in_a = int(input())
    set_a = set(map(int, input().split()))
    item_in_b = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))