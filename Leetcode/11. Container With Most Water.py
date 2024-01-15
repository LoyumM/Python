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
    def maxArea(self, hit: List[int]) -> int:
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