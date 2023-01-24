def mutate_string(string, position, character):
    ls = list(string)
    ls[position] = character
    string = ''.join(ls)
    return string