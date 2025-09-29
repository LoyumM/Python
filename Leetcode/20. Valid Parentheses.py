# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')':'(','}':'{',']':'['}
        stack = []

        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching.keys():
                if stack == [] or matching[char] != stack.pop():
                    return False
            else:
                return False
        
        return stack == [] 
        

s = "()[]{}"
#Output: true
solution = Solution()
print(solution.isValid(s))
