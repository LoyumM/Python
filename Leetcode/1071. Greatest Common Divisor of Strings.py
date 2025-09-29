# first solutiion
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ln = min(len(str1),len(str2))
        if len(str1) == ln:
            shorter = str1
            longer = str2
        else:
            shorter = str2
            longer =str1
        shortest_sequence = ""
        for idx in range(0,len(shorter)):
            n = idx - 0
            if shorter[:idx] == shorter[idx:idx+n]:
                shortest_sequence = shorter[:idx]
        if int(max(len(str1),len(str2))/len(shortest_sequence)) * shortest_sequence == longer:
            return shortest_sequence
        else:
            return ""
        

# a much more efficient function
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]

str1 = "ABABAB"
str2 = "ABAB"
#expected_output: "AB"
solution = Solution()
print(solution.gcdOfStrings(str1, str2))