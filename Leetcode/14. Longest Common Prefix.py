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

# Example usage
strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)
