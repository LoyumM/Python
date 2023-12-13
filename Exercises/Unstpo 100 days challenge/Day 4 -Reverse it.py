# Enter your code here. Read input from STDIN. Print output to STDOUT

def reverse_it(input_str:str, rev_str:str):
  input_list = [chr for chr in input_str]
  rev_idx = ''
  for i in range(len(input_list)):
    if rev_str == input_list[i]:
      rev_idx = i 
  return ''.join(input_list[:rev_idx]+input_list[rev_idx:][::-1])

input_str, rev_str = input().split()
result = reverse_it(input_str, rev_str)
print(result)
