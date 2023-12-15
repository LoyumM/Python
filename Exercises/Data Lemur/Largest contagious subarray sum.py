def max_subarray_sum(input):
    n = len(input)
    max_sum = 0
    for start_index in range(n):
        for end_index in range(start_index, n):
            cur_subarray_sum = 0
            for i in range(start_index, end_index+1):
                cur_subarray_sum += input[i]
            if cur_subarray_sum > max_sum:
                max_sum = cur_subarray_sum
    return max_sum