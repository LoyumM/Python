# time complexity O(n)
class Solution:
    def findMin(self, nums: list):
        min_val = nums[0]
        
        for num in nums:
            if num < min_val:
                min_val = num
                
        return min_val


nums = [3,4,5,1,2]    
sol_instance = Solution()
res = sol_instance.findMin(nums)
print(res)