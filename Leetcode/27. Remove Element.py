# Two pointer solution O(n)
class Solution:
    def removeElement(self, nums: list[int], val: int):
        start, end = 0, 0
        for end in range(len(nums)):
            if nums[end] == val:
                end += 1
            else: #nums[end] != val:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end += 1 
        return start

    
# more optimal solution:
class Solution:
    def removeElement(self, nums: list[int], val: int):

        s = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[s], nums[i] = nums[i], nums[s]
                i += 1
                s += 1
        return s
        
        
        
    
    
nums = [0,1,2,2,3,0,4,2]
# nums = [3,2,4,3]
# val = 3
val = 2
solution = Solution()
print(solution.removeElement(nums, val))