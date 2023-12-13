## Problem statement
# Mohan gave Rohan a challenge. Mohan said “I bet you cannot calculate the total number of set bits 
# in every number from 1 to N under 2 seconds.” In the heat of the moment Rohan accepted the challenge. 
# Now he doesn’t know how to achieve this but he doesn’t wanna lose to Mohan either. He asks for your 
# help in achieving this.

## Input format:
# Each Input has One line which contains an integer N.

## Output Format
# Return a Double data type number which is the median of two arrays.

# Solution

n = int(input())
num = 0
for i in range(1,n+1):
    binary = str(bin(i))
    num += binary.count("1")
print(num)