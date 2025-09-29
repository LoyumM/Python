# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#obvious solution
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            res.append(num**2)
        res.sort()
        return res
    
# what about a O(n) solution:
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n-1
        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res

nums = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(nums))