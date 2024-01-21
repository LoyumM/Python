# both solution works

class Solution:
    	# def removeDuplicates(self, nums: list[int]) -> int:
	# 	# nums[:] = sorted(set(nums))
	# 	# return len(nums)


# two pointer. 
# advance slow only when the two pointers are different. 
    def removeDuplicates(self, nums:list[int]):
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1
                
        return slow + 1