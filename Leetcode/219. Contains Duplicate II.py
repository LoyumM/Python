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
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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