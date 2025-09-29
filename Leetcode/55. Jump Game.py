# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

#first solution
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for num in nums:
            if gas < 0:
                return False
            elif num > gas:
                gas = num
            gas -= 1
        return True
    
# second
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0 
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return False

nums = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(nums))