class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k == 0:
            pass
        n = len(nums)
        k = k % n
        nums[n-k:], nums[:n-k] = nums[:n-k],nums[n-k:]