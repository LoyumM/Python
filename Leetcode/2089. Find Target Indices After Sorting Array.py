# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.


#binary search
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        lessThanEqual = 0
        onlyLess = 0
        for i in nums:
            if i <= target:
                lessThanEqual += 1
            if i < target:
                onlyLess += 1
        return list(range(onlyLess, lessThanEqual))



nums = [1,2,5,2,3]
target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
solution = Solution()
print(solution.targetIndices(nums, target))