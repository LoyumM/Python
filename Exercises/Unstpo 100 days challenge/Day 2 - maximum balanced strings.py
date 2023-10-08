def balanced_string(s):
    result = ""
    r_count = 0
    l_count = 0

    for char in s:
        if char == 'R':
            r_count += 1
        elif char == 'L':
            l_count += 1        
        if r_count == l_count:
            result += "(" + s[:r_count + l_count] + ")"
            s = s[r_count + l_count:]
            r_count = 0
            l_count = 0
    return result


input_string = input()
output = balanced_string(input_string)
print(output)
