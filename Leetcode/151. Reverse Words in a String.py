class Solution:
    def reverseWords(self, s: str):
        s = s.split(" ")
        s = [item for item in s if item != ""]
        return " ".join(s[::-1])