# There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

# You may perform the following move any number of times:

# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

# Note that there may be multiple seats or students in the same position at the beginning.

#first attempt
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        count = 0
        # Iterate over each student
        for student in students:
            # Find the closest seat for this student
            min_diff = float('inf')
            closest_seat_index = -1
            for i, seat in enumerate(seats):
                diff = abs(student - seat)
                if diff < min_diff:
                    min_diff = diff
                    closest_seat_index = i
            # Add the minimum difference (moves) to the count
            count += min_diff
            # Remove the seat that was taken
            seats.pop(closest_seat_index)
        return count

# using sort
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        count = 0
        seats.sort()
        students.sort()
        for idx in range(len(seats)):
            count += abs(seats[idx] - students[idx])
        return count

seats = [4,1,5,9]
students = [1,3,2,6]
#Output: 7
instance = Solution()
print(instance.minMovesToSeat(seats, students))