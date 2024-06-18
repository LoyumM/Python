#first solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        new = ""
        for idx in range(n):
            try:
                new = new + word1[idx]
            except IndexError:
                pass
            try:
                new = new + word2[idx]
            except IndexError:
                pass
        return new
    
# a more efficient solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            merged += word1[i] + word2[i]
        if len(word1) > min_length:
            merged += word1[min_length:]
        elif len(word2) > min_length:
            merged += word2[min_length:]
        return merged
            

word1 = "abc"
word2 = "pqrb"
solution = Solution()
print(solution.mergeAlternately(word1, word2))