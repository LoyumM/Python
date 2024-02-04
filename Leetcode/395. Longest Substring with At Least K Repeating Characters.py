class Solution:            
    def longestSubstring(self, s: str, k: int):
        if k > len(s):
            return 0
                
        freq = {}
        for i, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
        
        longSubstring = 0
        start = 0
        invalidSubstring = False
        for end in range(len(s)):
            if freq[s[end]] < k:
                longSubstring = max(longSubstring, self.longestSubstring(s[start:end], k))
                start = end+1
                invalidSubstring = True
        
        if not invalidSubstring:
            return len(s)
        else:
            return max(longSubstring, self.longestSubstring(s[start:], k))