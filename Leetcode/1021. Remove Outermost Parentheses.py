# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


#using stacks
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stacks = []
        results = []

        for chr in s:
            if chr == "(":
                if stacks:
                    results.append(chr)
                stacks.append(chr)
            else:
                stacks.pop()
                if stacks:
                    results.append(chr)
        
        return ''.join(results)


# counter based
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        open_count = 0
        
        for char in s:
            if char == '(':
                if open_count > 0:
                    result.append(char)  # Add only if it's not the outermost '('
                open_count += 1
            else:
                open_count -= 1
                if open_count > 0:
                    result.append(char)  # Add only if it's not the outermost ')'
        
        return ''.join(result)


s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
solution = Solution()
print(solution.removeOuterParentheses(s))