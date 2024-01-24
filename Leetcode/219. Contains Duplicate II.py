def containsNearbyDuplicate(nums: list, k: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False
            
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))