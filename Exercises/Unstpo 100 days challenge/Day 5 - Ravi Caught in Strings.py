n = int(input())
s = input()

def max_palindromic_substring(s:str, n:int):
    sub_str = ''
    max_palin = []
    for i in range(n):
        for j in range(n):
            sub_str = s[i:j+1]
            print(sub_str)
            if sub_str == sub_str[::-1]:
                max_palin.append(len(sub_str))
    return max(max_palin)

print(max_palindromic_substring(s, n))