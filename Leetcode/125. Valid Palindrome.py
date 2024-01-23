# basic solution: Uses extra memory:
s = "A man, a plan, a canal: Panama"
def ispalindrome(s:str):
    n = ''.join([chr.lower() for chr in s if chr .isalnum()])
    return n == n[::-1]

print(ispalindrome(s))

# Two pointer solution: Consumes no extra memory
class Solution:
    def isPalindrome(self, s: str):
        first, end =  0, len(s) - 1
        while first < end:
            if not s[first].isalnum():
                first += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[first].lower() == s[end].lower():
                first += 1
                end -= 1
            else:
                return False
        return True    
        
solution = Solution()
print(solution.isPalindrome(s))