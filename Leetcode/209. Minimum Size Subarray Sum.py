'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Attempt: To find a O(n log(n)) time complexity solution
Hint: Sliding window
'''

def minSubArrayLen(target:int, nums: list):
    nums.sort(reverse=True)
    sum = 0
    for idx, value in enumerate(nums):
        sum += value
        if sum >= target:
            return idx + 1
            break
    return 0

# target = 7
# nums = [2,3,1,2,4,3]
nums = [1,1,1,1,1,1,1,1]
target = 11
print(minSubArrayLen(target, nums))
# print(nums)
# nums.sort(reverse=True)
# sum = 0
# for idx, value in enumerate(nums):
#     sum += value
#     if sum >= target:
#         print(idx + 1)
#         break

'''
Brute force: Check every combination. 
First solution: sort list. Go from largest to smallest. Keep adding each element till sum >= target
'''