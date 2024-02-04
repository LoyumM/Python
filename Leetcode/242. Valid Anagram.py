# using sort(): O(logn) time complexity
class Solution:
    def isAnagram(self, s: str, t: str):
        return sorted(s) == sorted(t)


# two pointer solution using hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            count_s={}
            count_t={}
            for char in s:
                count_s[char] = count_s.get(char,0)+1
            for char in t:
                count_t[char] = count_t.get(char,0)+1
            if count_t == count_s:
                return True
        return False

        