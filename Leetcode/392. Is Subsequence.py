# first attempt
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        if not t:
            return False 
        left = 0
        for chr in t:
            if chr == s[left]:
                left += 1
                if left == len(s):  # Optimization: stop early if found
                    return True
        return left == len(s)
    
# a better written solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for right in range(len(t)):
            if left < len(s) and t[right] == s[left]:
                left += 1
        return left == len(s)

# same shit but with while loop
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for right in range(len(t)):
            if left < len(s) and t[right] == s[left]:
                left += 1
        return left == len(s)

# Input: 
s = "abc"
t = "ahbgdc"
#expectedOutput: true
solution = Solution()
print(solution.isSubsequence(s, t))
