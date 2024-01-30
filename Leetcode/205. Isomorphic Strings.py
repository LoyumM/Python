# s = "egg"
# t = "add"

# d1 = {}
# d2 = {}
# for value in s:
#     count = 1
#     if value not in d1:
#         d1[value] =  count
#     else:
#         count += 1
#         d1[value] = count
# for value in t:
#     count = 1
#     if value not in d2:
#         d2[value] =  count
#     else:
#         count += 1
#         d2[value] = count        
# print(d1 == d2)


def isIsomorphic(s: list, t: list):
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



# def isIsomorphic(s, t):
#     if len(s) != len(t):
#         return False

#     mapping_s_to_t = {}
#     mapping_t_to_s = {}

#     for char_s, char_t in zip(s, t):
#         if char_s in mapping_s_to_t:
#             if mapping_s_to_t[char_s] != char_t:
#                 return False
#         else:
#             mapping_s_to_t[char_s] = char_t

#         if char_t in mapping_t_to_s:
#             if mapping_t_to_s[char_t] != char_s:
#                 return False
#         else:
#             mapping_t_to_s[char_t] = char_s
#     print(mapping_s_to_t, mapping_t_to_s)
#     return True


# Example usage:
print(isIsomorphic("egg", "add"))     # Output: True
print(isIsomorphic("foo", "bar"))     # Output: False
print(isIsomorphic("paper", "title")) # Output: True