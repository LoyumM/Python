def contains_duplicate(input)-> bool:
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            if input[i] == input[j]:
                return True
    return False

#alternate solution
def contains_duplicate(input)-> bool:
    return len(input) != len(set(input))