# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = []
        second = []
        
        for chr in s:
            if chr == "#":
                if len(first) x> 0:
                    first.pop()
            else:
                first.append(chr)

        for chr in t:
            if chr == "#":
                if len(second) > 0:  
                    second.pop()
            else:
                second.append(chr)

        return first == second



