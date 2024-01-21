# obvious solution:
# time complexity of O(n2)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for key, val in d.items():
            if val > (len(nums)/2):
                return key
            
            
# sample test case:
nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))

# timc compelxity O(nlogn)
# a little cheating
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
