# brute force
def climbStairs(n: int):
    if n == 0 or n == 1:
        return 1

    ways = [0] * (n + 1)
    ways[0], ways[1] = 1, 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# brute force using recursion
def climbStairs(n:int):
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

# dynamic programming 
class Solution:
    def climbStairs(self, n:int):
        one, two = 1, 1
        
        for _ in range(n-1):
            temp = one 
            one = one + two
            two = temp
        return
    
# Example usage
solution = Solution()
stairs = []
for i in range(0, 40):
    n = i
    output = solution.climbStairs(n)
    print(f"Output for n={n}: {output}")
    stairs.append(output)

import matplotlib.pyplot as plt
# Plotting i on the y-axis and the corresponding number of ways on the x-axis
plt.plot(range(40), stairs, marker='o', linestyle='-', color='blue')
plt.title('Number of Ways to Climb Stairs')
plt.xlabel('Target number')
plt.ylabel('Number of Ways')
plt.grid(True)
# plt.show()
