# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        #[1,4,7,9]
        l, r = 0, k-1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            r += 1
            l += 1
        return res       


nums = [9,4,1,7]
k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

solution = Solution()
print(solution.minimumDifference(nums, k))