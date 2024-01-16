# obvious solution

class Solution:
    def coinChange(self, coins: list[int], amount: int):
        coins = sorted(coins)
        counter = 0
        target = 0
        idx = -1
        while target < amount:
            try:
                if target + coins[idx] < amount:
                    target += coins[idx]
                    counter += 1
                elif target + coins[idx] > amount:
                    idx -= 1
                elif target + coins[idx] == amount:
                    counter += 1
                    return counter    
            except IndexError:
                return -1
        target = 0
        while target + min(coins) > amount:
            return 0

coins = [1,2,3]
amount = 0
solution = Solution()
res = solution.coinChange(coins, amount)
print(res)