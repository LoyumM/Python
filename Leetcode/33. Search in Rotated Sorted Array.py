class Solution:
    def search(self, nums: list, target: int):
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else: 
                    high = mid - 1

            #right sorted portion
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else: 
                    mid + 1
            
        return -1