# first attempt
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max = 0
        for idx in range(len(nums)-k):
            average = sum(nums[idx:idx+k])/k
            print(nums[idx:idx+k])
            print(idx, average)
            if average > max:
                max = average
        return max
    
#accounting for all negative numbers and list with only one value 
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = sum(nums[:k]) / k
        current_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k] 
            max_avg = max(max_avg, current_sum / k) 
        return max_avg


nums = [1,12,-5,-6,50,3]
k = 4
#expectedOutput: 12.75000
solution = Solution()
print(solution.findMaxAverage(nums, k))