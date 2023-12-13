#Brute-Force Solution: O(n)^2 complexity
def max_subarray_sum(prices):
    diff = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > diff:
                diff = prices[j] - prices[i]
    return diff
            
print(max_subarray_sum([9, 1, 3, 6, 4, 8, 3, 5, 5]))

# a solution with O(n) complexity
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for cur_price in prices[1:]:
        max_profit = max(max_profit, cur_price - min_price)
        min_price = min(min_price, cur_price)
    
    return max_profit