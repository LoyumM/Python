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


# time complexity O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            center = (left + right) // 2
            res = min(res, nums[center])

            if nums[center] >= nums[left]:    
                left = center + 1

            else:
                right = center - 1

        return res
            