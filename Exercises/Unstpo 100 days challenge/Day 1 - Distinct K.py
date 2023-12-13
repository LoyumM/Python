# #Problem Statement
# Ashish is provided with a collection of n strings in which some strings are of repeating nature but he has been given 
# with a number k. His task is to find the kth unique string. Also before finding the kth unique string he has to sort 
# each individual string beforehand. If there are fewer unique strings than k return empty string. As his best friend, 
# your task is to help Ashish in accomplishing the task.

## Input format
# The first line contains an integer n denoting the number of strings.
# The next n lines contain strings.
# The next line contains an integer k.

## Output format:
# The output contains the kth distinct string.

# Solution
n = int(input())
lst = [input() for _ in range(n)]
k = int(input())

unique = []
not_unique = []

for strings in lst:
  if strings not in unique:
    unique.append(strings)
  else:
    not_unique.append(strings)

for strings in not_unique:
  unique.remove(strings)

if k > len(unique):
  print("")
else:
  print(unique[k-1])