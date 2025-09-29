# Given a string s, return the maximum length of a substring
# such that it contains at most two occurrences of each character.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        d = {}
        l = 0

        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
                res = max(res, r - l + 1)
                print(s[l:r+1])
            else:
                d[s[r]] += 1
                if d[s[r]] <= 2:
                    res = max(res, r - l + 1)
                    print(s[l:r+1])
                else:
                    while d[s[r]] > 2:
                        d[s[l]] -= 1
                        l += 1
                    res = max(res, r - l + 1)
                    print(s[l:r+1])
        return res



s = "bcbbbcba"
solution = Solution()
solution.maximumLengthSubstring(s)