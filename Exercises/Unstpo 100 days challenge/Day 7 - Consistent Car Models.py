allowed_string = input()
N = int(input())
all_models = input().split()

counter = 0
for model in all_models:
  for character in model:
    if character not in allowed_string:
      counter += 1
print(N - counter)