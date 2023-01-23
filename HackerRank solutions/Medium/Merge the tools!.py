def merge_the_tools(string, k):
    substring = ""
    for inx, val in enumerate(string):
        if val not in substring:
            substring += val
        if (inx+1) % k == 0:
            print(substring)
            substring = ""
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)