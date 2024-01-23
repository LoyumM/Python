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
        counter = 0
        idx = len(s) - 1
        while idx >= 0 and s[idx] == ' ':
            idx -= 1
        while idx >= 0 and s[idx] != ' ':
            counter += 1
            idx -= 1
        return counter
