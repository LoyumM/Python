# first solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.split()
#         return len(s[-1])

# a more efficient solution: fails when there is a single character
# class Solution:
#     def lengthOfLastWord(self, s: str):
#         n = len(s) - 1
#         c = 0
#         while n > 0:
#             if s[n] == " ":
#                 n -= 1
#             else:# s[n] != " ":
#                 n -= 1
#                 c += 1
#                 if s[n] == " ":
#                     break
#         return c

# variation of the efficient solution that works with all test cases    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
