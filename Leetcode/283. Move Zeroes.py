class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums


nums = [0,0,1,2,0,3,12]
#expOutputOutput: [1,2,3,12,0,0]
solution = Solution()
print(solution.moveZeroes(nums))