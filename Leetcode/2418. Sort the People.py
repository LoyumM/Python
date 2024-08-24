# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

# first attempt: Doesn't work names are repeated
# class Solution:
#     def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
#         d = {}
#         for i in range(len(names)):
#             d[names[i]] = heights[i]
#         sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
#         return list(sorted_d.keys())

# Efficient solution: O(nlogn)
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        sorted_indices = sorted(range(len(heights)), key = lambda x: heights[x], reverse=True) #sort height indices 
        return [names[i] for i in sorted_indices] #sort name by sorted height indices

names = ["Mary","John","Emma"] 
heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

instance = Solution()
print(instance.sortPeople(names, heights))
        
