# sad occurs at index 0 and 6, return the first one
# if needle not in haystack:
#     print(-1)
def strStr(needle:str, haystack:str):
    if needle in haystack:
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                if needle[:len(needle)] == haystack[i:i+len(needle)]:
                    return i
    else:
        return -1
    
    
haystack = "safbsad" 
needle = "sad"
print(strStr(needle,haystack))
