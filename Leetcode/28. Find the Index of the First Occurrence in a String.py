haystack = "safbsad" 
needle = "sad"


# sad occurs at index 0 and 6, return the first one
# if needle not in haystack:
#     print(-1)
def strStr(needle:str, haystack:str):
    n = len(needle) - 1
    if needle in haystack:
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                if needle[:n] == haystack[i:i+n]:
                    return i
    else:
        return -1
    
    
haystack = "sadbsad" 
needle = "sad"
print(strStr(needle,haystack))
