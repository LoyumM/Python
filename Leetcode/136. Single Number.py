# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# first attempt
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key, value in d.items():
            if value == 1:
                return key
                break

# bitwise XOR
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR each element with result
        return result


nums = [1,2,2,3,3,4,4,4]
solution = Solution()
print(solution.singleNumber(nums))