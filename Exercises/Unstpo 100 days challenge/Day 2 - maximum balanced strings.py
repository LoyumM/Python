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



#### chatGPT solution:

def balanced_string_split(s):
    result = []
    count = 0
    current_balanced = ""

    for char in s:
        if char == 'L':
            count += 1
        else:
            count -= 1
        
        current_balanced += char

        if count == 0:
            result.append(current_balanced)
            current_balanced = ""

    return "(" + ")(".join(result) + ")"

# Test case
input_str = input()
output_str = balanced_string_split(input_str)
print(output_str)
