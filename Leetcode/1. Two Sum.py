class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            cur_value = nums[i]
            complement = target - cur_value
            if complement in d:
                return [d[complement], i]
            d[cur_value] = i
        