m = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
  i = input().split()
  o = set(map(int, input().split()))
  if(i[0]=="intersection_update"):   
    s.intersection_update(o)
  elif(i[0]=='update'):
    s.update(o)
  elif(i[0]=='symmetric_difference_update'):
    s.symmetric_difference_update(o)
  else:
    s.difference_update(o)

print(sum(s))