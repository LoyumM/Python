# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        nicesubstring = ''
        substring = ''
        for windowEnd in range(len(s)):
            for windowStart in range(windowEnd + 1):
                substring = s[windowStart:windowEnd+1]
                
                if (len(set(substring.lower()))) == (len(set(substring))) // 2:
                    nicesubstring = max(nicesubstring,substring,key = len)
                    
        return nicesubstring

s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
solution = Solution()
print(solution.longestNiceSubstring(s))
        