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


def max_subarray_sum(input):
    if not input:
        return 0

    max_sum = input[0]
    current_sum = input[0]

    for num in input[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max(0, max_sum)