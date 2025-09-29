# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



# hashmap solution
class Solution:
    def intersect(self, nums1:list[int], nums2:list[int]) -> list[int]:
        freq1 = {}
        freq2 = {}

        # Store frequencies of nums1:
        for num in nums1:
            if num in freq1:
                freq1[num] += 1
            else:
                freq1[num] = 1

        # Store frequencies of nums2:
        for num in nums2:
            if num in freq2:
                freq2[num] += 1
            else:
                freq2[num] = 1

        result = []

        for num in freq1:
            if num in freq2:
                count = min(freq1[num], freq2[num])
                result.extend([num] * count)

        return result

#quicksort
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)
        
        nums1 = quicksort(nums1)
        nums2 = quicksort(nums2)
        
        i, j = 0, 0
        result = []
        
        # Use two pointers to find intersection
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result


# Example usage
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
solution = Solution()
print(solution.intersect(nums1, nums2))  # Output: [4,9]
