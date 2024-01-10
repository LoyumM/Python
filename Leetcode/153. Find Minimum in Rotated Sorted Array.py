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
    def findMin(self, nums: list) -> int:
        target = nums[0]
        low, high = 0, len(nums) - 1

        while low <= high:
            if nums[low] < nums[high]:
                target = min(target, nums[low])
                break

            mid = (low + high) // 2
            target = min(target, nums[mid])
            
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return target
            
            
nums = [3,4,5,1,2]    
sol_instance = Solution()
res = sol_instance.findMin(nums)
print(res)