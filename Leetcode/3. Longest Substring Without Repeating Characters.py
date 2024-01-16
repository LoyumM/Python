class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if len(s) in [0,1]:
            return 1
        length = 0
        count = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and count == 0:
                    if (j-i) >= length:
                        length = j - i
                        count += 1
            count = 0
        return length

s = " "
solution = Solution()
print(solution.lengthOfLongestSubstring(s))