# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid:]

        self.sortColors(left_arr)
        self.sortColors(right_arr)

        i = j = k = 0
        # i -> index for left_half
        # j -> index for right_half
        # k -> index for merged nums

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            nums[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            nums[k] = right_arr[j]
            j += 1
            k += 1

        
            


nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
solution = Solution()
print(solution.sortColors(nums))
print(nums)
        