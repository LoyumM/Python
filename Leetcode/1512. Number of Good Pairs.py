# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        d ={}
        count=0
        for i in nums:
            if i in d:
                count += d[i]
                # print(i, count)
                d[i]+=1
            else:
                d[i]=1
        return count

nums = [1,2,3,1,1,3]
# expected output = 4
# Explaination: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
instance = Solution()
print(instance.numIdenticalPairs(nums))

