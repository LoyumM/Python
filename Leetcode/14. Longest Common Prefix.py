def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        temp_prefix = ""
        for idx in range(min(len(word), len(prefix))):
            if word[idx] == prefix[idx]:
                temp_prefix += word[idx]
            else:
                break
        prefix = temp_prefix
    return prefix

strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)

# could be made faster if we sort the strings first, take the first and last word and compare the two only
# which approach takes more time I think would depend on how many words there are
