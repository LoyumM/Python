class Solution:
    def maxProfit(self, prices:list):
        min_price = prices[0]
        max_profit = 0
        for cur_price in prices[1:]:
            max_profit = max(max_profit, cur_price - min_price)
            min_price = min(min_price, cur_price)        
        return max_profit