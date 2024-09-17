# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Helper function to merge two sorted halves
        def merge_sort(people):
            if len(people) <= 1:
                return people

            mid = len(people) // 2
            left = merge_sort(people[:mid])
            right = merge_sort(people[mid:])

            return merge(left, right)

        # Helper function to merge two sorted arrays
        def merge(left, right):
            merged = []
            while left and right:
                # Compare heights, use the same sorting strategy as in the greedy solution
                if left[0][0] > right[0][0] or (left[0][0] == right[0][0] and left[0][1] <= right[0][1]):
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))

            return merged + left + right

        # Use merge sort to sort the people list
        sorted_people = merge_sort(people)
        
        # Initialize the result queue
        queue = []
        
        # Insert sorted people based on the 'k' value
        for person in sorted_people:
            queue.insert(person[1], person)

        return queue
    

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
solution = Solution()
print(solution.reconstructQueue(people))