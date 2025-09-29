# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_time = 0
        for idx in range(1, len(points)):
            x1, y1 = points[idx - 1]
            x2, y2 = points[idx]
            total_time += max(abs(x2-x1), abs(y2-y1)) 
        return total_time

points = [[1,1],[3,4],[-1,0]]
#expected ouptut is 7
solution = Solution()
print(solution.minTimeToVisitAllPoints(points))


# Given two points (𝑥1,𝑦1)and (𝑥2,𝑦2), the time to move from one point to the other is determined 
# by the largest of the differences in their x-coordinates or y-coordinates.
# This is because you can move diagonally (covering both x and y directions) and when one of the differences is larger, you will need to cover the 
# remaining distance in that direction by moving horizontally or vertically.

# Thus, The time taken to move from (𝑥1,𝑦1) to (𝑥2,𝑦2) is max(|x2 - x1|, |y2 - y1|) seconds.

# Steps:
# Initialize a variable total_time to store the cumulative time taken.
# Iterate over the points, calculating the time needed to move from the current point to the next, and add this time to total_time.
# Return the total_time after processing all points.

