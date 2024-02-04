class Solution:
    def groupAnagrams(self, strs: list):
        dict = {} 
        for s in strs:
            so ="".join(sorted(s)) 
            if so not in dict:
                dict[so] = [s] 
            else:
                dict[so].append(s)
        return list(dict.values())
        

        
    
    
strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))