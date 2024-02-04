# both solution works

class Solution:
    # def removeDuplicates(self, nums: list[int]) -> int:
	# 	# nums[:] = sorted(set(nums))
	# 	# return len(nums)


# two pointer. 
# advance slow only when the two pointers are different. 
    # def removeDuplicates(self, nums:list[int]):
    #     slow, fast = 0, 1
    #     while fast in range(len(nums)):
    #         if nums[slow] == nums[fast]:
    #             fast += 1
    #         else:
    #             nums[slow+1] = nums[fast]
    #             fast += 1
    #             slow += 1
                
        # return slow + 1
    
#this is also the same as the previous solution:
    def removeDuplicates(self, nums: list[int]):
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        print(nums)
        return j + 1

nums = [0,0,1,1,1,2,2,3,3,4]  
solution = Solution()
print(solution.removeDuplicates(nums))