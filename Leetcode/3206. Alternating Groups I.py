# There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)
        colors += colors #no duplicate counting as we're only iterating till len(colors)
        count = 0
        for i in range(n):
            if colors[i] == colors[i+2] and colors[i] != colors[i+1]:
                count += 1
        return count

colors = [0,1,0,0,1]
#Output: 3
# Explainiation: 0,1,10 ; 0,1,0 ; 1,0,1
solution = Solution()
print(solution.numberOfAlternatingGroups(colors))

