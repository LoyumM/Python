# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        d = {}
        answer = []
        for idx, num in enumerate(sorted(nums)):
            if num not in d:
                d[num] = idx
        for num in nums:
            answer.append(d[num])
        return answer

nums = [8,1,2,2,3]
#expected output: nums = [4,0,1,1,3]
instance = Solution()
print(instance.smallerNumbersThanCurrent(nums))