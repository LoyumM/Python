# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

#string manipulation
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        s = list(s)  # Convert to list for mutability
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                del s[i:i + 2]  # Remove both adjacent duplicates
                i = max(i - 1, 0)  # Move one step back to check again
            else:
                i += 1
        return ''.join(s)  # Convert list back to string

#using stacks
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove the duplicate character
            else:
                stack.append(char)  # Add the current character to the stack
        return ''.join(stack)  # Convert stack back to string

# Test
s = "abbaca"
solution = Solution()
print(solution.removeDuplicates(s))  # Output: "ca"
