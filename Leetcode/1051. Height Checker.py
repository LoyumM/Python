class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        v = heights[:]
        cnt = 0

        v.sort()

        for i in range(len(v)):
            if heights[i] != v[i]:
                cnt += 1
        
        return cnt