def containsNearbyDuplicate(nums: list, k: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False
            
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d1 = {}
        for key, val in enumerate(nums):
            if val not in d1:
                d1[val] = key
            else:
                if abs(d1.get(val) - key) <= k:
                    return True
                else:
                    d1[val] = key

        return False
    
 
# same solution but a little neater    
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for idx, value in enumerate(nums):
            if value in d and abs(d.get(value) - idx) <= k:
                return True
            else:
                d[value] = idx
        return False