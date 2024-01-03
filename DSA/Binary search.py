def bubble_sort(arr:list):
    """Sorts the array in ascending order

    Args:
        arr (list): The array to be sorted

    Returns:
        arr (list): The sorted array
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr





def binary_search(arr:list, target:int):
    """Returns the index of the target element from a sorted array

    Args:
        arr (list): A sorted array
        target (int): The target value to look for

    Returns:
        index (int): Index of the target value in the array
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10]
    find = 6
    print(binary_search(numbers, find))
