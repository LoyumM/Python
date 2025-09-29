#first attempt: doesnt work
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums) - 1
        min = float('inf')
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                print(i, nums[i], j, nums[j])
                if nums[i] + j >= n:
                    pass
        return n

#greedy solutionx
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0

        for idx in range(n-1):
            farthest = max(farthest, idx + nums[idx])

            if idx == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n -1:
                    break
        return jumps
                

nums = [2,3,1,1,4]
solution = Solution()
print(solution.jump(nums))