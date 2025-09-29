# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

# first attempt
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing = []
        for num in range(max(arr)+k+1):
            if num not in arr:
                missing.append(num)
        return missing[k]

#binary search    
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # Number of missing elements before arr[mid]
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # After binary search, left is the smallest index such that the number of missing elements before it is >= k
        # The kth missing number is therefore:
        # arr[right] + (k - number of missing elements before arr[right])
        return left + k


arr = [1,2,3,4]
k = 2
# Output: 2
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
solution = Solution()
print(solution.findKthPositive(arr, k))