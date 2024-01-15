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
    def maxArea(self, hit: list[int]):
        mx = 0
        i = 0
        size = len(hit) - 1
        while i < size:
            dif = size - i
            mn = min(hit[i], hit[size])
            mx = max(mx, dif * mn)
            
            if hit[i] < hit[size]:
                i += 1
            else :
                size -= 1
        return mx
    
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
                idx_a -= 1
        return area