def missing_int(input: list[int])-> int:
    for i in range(len(input)):
        if i not in input:
            return i
    return i+1
