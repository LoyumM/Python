def max_three(input):
    input.sort()

    max_mul_pos = input[-1] * input[-2] * input[-3]
    max_mul_neg = input[0] * input[1] * input[-1]

    max_mul_mixed = max_mul_pos if max_mul_pos > max_mul_neg else max_mul_neg

    return max_mul_mixed