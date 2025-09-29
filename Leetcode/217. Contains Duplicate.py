# solution 1
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True 
            else:
                d[num] = 1
        return False

# solutoin 2:
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)