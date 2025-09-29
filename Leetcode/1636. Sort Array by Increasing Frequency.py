# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        nums.sort(key = lambda x: (freq[x], -x))
        # Since Python's sort() function sorts tuples by each element in order, this part ensures that when two elements have the same frequency (freq[x]),
        #  they are sorted in decreasing order based on their value.
        return nums

nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

instance = Solution()
print(instance.frequencySort(nums))