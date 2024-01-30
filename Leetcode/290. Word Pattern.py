class Solution:
    def wordPattern(self, pattern: str, s: str):
        t = s
        s = pattern
        t = t.split()
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for idx in range(len(s)):
            chr_s, chr_t = s[idx], t[idx]
            
            if chr_s in dict1:
                if dict1[chr_s] != chr_t:
                    return False    
            else:
                dict1[chr_s] = chr_t
            
            if chr_t in dict2:
                if dict2[chr_t] != chr_s:
                    return False
            else:
                dict2[chr_t] = chr_s
        return True