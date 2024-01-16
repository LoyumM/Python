# obvious solution
class Solution:
    def coinChange(self, coins: list[int], amount: int):
        coins = sorted(coins)
        counter = 0
        target = 0
        idx = -1
        for index in range(-1, -(len(coins)), -1):
            try:
                while target < amount:
                    if target + coins[idx] < amount:
                        target += coins[idx]
                        counter += 1
                        print(f"target: {target}, counter: {counter}")
                    elif target + coins[idx] > amount:
                        idx -= 1
                        print(f"target: {target}, counter: {counter}, idx: {idx}")
                    elif target + coins[idx] == amount:
                        counter += 1
                        print(f"target: {target}, counter: {counter}")
                        return counter    
            except IndexError:
                counter = 0
                target = 0
                idx = index
        # target = 0
        # while target + min(coins) > amount:
        #     return 0

coins = [1,3,4,5]
amount = 7
solution = Solution()
res = solution.coinChange(coins, amount)
print(res)