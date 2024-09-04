# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.


class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_length = 0

        for idx in range(1, n - 1):
            if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
                left = idx - 1
                right = idx + 1

                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                current_length = right - left + 1
                max_length = max(max_length, current_length)
        return max_length

        


arr = [2,1,4,7,3,2,5]
solution = Solution()
print(solution.longestMountain(arr))