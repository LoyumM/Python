#kinda works but very basic logic
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        start, end = 0, 0
        for end in range(len(nums)):
            if nums[end] == val:
                end += 1
            else: #nums[end] != val:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end += 1 

        return sum(1 for element in nums if element != val)
    
    
nums = [0,1,2,2,3,0,4,2]
# nums = [3,2,4,3]
# val = 3
val = 2