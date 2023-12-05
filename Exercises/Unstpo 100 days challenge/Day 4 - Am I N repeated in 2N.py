def repeated_2n(numbers:list, k:int):
    element_counts = {}

    for element in numbers:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    target_count = k // 2
    result_element = None

    for element, count in element_counts.items():
        if count == target_count:
            result_element = element
            break
    return result_element

k = int(input())    
numbers = list(map(int, input().split()))
print(repeated_2n(numbers, k))