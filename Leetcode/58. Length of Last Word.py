# first solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.split()
#         return len(s[-1])

# a more efficient solution: fails when there is a single character
class Solution:
    def lengthOfLastWord(self, s: str):
        n = len(s) - 1
        c = 0
        while n > 0:
            if s[n] == " ":
                n -= 1
            else:# s[n] != " ":
                n -= 1
                c += 1
                if s[n] == " ":
                    break
        return c
    
    
