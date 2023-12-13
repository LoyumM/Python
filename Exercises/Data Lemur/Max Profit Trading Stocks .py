def max_subarray_sum(prices):
    diff = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > diff:
                diff = prices[j] - prices[i]
    return diff
            
print(max_subarray_sum([9, 1, 3, 6, 4, 8, 3, 5, 5]))