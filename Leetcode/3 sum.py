# Brute Force
# TC: O(n*n*n)
class Solution:
    def threeSum(self, nums:list):
        arrLength = len(nums)

        ans = []

        for i_idx in range(0, arrLength - 2):
            for j_idx in range(i_idx + 1, arrLength - 1):
                for k_idx in range(j_idx + 1, arrLength):
                    if nums[i_idx] + nums[j_idx] + nums[k_idx] == 0:
                        # Sort the triplet and add it to the result if not already present
                        triplet = sorted([nums[i_idx], nums[j_idx], nums[k_idx]])
                        
                        if triplet not in ans:
                            ans.append(triplet)

        return ans

# Two pointer
# TC: O(n*n):
class Solution:
    def threeSum(self, nums:list):
        arrLength = len(nums)

        nums.sort()

        ans = []

        for idx in range(0, arrLength):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            start, end = idx + 1, arrLength - 1
            
            while start < end:
                threeSum = nums[idx] + nums[start] + nums[end]

                if threeSum == 0:
                    ans.append([nums[idx], nums[start], nums[end]])
                
                    while (start < end) and nums[start] == nums[start + 1]:
                        start += 1
                    
                    while (start < end) and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif threeSum < 0:
                    start += 1
                
                else:
                    end -= 1

        return ans