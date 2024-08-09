# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Two pointer solution
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        # [1,2,2,2,3,3,5,7]
        l = 0
        max_count = 0
        for r in range(len(nums)):
            # Move the left pointer if the difference exceeds 1
            while nums[r] - nums[l] > 1:
                l += 1
            # If the current subsequence is harmonious, update max_count
            if nums[r] - nums[l] == 1:
                max_count = max(max_count, r - l + 1)
        return max_count

nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
solution = Solution()
print(solution.findLHS(nums))