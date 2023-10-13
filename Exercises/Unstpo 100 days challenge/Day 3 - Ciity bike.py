def city_biker(l:list):
    """This returns the highest altitude

    Args:
        l (list): list of all stop points

    Returns:
        _type_: an int value, specifying the max altitude
    """
    l = []
    init_val = 0
    l.append(init_val)
    for val in altitudes:
        init_val += int(val)
        l.append(init_val)

    max_val = l[0]
    for val in l:
        if val > max_val:
            max_val = val
    return max_val


N = int(input())
altitudes = input().split()
result = city_biker(altitudes)
print(result)
