# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        
        #Sort the items by frequency and select the top k
        result = [num for num, freq in count.most_common(k)]
        
        return result
    
# raw

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        unique_elements = list(frequency.keys())
        
        for i in range(len(unique_elements)):
            max_idx = i
            for j in range(i + 1, len(unique_elements)):
                if frequency[unique_elements[j]] > frequency[unique_elements[max_idx]]:
                    max_idx = j
            unique_elements[i], unique_elements[max_idx] = unique_elements[max_idx], unique_elements[i]

        return unique_elements[:k]