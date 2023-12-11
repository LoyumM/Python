# First solution

def count_consistent_cars(allowed_components, all_models, N)
  counter = 0
  for model in all_models:
    for character in model:
      if character not in allowed_string:
        counter += 1
  return N - counter

allowed_string = input()
N = int(input())
all_models = input().split()
print(count_consistent_cars(allowed_components, all_models, N))


## using sets


def count_consistent_cars(allowed_components, n, car_models):
    allowed_set = set(allowed_components)
    consistent_count = 0
    for model in car_models:
        if set(model).issubset(allowed_set):
            consistent_count += 1
    return consistent_count

allowed_components = input()
N = int(input())
car_models = input().split()
print(count_consistent_cars(allowed_components, N, car_models)