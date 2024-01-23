# basic solution: Uses extra memory:
s = "A man, a plan, a canal: Panama"
def ispalindrome(s:str):
    n = ''.join([chr.lower() for chr in s if chr .isalnum()])
    return n == n[::-1]

print(ispalindrome(s))

    