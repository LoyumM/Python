# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def countGoodSubstrings(self, s:str) -> int:
        l = 0
        d = {} # a dict to keep track of number of chr in substring
        count = 0
        for r in range(len(s)):
            if s[r] in d:
                d[s[r]] += 1 #if the same chr occurs more than once in the substring
            else:
                d[s[r]] = 1 # initial occurance

            if r - l + 1 == 3:
                if len(d) == 3: #would only happen if there are no duplicate chr
                    count += 1
                    d[s[l]] -= 1 #to remove the iniital chr in the substr
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
        return count

s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
solution = Solution()
print(solution.countGoodSubstrings(s))