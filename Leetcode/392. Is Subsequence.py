# Decent enough two pointer solution
def issubsequence(s, t):
    idx1, idx2 = 0, 0
    while idx2 < len(t):
        if idx1 < len(s) and t[idx2] == s[idx1]:
            idx1 += 1
        idx2 += 1
    return idx1 == len(s)


s = "abc"
t = "ahbgdc"
# s , t = "axc", "ahbgdc"
print(issubsequence(s,t))