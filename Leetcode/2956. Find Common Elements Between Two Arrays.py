# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].

class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = 0
        count2 = 0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count1 += 1
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                count2 += 1
        
        return [count1, count2]
    
nums1 = [2,3,2]
nums2 = [1,2]
# expected output = [2,1]
solution = Solution()
print(solution.findIntersectionValues(nums1, nums2))
