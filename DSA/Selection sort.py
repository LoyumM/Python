def selection_sort(arr:list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
if __name__ == "__main__":
    tests = [[64,34,25,12],
            [3,2,4,1,5,8,7,6]]
    for test in tests:
        selection_sort(test)
        print(f"sorted array is: {test}")
        