def ab_string(input_str):
    result = "YES"

    for i in range(1, len(input_str)):
        if input_str[i] == "a" and input_str[i-1] == "b":
            result = "NO"
            break
    return result

input_str = input()
print(ab_string(input_str))
                