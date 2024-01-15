import matplotlib.pyplot as plt

#brute force
# def climbStairs(n: int):
#     if n == 0 or n == 1:
#         return 1

#     ways = [0] * (n + 1)
#     ways[0], ways[1] = 1, 1

#     for i in range(2, n + 1):
#         ways[i] = ways[i - 1] + ways[i - 2]

#     return ways[n]

# brute force using recursion
def climbStairs(n:int):
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

# Example usage
stairs = []
for i in range(0, 30):
    n = i
    output = climbStairs(n)
    print(f"Output for n={n}: {output}")
    stairs.append(output)
    
# Plotting i on the y-axis and the corresponding number of ways on the x-axis
plt.plot(range(30), stairs, marker='o', linestyle='-', color='blue')
plt.title('Number of Ways to Climb Stairs')
plt.xlabel('Target number')
plt.ylabel('Number of Ways')
plt.grid(True)
plt.show()
    