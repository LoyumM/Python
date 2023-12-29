def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        less_than_pivot = [x for x in arr if x <= pivot]
        greater_than_pivot = [x for x in arr if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
result = quick_sort(my_list)
print("Quick Sorted array:", result)
