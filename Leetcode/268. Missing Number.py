# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# first attempt
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
#sum of numbers
class Solution:
    def missingNumber(self, nums:list[int]) -> int:
        n = len(nums)
        sum_array = (n * (n + 1))//2
        return sum_array - sum(nums)



nums = [0,1]
solution = Solution()
print(solution.missingNumber(nums))