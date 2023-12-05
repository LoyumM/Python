def find_common_characters(strings):
    strings = [s.lower() for s in strings]
    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars.intersection_update(set(string))

    result = sorted(list(common_chars))
    return "[" + "][".join(result) + "]"

N = int(input())
strings = [input() for _ in range(N)]

print(find_common_characters(strings))