#Brute-Force: O(n^2)
def two_sum(input: list[int], target: int):
    for i in range(len(input)-1):
        for j in range(i+1,len(input)):
            if input[i] + input[j] == target:
                return [i,j]
    return [-1, -1]

lst = [1, 4, 6, 10] 
target = 10

print(two_sum(lst, target))

# dictionary: O(n)
def two_sum(input: list[int], target) -> list[int]:
    d = {}
    for i in range(len(input)):

        cur_value = input[i]
        complement = target - cur_value
        if complement in d:
            return [d[complement], i]
        d[cur_value] = i
        print(d)

    return [-1, -1]

lst = [1, 4, 6, 10] 
target = 10

print(two_sum(lst, target))