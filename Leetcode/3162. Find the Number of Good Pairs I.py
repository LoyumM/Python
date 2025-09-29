# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
# Return the total number of good pairs.

# # brute force: time complexity O(n**2)
# class Solution:
#     def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] % (nums2[j] * k) == 0:
#                     count += 1
#         return count
    
# using hashmaps
from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        key_map = defaultdict(int) # using a default dict for creating a dict for the function type int
        for i in nums2:
            key_map[i*k] += 1
        count = 0 
        for num in nums1:
            for key in key_map:
                if num % key == 0:
                    count += key_map[key] # for the case when the numbers in nums2 are repeated 
        return count



nums1 = [1,3,4] 
nums2 = [1,3,4]
k = 1
#expected output = 5
# Explanation:
# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
instance = Solution()
print(instance.numberOfPairs(nums1, nums2, k))