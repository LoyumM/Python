# n = int(input())
# list_numbers = [int(input()) for _ in range(n)]

# last_idx = len(list_numbers)-1
# # for idx in range(len(list_numbers)):
# for idx in range(last_idx):
#   print(last_idx)
#   # if list_numbers[idx] == 0 and idx != abs(last_idx):
#   if list_numbers[idx] == 0 :
#     list_numbers[idx],list_numbers[last_idx] = list_numbers[last_idx],list_numbers[idx]
#     last_idx += -1
#     print(list_numbers)
#     print(len(list_numbers))
#     print(last_idx)
# list_strings = [str(number) for number in list_numbers]
# print(' '.join(list_strings))



def move_non_functional_bulbs(arr):
    functional_bulbs = [bulb for bulb in arr if bulb != 0]
    num_non_functional_bulbs = arr.count(0)
    bulbs = functional_bulbs + [0] * num_non_functional_bulbs
    result = [str(bulb) for bulb in bulbs]
    return ' '.join(result)

n = int(input())
arr = [int(input()) for _ in range(n)]
print(move_non_functional_bulbs(arr))