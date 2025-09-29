# Given two integer arrays nums1 and nums2, return an array of their intersection
# Each element in the result must be unique and you may return the result in any order.

# first attempt
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = {}
        for elem in nums1:
            seen[elem] = 1
        
        res = []
        for elem in nums2:
            if seen.get(elem, -1) == 1:  #-1 is the default value that would be returned if elem is not in seen
                res.append(elem)
                seen[elem] = 0 # handling duplicates

        return res
    

    

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [9,4]
solution = Solution()
print(solution.intersection(nums1, nums2))