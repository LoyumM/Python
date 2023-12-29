def merge_two_sorted_arrays(arr_a:list, arr_b:list):
    sorted_list = []
    len_a = len(arr_a)
    len_b = len(arr_b)
    i = j = 0
    while i < len_a and j < len_b:
        if arr_a[i] < arr_b[j]:
            sorted_list.append(arr_a[i])
            i += 1
        else:
            sorted_list.append(arr_b[j])
            j += 1
    while i < len_a:
        sorted_list.append(arr_a[i])
        i += 1
    while j < len_b:    
        sorted_list.append(arr_b[j])
        j += 1
    return sorted_list

def merge_sort(arr:list):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge_two_sorted_arrays(left, right)
    

if __name__ == "__main__":
    a = [5,7,12,56,89,100]
    b = [7,9,15,49]
    c = [10,3,5,4,30,1,12,43,8]
    print('hey')
    print(merge_two_sorted_arrays(a,b))
    print(merge_sort(c))