# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  
            mid_number = nums[mid]
            
            if mid_number == target:
                return mid
            elif target > mid_number:  
                left = mid + 1
            else:
                right = mid - 1
                
        return -1  

nums = [-1, 0, 3, 5, 9, 12] 
target = 9
solution = Solution()
print(solution.search(nums, target))

        

nums = [-1,0,3,5,9,12] 
target = 9
solution = Solution()
print(solution.search(nums, target))