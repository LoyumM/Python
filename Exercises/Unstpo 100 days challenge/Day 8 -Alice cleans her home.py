n = int(input())
list_numbers = [int(input()) for _ in range(n)]

last_idx = len(list_numbers)-1
for idx in range(len(list_numbers)):
  # if list_numbers[idx] == 0 and idx != abs(last_idx):
  if list_numbers[idx] == 0 :
    list_numbers[idx],list_numbers[last_idx] = list_numbers[last_idx],list_numbers[idx]
    last_idx += -1
    print(list_numbers)
list_strings = [str(number) for number in list_numbers]
print(' '.join(list_strings))


