# neetcode solution
class Solution:
        def removeDuplicates(self, nums: list[int]):
            l, r = 0, 0
            while r < len(nums):
                count = 1
                while r+1 < len(nums) and nums[r] == nums[r+1]:
                    r += 1
                    count += 1
                for i in range(min(2, count)):
                    nums[l] = nums[r]
                    l += 1
                r += 1
            return l


# other people's solution
class Solution:
        def removeDuplicates(self, nums: list[int]):
            k = 0
            for val in nums:
                if k < 2 or val != nums[k - 2]:
                    nums[k] = val
                    k += 1
            return k 

# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
# print(removeDuplicates(nums))