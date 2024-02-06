class Solution:
    def fourSum(self, nums: list, target: int):
        nums.sort()
        s = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[i] + nums[j] + nums[l] + nums[r]<target:
                        l+=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]>target:
                        r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r]==target:
                        s.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return list(s)
    
# a more general approach
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            lo, hi = 0, len(nums) - 1
            res = []
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total < target:
                    lo += 1
                elif total > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]: hi -= 1
            return res
                    
        def kSum(nums, target, k):
            if not nums:
                return []
            
            avg = target // k
            if nums[0] > avg or nums[-1] < avg:
                return []
        
            if k == 2:
                return twoSum(nums, target)
            
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue
                for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
            
            return res
            
        nums.sort()
        return kSum(nums, target, 4)