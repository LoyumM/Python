# brute force method: time complexity (O(n2))
class Solution:
    def maxArea(self, height):
        res = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                length = min(height[i], height[j])
                breadth = j - i
                area = length * breadth
                res = max(res, area)
        return res

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
result = solution.maxArea(height)
print(result)

# time complexity O(n)
class Solution:
    def maxArea(self, height: list[int]):
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            dif = end - start
            min_height = min(height[start], height[end])
            max_area = max(max_area, dif * min_height)
            
            if height[start] < height[end]:
                start += 1
            else :
                end -= 1
        return max_area
    
# suyesh's solution: O(n)
class Solution:
    def maxArea(self, height: list):
        breath = len(height) - 1
        area = 0
        idx_a = 0
        idx_b = -1
        for _ in range(len(height)):
            if height[idx_a] > height[idx_b]:
                area = max(area, height[idx_b] * breath)
                breath -= 1
                idx_a += 1
            else:
                area = max(area, height[idx_a] * breath)
                breath -= 1
                idx_b -= 1
        return area